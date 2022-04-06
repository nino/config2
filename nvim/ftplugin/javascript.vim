iabbrev improt import

command! Atof :s/\vconst\s+([a-zA-Z0-9_$]+)\s*\=\s*\((.*)\)\s*\=\>\s*\{/function \1(\2) {/
