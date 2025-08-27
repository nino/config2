function wta
    if test (count $argv) -eq 0
        echo "Error: No branch name provided" >&2
        return 1
    end

    # Get the git directory
    set -l git_dir (git rev-parse --git-common-dir 2>/dev/null)

    if test -z "$git_dir"
        echo "Error: Not in a git repository" >&2
        return 1
    end

    # Get the main worktree root
    set -l repo_root (dirname $git_dir)

    # Construct the worktree path
    set -l worktree_path "$repo_root/worktree/$argv[1]"

    # Pass the constructed path and any additional arguments to git worktree add
    git worktree add $worktree_path $argv[2..-1]
end

function wtr
    if test (count $argv) -eq 0
        echo "Error: No worktree name provided" >&2
        return 1
    end

    # Get the git directory
    set -l git_dir (git rev-parse --git-common-dir 2>/dev/null)

    if test -z "$git_dir"
        echo "Error: Not in a git repository" >&2
        return 1
    end

    # Get the main worktree root
    set -l repo_root (dirname $git_dir)

    # Construct the worktree path
    set -l worktree_path "$repo_root/worktree/$argv[1]"

    # Remove the worktree
    git worktree remove $worktree_path $argv[2..-1]
end

function wtl
  git worktree list
end

# Completion for existing worktrees (for wtr)
function __fish_complete_worktrees
    set -l git_dir (git rev-parse --git-common-dir 2>/dev/null)
    if test -n "$git_dir"
        set -l repo_root (dirname $git_dir)
        if test -d "$repo_root/worktree"
            ls -1 "$repo_root/worktree" 2>/dev/null
        end
    end
end

# Completion for git branches (for wta)
function __fish_complete_git_branches
    git branch -a 2>/dev/null | string replace -r '^\*?\s+' '' | string replace -r '^remotes/' ''
end

# Set up completions
complete -c wta -f -a "(__fish_complete_git_branches)" -d "Branch"
complete -c wtr -f -a "(__fish_complete_worktrees)" -d "Worktree"
