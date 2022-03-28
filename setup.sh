#!/usr/bin/bash

# This is very outdated

brew install neovim
brew install tmux
brew install python3
brew install n
brew install reattach-to-user-namespace
brew install ack
brew install ripgrep
brew install tig
brew cask install divvy
brew cask install bettertouchtool
brew cask install gitkraken
brew cask install launchbar
brew cask install iterm2
brew cask install google-chrome
brew cask install 1password

# Install Oh-my-zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
rm ~/.zshrc

ln -s ~/.config/tmux.conf ~/.tmux.conf
ln -s ~/.config/.ackrc ~/.ackrc
ln -s ~/.config/.tigrc ~/.tigrc
ln -s ~/.config/zsh/zshrc ~/.zshrc

pip install --upgrade pip
pip3 install --upgrade pip
pip install neovim
pip3 install neovim
npm i -g neovim
sudo gem install neovim
