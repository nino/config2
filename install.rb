# I should really update this at some point, but the general idea seems decent


require 'FileUtils'

HOME_PATH = File.expand_path '~'

config_files = %w(
  .zshrc .tmux.conf
  .zsh-update .yarnrc .rbenv
  .kwm .khdrc .ruby-version
  .hyper.js .eslintrc
)

issues = []

def should_delete? file_name
  loop do
    print "The file or folder #{file_name} already exists. Delete? (Y/n) "
    input = gets.chomp.downcase
    if input == 'y'
      return true
    else
      return false
    end
  end
end

config_files.each do |file_name|
  begin
    file_path = HOME_PATH + file_name

    if File.exists? file_path
      if should_delete? file_name
        FileUtils.rm_r file_path, force: true
      else
        issues << "#{file_name} has been skipped"
      end
    end

    source_path = File.join HOME_PATH, '.config', file_name
    destination_path = File.join HOME_PATH, file_name
    FileUtils.ln_s source_path, destination_path
  rescue
    issues << "Something went wrong with #{file_name}"
  end
end

puts issues.join "\n"
