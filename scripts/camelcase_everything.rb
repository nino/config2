# frozen_string_literal: true

require 'pp'
require_relative 'camelcase'
require_relative 'gsub_in_file'

files = ARGV

def find_locals(file_contents)
  matches = file_contents.scan(/(const|let)\s+(\w[a-zA-Z_0-9]*)/)
  matches.reject(&:nil?).map { |match| match[1] }
end

files.each do |file|
  puts "Processing #{file}"
  file_contents = File.open(file).read

  locals = find_locals(file_contents)
  pp locals
  locals.each do |local|
    files.each do |inner_file|
      gsub_in_file(inner_file, /\b#{local}/, local.camelcase)
    end
  end
end
