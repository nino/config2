# Two-line prompt, ported from fish/functions/fish_prompt.fish:
# - green lines if the last command's exit status is OK, red otherwise
# - your user name, in red if root or yellow otherwise
# - your hostname, in cyan if ssh or blue otherwise
# - the current path
# - the current time
# - the current git branch, if any
#
# ┬─[nino@Hattori:~/w/dashboard]─[11:39:00]─[G:main]
# ╰─>$ echo here

setopt prompt_subst

if [ -n "$SSH_CLIENT" ]; then
    _prompt_host_color=cyan
else
    _prompt_host_color=blue
fi

# Branch name only - no dirty/untracked/stash checks, they make the prompt slow
# (the fish config disabled them too)
_prompt_git_segment() {
    local ref
    ref=$(git symbolic-ref --short HEAD 2>/dev/null) \
        || ref=$(git rev-parse --short HEAD 2>/dev/null) \
        || return
    print -rn -- "─%B%F{green}[%f%bG:$ref%B%F{green}]%f%b"
}

_prompt_status_color='%F{%(?.green.red)}'

PROMPT="${_prompt_status_color}┬─%f%B%F{green}[%f%b%B%F{%(!.red.yellow)}%n%f%b%B@%b%B%F{${_prompt_host_color}}%m%f%b:%~%B%F{green}]%f%b─%B%F{green}[%f%b%*%B%F{green}]%f%b\$(_prompt_git_segment)
${_prompt_status_color}╰─>%f%B%F{red}\$ %f%b"
