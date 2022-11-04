# frozen_string_literal: true

require "rugged"

repo = Rugged::Repository.new("/Users/nino/immo/immo-platform")
branch = repo.head.name.gsub('refs/heads/', '')
issue_match = branch.match(/^\w+-\d+/)
if !issue_match.nil?
  puts issue_match[0]
else
  puts "No issue ID recognized"
end



