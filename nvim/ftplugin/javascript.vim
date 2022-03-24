set shiftwidth=2
set tabstop=2
set softtabstop=2
set expandtab

iabbrev improt import

command! Atof :s/\vconst\s+([a-zA-Z0-9_$]+)\s*\=\s*\((.*)\)\s*\=\>\s*\{/function \1(\2) {/
