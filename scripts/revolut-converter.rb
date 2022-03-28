#!/usr/bin/env ruby

require "csv"

filepaths = ARGV

def dump_csv rows
  rows.each do |row|
    puts (row.join ',')
  end
end

def convert_file! path
  outputpath = path.gsub(/\.csv/, '-cleaned.csv')
  modified_content = CSV.parse(open(path).read)
  modified_content.each do |row|
    begin
      row[2] = row[2].gsub(/ .*$/, '') if row[2]
      row[3] = row[3].gsub(/ .*$/, '') if row[3]
    rescue
      puts row.inspect
    end
  end
  CSV.open(outputpath, 'w') do |file|
    modified_content.each do |row|
      file << row
    end
  end
end

filepaths.each do |filepath|
  convert_file! filepath
end


