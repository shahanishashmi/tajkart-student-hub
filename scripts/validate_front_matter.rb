# Parse every Markdown front matter block and repository YAML inventory with Ruby's standard parser.

require "yaml"

front_matter = /\A---\s*\r?\n(.*?)\r?\n---(?:\s*\r?\n|\z)/m
markdown_files = Dir.glob("**/*.md", File::FNM_DOTMATCH).reject do |path|
  parts = path.split(/[\\\/]/)
  parts.any? { |part| [".", "..", ".git"].include?(part) } || parts.include?("vendor")
end

front_matter_count = 0
markdown_files.each do |path|
  source = File.read(path, encoding: "UTF-8")
  match = front_matter.match(source)
  next unless match

  metadata = YAML.safe_load(match[1], aliases: false)
  raise "front matter must be a mapping: #{path}" unless metadata.is_a?(Hash)

  front_matter_count += 1
end

yaml_files = ["_config.yml", ".github/dependabot.yml"] + Dir.glob("data/**/*.yml") + Dir.glob(".github/**/*.yml")
yaml_files.uniq.each do |path|
  next unless File.file?(path)

  YAML.safe_load_file(path, aliases: false)
end

puts "Parsed front matter in #{front_matter_count} Markdown files and #{yaml_files.uniq.length} YAML configuration/inventory files."
