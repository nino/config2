if status is-interactive
    # Commands to run in interactive sessions can go here
end

fish_add_path /opt/homebrew/bin
fish_add_path /usr/local/bin
fish_add_path ~/.cargo/bin
fish_add_path ~/.config/scripts
fish_add_path ~/.local/context-osx-64/bin

alias l='eza -lh'
alias la='eza -lha'
alias ls='ls'
alias dum='diskutil unmount'
alias js='jekyll serve --watch'
alias pastepd='pbpaste | pandoc --smart --css css.css'
alias pdtex='pandoc --template ~/Google\ Drive/Other\ Shit/pandoc-template.tex'
alias osajsi='osascript -i -l JavaScript'
alias v='nvim'
alias vi='nvim'
alias vim='nvim'
alias vs='nvim -S ~/Prevsession.vim'
alias bb='bbedit'
alias vimserv='NVIM_LISTEN_ADDRESS=/tmp/neovim/neovim nvim'
alias vv='/Applications/VV.app/Contents/Resources/bin/vv'
alias zhrc='bbedit ~/.zshrc'
alias zshrc='bbedit ~/.zshrc'
alias tmconf='bbedit ~/.tmux.conf'
alias tst='tig status'
alias vc='nvim -S `ls | grep .vim | fzf`'
alias ydl="youtube-dl -f 'best[ext=mp4]' "
alias yda="youtube-dl -x --audio-format mp3 "
alias ct='ctags -R .'
alias uuid='uuidgen | tr -d "\n" | tr "[:upper:]" "[:lower:]" | pbcopy'
alias myarn='git checkout upstream/develop -- yarn.lock && yarn && git add yarn.lock'
alias beep="echo -ne '\007' && sleep 1 && echo -ne '\007' && sleep 1 && echo -ne '\007'"
alias com="git add . && git commit -m"
alias awk='gawk'
alias dockre='docker'
alias yran='yarn'
alias yanr='yarn'
alias ynar='yarn'
alias ynra='yarn'
alias ayrn='yarn'
alias vlime='sbcl --load ~/.local/share/nvim/lazy/vlime/lisp/start-vlime.lisp'
alias rvlime='rlwrap sbcl --load ~/.local/share/nvim/lazy/vlime/lisp/start-vlime.lisp'

function save
  if test -z $argv;
    git commit && git push
  else
    git commit -m $argv && git push
  end
end

function saveall
  git add .
  save $argv
end

function mcd
  mkdir $argv && cd $argv
end

direnv hook fish | source

function maybe_source
  if test -f $argv
    source $argv
  end
end

source ~/.config/fish/git.fish
source ~/.config/secret-config2/fish/secret.fish
if [ -f ~/credentials ];
  source ~/credentials
end

if [ -e /usr/local/bin/nvim ];
  export EDITOR=/usr/local/bin/nvim
end

export REACT_EDITOR='cursor'
export EDITOR='cursor'
export VISUAL='cursor'
export CMAKE_EXPORT_COMPILE_COMMANDS=true
export PACKERPATH=$HOME/.local/share/nvim/site/pack/packer/start
export HOMEBREW_AUTO_UPDATE_SECS=600
export CMAKE_GENERATOR=Ninja
export CMAKE_PREFIX_PATH="/opt/homebrew:$CMAKE_PREFIX_PATH"
export MAKEFLAGS="-j16"
export VCPKG_ROOT=$HOME/code-friends/vcpkg
fish_add_path $VCPKG_ROOT
# export VCPKG_TARGET_ARCHITECTURE=x64
export PKG_CONFIG_PATH="$VCPKG_ROOT/installed/$TRIPLET/lib/pkgconfig:$PKG_CONFIG_PATH"
export CMAKE_TOOLCHAIN_FILE="$VCPKG_ROOT/scripts/buildsystems/vcpkg.cmake"
export TRIPLET='arm64-osx'

function co
  set -l branch (git lb | uniquelines | fzf)
  if [ -z "$1" ];
    gco $branch
  else if [ "$1" = "merge" ];
    eval "git merge \"$branch\""
  end
  # local branch="$( git branch | sed s/\*/\ /g | awk '{ print $1 }' | fzf)"
  # if [ ! -z $branch ]; then
  #   if [ -z $1 ]; then
  #     git checkout "$branch"
  #   elif [ "$1" = "tig" ]; then
  #     eval "tig \"$branch\""
  #   else
  #     local command="git $1 \"$branch\""
  #     eval $command
  #   fi
  # fi
end


function cheat.sh
    curl cheat.sh/$argv
end

# register completions (on-the-fly, non-cached, because the actual command won't be cached anyway
complete -c cheat.sh -xa '(curl -s cheat.sh/:list)'

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
# if test -f /usr/local/Caskroom/miniconda/base/bin/conda
#     eval /usr/local/Caskroom/miniconda/base/bin/conda "shell.fish" "hook" $argv | source
# else
#     if test -f "/usr/local/Caskroom/miniconda/base/etc/fish/conf.d/conda.fish"
#         . "/usr/local/Caskroom/miniconda/base/etc/fish/conf.d/conda.fish"
#     else
#         set -x PATH "/usr/local/Caskroom/miniconda/base/bin" $PATH
#     end
# end
# <<< conda initialize <<<


~/.local/bin/mise activate fish | source
fish_add_path /Users/Nino/.modular/bin
