Jekyll::Hooks.register :site, :post_write do |site|
  sections_dir = site.source + "/sections"
  includes_dir = site.source + "/_includes"
  output_path  = site.dest + "/llms-full.txt"

  config_file  = site.source + "/_config.yml"
  metadata_file = site.source + "/source-metadata.yml"

  canonical_order = %w[
    section-authors.md
    section-nomenclature.md
    00-methodology.md
    01-objective.md
    02-vaccine-timeline.md
    03-disease-burden.md
    04-death-risk.md
    05-intussusception-risk.md
    06-ses-gradient.md
    07-risk-benefit.md
    08-post-vaccination.md
    09-cost-benefit.md
    10-equity-paradox.md
    section-counterclaims.md
    11-conclusions.md
    section-revisions.md
    12-sources.md
    annex-a-factcheck.md
    annex-b-glossary.md
  ]

  badge_map = {
    "derivado" => "\u25c7 Derivado",
    "supuesto" => "\u25b3 Supuesto",
    "observado" => "\u25ce Observado",
    "exploratorio" => "\u25cb Exploratorio",
  }

  def read_file(path)
    File.exist?(path) ? File.read(path, encoding: "utf-8") : ""
  end

  def yaml_val(text, key)
    text.each_line do |line|
      s = line.strip
      if s.start_with?(key + ":")
        v = s[(key.length + 1)..].strip
        v = v[1..-2] if v.start_with?('"') && v.end_with?('"')
        return v
      end
    end
    ""
  end

  def strip_front_matter(text)
    if text.start_with?("---")
      end_idx = text.index("---", 3)
      return text[(end_idx + 3)..].lstrip if end_idx
    end
    text
  end

  def strip_html(text)
    text = text.gsub(/<span[^>]*>([^<]+)<\/span>/, '\1')
    text = text.gsub(/<br\s*\/?>/, ' ')
    text = text.gsub(/<\/(div|p|sup|code|strong|em|span|small)[^>]*>/, '')
    text = text.gsub(/<(div|p|sup|code|strong|em|span|small)[^>]*>/, '')
    text = text.gsub(/<a\s+[^>]*>/, '')
    text = text.gsub(/<\/a>/, '')
    text
  end

  def resolve_includes(text, includes_dir, badge_map)
    # calculo boxes
    text = text.gsub(/\{%\s*include\s+tags\/calculo\.html\s+.*?%\}/m) do |match|
      formula = match[/formula="((?:[^"\\]|\\.)*)"/, 1] || ""
      resultado = match[/resultado="((?:[^"\\]|\\.)*)"/, 1] || ""
      nota = match[/nota="((?:[^"\\]|\\.)*)"/, 1] || ""
      nota = nota.gsub(/<span[^>]*>([^<]+)<\/span>/, '\1')
      parts = ["**C\u00e1lculo:**"]
      parts << " `#{formula}`" unless formula.empty?
      parts << " **= #{resultado}**" unless resultado.empty?
      parts << " _(#{nota})_" unless nota.empty?
      parts.join
    end

    # fuente
    text = text.gsub(/\{%\s*include\s+tags\/fuente\.html\s+.*?%\}/m) do |match|
      num = match[/numero="((?:[^"\\]|\\.)*)"/, 1] || "?"
      texto = match[/texto="((?:[^"\\]|\\.)*)"/, 1] || "Fuente"
      url = match[/url="((?:[^"\\]|\\.)*)"/, 1] || ""
      result = "[#{num}]"
      result << " #{texto} (#{url})" unless url.empty? || texto.empty?
      result
    end

    # nnya
    text = text.gsub(/\{%\s*include\s+tags\/nnya\.html\s+.*?%\}/m) do |match|
      cantidad = match[/cantidad="((?:[^"\\]|\\.)*)"/, 1] || ""
      nota = match[/nota="((?:[^"\\]|\\.)*)"/, 1] || ""
      r = cantidad.empty? ? "**NNyA**" : "**#{cantidad} NNyA**"
      r << " (#{nota})" unless nota.empty?
      r
    end

    # ratio
    text = text.gsub(/\{%\s*include\s+tags\/ratio\.html\s+.*?%\}/m) do |match|
      valor = match[/valor="((?:[^"\\]|\\.)*)"/, 1] || ""
      i = match[/interpretacion="((?:[^"\\]|\\.)*)"/, 1] || ""
      r = valor.empty? ? "**Ratio**" : "**Ratio:** #{valor}"
      r << " \u2014 #{i}" unless i.empty?
      r
    end

    # simple badges
    badge_map.each do |tag, label|
      text = text.gsub(/\{%\s*include\s+tags\/#{tag}\.html\s*%\}/, label)
    end

    # sourcing-policy.md
    sp_path = File.join(includes_dir, "sourcing-policy.md")
    sp_content = read_file(sp_path)
    text = text.gsub(/\{%\s*include\s+sourcing-policy\.md\s*%\}/, sp_content)

    # remaining HTML
    text = strip_html(text)
    text
  end

  # --- Build header ---
  cfg = read_file(config_file)
  md  = read_file(metadata_file)
  title = yaml_val(cfg, "title")
  desc  = yaml_val(cfg, "description")
  version = yaml_val(md, "version")
  version = "1.0.0" if version.empty?

  lines = []
  lines << "# #{title}"
  lines << ""
  lines << "> #{desc}"
  lines << "> Versi\u00f3n #{version} \u00b7 https://open-evidence-ar.github.io/rotavirus-argentina/"
  lines << "> _Archivo \u00fanico generado para consumo LLM \u2014 concatena todas las secciones del estudio_"
  lines << ""

  # --- Sections ---
  canonical_order.each do |filename|
    filepath = File.join(sections_dir, filename)
    unless File.exist?(filepath)
      lines << "\n---\n## #{filename}\n\n_*[Archivo no encontrado]*_\n"
      next
    end

    text = read_file(filepath)
    text = strip_front_matter(text).strip
    text = resolve_includes(text, includes_dir, badge_map)

    first_line = text.lines.first&.strip || ""
    if first_line.start_with?("## ")
      lines << "\n---\n"
      lines << text + "\n"
    else
      section_name = filename.sub(/\.md$/, "")
      lines << "\n---\n## #{section_name}\n"
      lines << text + "\n"
    end
  end

  File.write(output_path, lines.join("\n"), encoding: "utf-8")
  Jekyll.logger.info "llms-full.txt:", "generated (#{lines.join.length} bytes)"
end
