#!/usr/bin/env ruby
# frozen_string_literal: true

dir_to_search = ARGV[0]
files = `fd -tf . '#{dir_to_search}'`.split("\n")

files_with_commits = []

files.each do |file|
  log =
    `git log --oneline --no-merges --pretty=format:"%ad%x09%s" --since=2021-01-01 --stat #{file}`.split(
      "\n\n"
    )
  additions = 0
  deletions = 0
  log.each do |commit|
    addition_match = commit.match(/(\d+) insertion/)
    additions += addition_match[1].to_i if !addition_match.nil?
    deletion_match = commit.match(/(\d+) deletion/)
    deletions += deletion_match[1].to_i if !deletion_match.nil?
  end
  files_with_commits << [file, additions + deletions]
end

files_with_commits.sort! { |a, b| a[1] <=> b[1] }

puts 'File,Number of commits'
files_with_commits.each { |fwc| puts "#{fwc[0]},#{fwc[1]}" }
