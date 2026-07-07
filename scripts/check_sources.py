#!/usr/bin/env python3
"""
check_sources.py
================
Parses sections/12-sources.md in the Rotavirus Argentina repo, extracts every
DOI and URL, then performs HEAD/GET accessibility checks against each target.

Three categories of URLs handled:
  - https://doi.org/...           -- resolved via DOI convention
  - https://*.org/...             -- generic publisher URLs
  - https://web.archive.org/web/2*/...  -- archive.org wildcard (always 200)

The script does NOT consider dead URLs a hard failure -- it reports them as
warnings and exits with code 0. Only structural source-table errors (missing
mandatory columns, broken markdown) raise exit code 2.

Usage:
  python scripts/check_sources.py                # check all sources
  python scripts/check_sources.py --source 4     # check only source #4
  python scripts/check_sources.py --json         # JSON report
  python scripts/check_sources.py --timeout 5    # 5s timeout per URL

Exit codes:
  0  no dead URLs found (or all are wildcards)
  1  at least one URL is unreachable
  2  structural error in 12-sources.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path

# Force UTF-8 output (Windows consoles)
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "sections" / "12-sources.md"

# Patterns to extract URL/DOI rows from the markdown table
# Each source row: | # | Source | [doi:X](url) | [archived](archive_url) |
TABLE_ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*\[(?:archived|linked)\]\(([^)]+)\)\s*\|",
    re.MULTILINE,
)
# Also accept rows with just URL column (no archived link)
TABLE_ROW_RE_NO_ARCHIVE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|",
    re.MULTILINE,
)

USER_AGENT = "rotavirus-argentina-evidence/0.3 (+https://github.com/open-evidence-ar/rotavirus-argentina)"


@dataclass
class SourceCheck:
    id: int
    name: str
    link_text: str
    url: str
    archive_url: str
    status_code: int = 0
    accessible: bool = False
    note: str = ""
    elapsed_ms: int = 0


def head_or_get(url: str, timeout: float) -> tuple[int, str]:
    """Attempt HEAD, fall back to GET if HEAD returns 405. Returns (code, body_snippet_or_empty)."""
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, ""
    except urllib.error.HTTPError as e:
        if e.code in (405, 403):
            # Some publishers reject HEAD; attempt GET
            try:
                req = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    return resp.status, ""
            except urllib.error.HTTPError as e2:
                return e2.code, ""
            except Exception:
                return 0, ""
        return e.code, ""
    except urllib.error.URLError:
        return 0, ""
    except Exception:
        return 0, ""


def is_wildcard_archive(url: str) -> bool:
    """archive.org wildcard URLs (with /2*/) always 200 -- skip real HTTP."""
    return "web.archive.org/web/2*/" in url


def check_one(src: SourceCheck, timeout: float) -> None:
    """Run HEAD/GET against the URL, classify, set status fields."""
    if is_wildcard_archive(src.url):
        src.status_code = 200
        src.accessible = True
        src.note = "archive.org wildcard -- always 200 by URL structure"
        src.elapsed_ms = 0
        return
    if src.url.startswith("[") or not src.url.startswith("http"):
        src.note = "not a valid HTTP URL"
        src.accessible = False
        src.elapsed_ms = 0
        return

    start = time.time()
    code, _ = head_or_get(src.url, timeout)
    elapsed = int((time.time() - start) * 1000)
    src.elapsed_ms = elapsed
    src.status_code = code
    src.accessible = (200 <= code < 400)
    if code == 403:
        src.note = "publisher returned 403 (may be rate-limited or paywalled; verify manually)"
    elif code == 0:
        src.note = "no response (timeout or DNS failure)"


def parse_sources_table(md_text: str) -> list[SourceCheck]:
    """Extract numbered source rows from 12-sources.md.

    Each row contributes one primary URL. Wildcard archive URLs are stored in
    archive_url. Rows without a trailing archive link are still accepted.
    """
    sources: list[SourceCheck] = []
    seen_ids: set[int] = set()

    for match in TABLE_ROW_RE.finditer(md_text):
        sid = int(match.group(1))
        if sid in seen_ids:
            continue
        seen_ids.add(sid)
        sources.append(
            SourceCheck(
                id=sid,
                name=match.group(2).strip(),
                link_text=match.group(3).strip(),
                url=match.group(4).strip(),
                archive_url=match.group(5).strip(),
            )
        )

    # No rows with archive column: try simpler table format (just ID | name | URL)
    if not sources:
        for match in TABLE_ROW_RE_NO_ARCHIVE.finditer(md_text):
            sid = int(match.group(1))
            if sid in seen_ids:
                continue
            seen_ids.add(sid)
            sources.append(
                SourceCheck(
                    id=sid,
                    name=match.group(2).strip(),
                    link_text=match.group(3).strip(),
                    url=match.group(4).strip(),
                    archive_url="",
                )
            )

    return sources


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", type=int, default=None, help="check only this source id")
    parser.add_argument("--timeout", type=float, default=10.0, help="per-URL timeout in seconds")
    parser.add_argument("--json", action="store_true", help="emit JSON report to evidence/sources-report.json")
    parser.add_argument("--verbose", "-v", action="store_true", help="print every source result")
    args = parser.parse_args()

    if not SOURCES_FILE.is_file():
        print(f"ERROR: sources file not found at {SOURCES_FILE}", file=sys.stderr)
        return 2

    md_text = SOURCES_FILE.read_text(encoding="utf-8")
    sources = parse_sources_table(md_text)

    if not sources:
        print(f"ERROR: no source rows parsed from {SOURCES_FILE.name}", file=sys.stderr)
        return 2

    print("=" * 72)
    print(f"checking {len(sources)} sources from {SOURCES_FILE.name}")
    print("=" * 72)

    targets = sources
    if args.source is not None:
        targets = [s for s in sources if s.id == args.source]
        if not targets:
            print(f"ERROR: no source #{args.source} found in table", file=sys.stderr)
            return 2

    broken: list[SourceCheck] = []
    for src in targets:
        check_one(src, args.timeout)
        marker = "PASS" if src.accessible else "FAIL"
        if args.verbose or not src.accessible:
            print(f"[{marker}] #{src.id} {src.link_text[:30]:30s} <- {src.url[:60]}")
            print(f"        code={src.status_code}  elapsed={src.elapsed_ms}ms  note={src.note}")
        if not src.accessible:
            broken.append(src)

    ok_count = sum(1 for s in targets if s.accessible)
    print("=" * 72)
    print(f"RESULT: {ok_count}/{len(targets)} sources accessible")
    print(f"        {len(broken)} unreachable within {args.timeout}s timeout")
    print("=" * 72)

    if args.json:
        out = ROOT / "evidence" / "sources-report.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(
                {
                    "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "sources_total": len(sources),
                    "checked_count": len(targets),
                    "ok_count": ok_count,
                    "broken": [asdict(b) for b in broken],
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"JSON report -> {out}")

    # Exit codes: 0=ok, 1=at least one unreachable, 2=structural error (handled above)
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
