## gsub, but for files
def gsub_in_file(filepath, pattern, replacement)
  result = File.open(filepath).read.gsub(pattern, replacement)
  File.open(filepath, 'w') { |file| file.write(result) }
end

