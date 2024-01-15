if status is-interactive
    # Commands to run in interactive sessions can go here
end

fish_add_path /usr/local/bin
fish_add_path /opt/homebrew/bin
fish_add_path ~/.cargo/bin

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
alias uuid='uuidgen | tr -d "\n" | pbcopy'
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

maybe_source /usr/local/opt/asdf/libexec/asdf.fish
maybe_source /opt/homebrew/opt/asdf/libexec/asdf.fish

source ~/.config/secret-config2/fish/secret.fish
