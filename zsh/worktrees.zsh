# ported from fish/worktrees.fish

wta() {
    if [ $# -eq 0 ]; then
        echo "Error: No branch name provided" >&2
        return 1
    fi

    local worktree_path="$1"

    # Pass the constructed path and any additional arguments to git worktree add
    git worktree add ~/.claude-worktrees/$worktree_path "${@:2}"
}

wtam() {
    wta "$1" -b "$1" $TRUNKBRANCHNAME
}

wtax() {
    ## FYI this doesn't actually work yet
    if [ $# -eq 0 ]; then
        echo "Error: No branch name provided" >&2
        return 1
    fi

    local branch_name="$1"
    local current_dir=$(pwd)

    # Get the git directory and repo root
    local git_dir=$(git rev-parse --git-common-dir 2>/dev/null)

    if [ -z "$git_dir" ]; then
        echo "Error: Not in a git repository" >&2
        return 1
    fi

    local repo_root=$(dirname $git_dir)
    local worktree_path="$repo_root/worktree/$branch_name"

    # Create new tmux session with the branch name, starting in current directory
    tmux new-session -d -s $branch_name -c $current_dir

    # Run gfmm && wta to create the worktree, then cd into it
    tmux send-keys -t $branch_name:0 "gfmm && wta $branch_name -b $branch_name master && cd $worktree_path" C-m

    # Wait a moment for the worktree to be created
    sleep 1

    # Open nvim in tab 0
    tmux send-keys -t $branch_name:0 "nvim" C-m

    # Create a new tab with two panes
    tmux new-window -t $branch_name:1 -c $worktree_path

    # Split the window vertically
    tmux split-window -t $branch_name:1 -h -c $worktree_path

    # Left pane: yarn && yarn dev
    tmux send-keys -t $branch_name:1.0 "yarn && yarn dev" C-m

    # Right pane: yarn exec tsc -- --noEmit --watch
    tmux send-keys -t $branch_name:1.1 "yarn exec tsc -- --noEmit --watch" C-m

    # Switch to the new session
    tmux switch-client -t $branch_name
}

wtr() {
    if [ $# -eq 0 ]; then
        echo "Error: No worktree name provided" >&2
        return 1
    fi

    local worktree_path=~/.claude-worktrees/$1

    git worktree remove $worktree_path "${@:2}"
}

wtl() {
    git worktree list
}

# Completion for git branches (for wta)
_wta_branches() {
    local -a branches
    branches=(${(f)"$(git branch -a 2>/dev/null | sed -E 's/^\*?[[:space:]]*//' | sed -E 's/^remotes\///')"})
    (( ${#branches} )) && _describe 'branch' branches
}

# Completion for existing worktrees (for wtr)
_wtr_worktrees() {
    local -a worktrees
    if [ -d ~/.claude-worktrees ]; then
        worktrees=(${(f)"$(find ~/.claude-worktrees -mindepth 1 -maxdepth 2 -type d -exec test -e '{}/.git' \; -print 2>/dev/null | sed "s|$HOME/.claude-worktrees/||")"})
    fi
    (( ${#worktrees} )) && _describe 'worktree' worktrees
}

# Set up completions (compinit must have run already)
if (( $+functions[compdef] )); then
    compdef _wta_branches wta
    compdef _wtr_worktrees wtr
fi
