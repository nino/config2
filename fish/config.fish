if status is-interactive
    # Commands to run in interactive sessions can go here
end

source ~/.asdf/asdf.fish
fish_add_path ~/.asdf/shims
fish_add_path ~/.asdf/bin
fish_add_path /usr/local/bin
fish_add_path /opt/homebrew/bin
fish_add_path ~/.cargo/bin
fish_add_path ~/.config/scripts

alias l='ls -l -h'
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
alias arst='asdf'
alias yran='yarn'
alias yanr='yarn'
alias ynar='yarn'
alias ynra='yarn'
alias ayrn='yarn'

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

if [ -e /usr/local/bin/nvim ];
  export EDITOR=/usr/local/bin/nvim
end

export EDITOR='nvim'
export VISUAL='nvim'
export CMAKE_EXPORT_COMPILE_COMMANDS=true

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

# opam configuration
source /Users/Nino/.opam/opam-init/init.fish > /dev/null 2> /dev/null; or true
