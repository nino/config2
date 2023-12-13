#!/usr/bin/env ruby

# WIP script to generate a graph of homebrew dependencies
# I was going to say:
# "I should rewrite this in Python to learn Python better", but Copilot
# autocompleted from "I should" to:
# "I should probably use the ruby homebrew API instead of shelling out"
# I wasn't aware of any such API, and I'm still not sure whether Copilot has
# made it up.

require "concurrent-ruby"

installed = `brew list`.lines.map(&:strip)

threadpool = Concurrent::FixedThreadPool.new(16)

futures = []
deps = Concurrent::Map.new
installed.each do |package|
  futures << Concurrent::Future.execute(executor: threadpool) do
    info = `brew info #{package}`.lines.map(&:strip)
    package_deps = info.select do |line|
      line.start_with?('Build:') || line.start_with?('Required:')
    end.flat_map { |line| line.gsub(/Build: |Required: /, '').split(/,? +/) }
    deps[package] = package_deps
    puts "Done #{package}"
  end
end

deps.keys
futures.each(&:wait)
puts deps
File.open("output.gv", "w") do |f|
  deps.each_pair do |k, v|
    v.each do |dep|
      f.puts "#{dep} -> #{k}"
    end
  end
end
