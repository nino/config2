local mod = {}

--- @param c string
--- @return integer
function mod.utf8_to_unicode_codepoint(c)
  local b1, b2, b3, b4 = c:byte(1, -1)
  local codepoint --- @type integer
  if b1 < 0x80 then
    codepoint = b1
  elseif b1 < 0xE0 then
    codepoint = (b1 - 0xC0) * 0x40 + b2 - 0x80
  elseif b1 < 0xF0 then
    codepoint = (b1 - 0xE0) * 0x1000 + (b2 - 0x80) * 0x40 + b3 - 0x80
  else
    codepoint = (b1 - 0xF0) * 0x40000 + (b2 - 0x80) * 0x1000 + (b3 - 0x80) * 0x40 + b4 - 0x80
  end
  return codepoint
end

--- Define a new digraph.
--- @param keys string
--- @param char string
--- @return nil
function mod.set_digraph(keys, char)
  vim.cmd("digraph " .. keys .. " " .. mod.utf8_to_unicode_codepoint(char))
end

--- Toggle an option
--- @param option string
--- @return nil
function mod.toggle_option(option)
  vim.o[option] = not vim.o[option]
end

--- Create a new command.
--- @param name string
--- @param fun function
--- @param info table
function mod.new_cmd(name, fun, info)
  vim.api.nvim_create_user_command(name, fun, info)
end

local run_once_functions = {}

function mod.run_once(description, fun)
  if not run_once_functions[description] then
    fun()
  end
  run_once_functions[description] = true
end

--- Find the remote's default branch (e.g. "origin/main" or "origin/master").
--- @param remote string|nil defaults to "origin"
--- @return string
function mod.git_default_branch(remote)
  remote = remote or "origin"
  local head = vim.fn.systemlist("git symbolic-ref --short refs/remotes/" .. remote .. "/HEAD")[1]
  if vim.v.shell_error == 0 and head and #head > 0 then
    return head
  end
  for _, name in ipairs({ "main", "master", "trunk", "develop" }) do
    local branch = remote .. "/" .. name
    vim.fn.system("git rev-parse --verify --quiet " .. branch)
    if vim.v.shell_error == 0 then
      return branch
    end
  end
  return remote .. "/main"
end

--- Cache of branch name -> diff base, so we only pay for `gh` once per branch.
--- @type table<string, string>
local diff_base_cache = {}

--- Forget any cached diff bases (e.g. after opening or retargeting a PR).
function mod.clear_diff_base_cache()
  diff_base_cache = {}
end

--- Find the ref to diff the current branch against: the base branch of its open
--- PR if there is one, otherwise the remote's default branch.
--- @param remote string|nil defaults to "origin"
--- @return string
function mod.git_diff_base(remote)
  remote = remote or "origin"
  local branch = vim.fn.systemlist("git rev-parse --abbrev-ref HEAD")[1]
  if vim.v.shell_error ~= 0 or not branch or #branch == 0 then
    return mod.git_default_branch(remote)
  end
  if diff_base_cache[branch] then
    return diff_base_cache[branch]
  end
  local base --- @type string|nil
  if vim.fn.executable("gh") == 1 then
    local out = vim.fn.systemlist("gh pr view --json baseRefName --jq .baseRefName 2>/dev/null")[1]
    if vim.v.shell_error == 0 and out and out:match("^[%w%._/%-]+$") then
      base = out
      -- Prefer the remote-tracking ref, which is what we actually want to diff against.
      vim.fn.system("git rev-parse --verify --quiet " .. remote .. "/" .. base)
      if vim.v.shell_error == 0 then
        base = remote .. "/" .. base
      end
    end
  end
  base = base or mod.git_default_branch(remote)
  diff_base_cache[branch] = base
  return base
end

--- Resolve the commit to diff a working file against: the merge base of HEAD
--- and `base` (defaults to `git_diff_base()`), so commits landed on the target
--- since we branched off don't show up as our changes.
--- @param base string|nil
--- @return string commit the commit to diff against
--- @return string ref the human-readable ref it came from
function mod.git_diff_base_commit(base)
  if not base or #base == 0 then
    base = mod.git_diff_base()
  end
  local merge_base = vim.fn.systemlist("git merge-base HEAD " .. base)[1]
  if vim.v.shell_error == 0 and merge_base and #merge_base > 0 then
    return merge_base, base
  end
  return base, base
end

--- Check whether `path` is tracked in `commit`.
--- @param commit string
--- @param path string absolute path to the file
--- @return boolean
function mod.git_path_in_commit(commit, path)
  if #path == 0 then
    return false
  end
  local dir = vim.fn.fnamemodify(path, ":h")
  local name = vim.fn.fnamemodify(path, ":t")
  -- `<rev>:./name` resolves relative to -C, so this works from any subdirectory.
  vim.fn.system({ "git", "-C", dir, "cat-file", "-e", commit .. ":./" .. name })
  return vim.v.shell_error == 0
end

--- Close every `fugitive://` window in the current tabpage, so stepping
--- through `:GD`'s quickfix list doesn't leave the previous file's diff pane
--- on screen. Fugitive windows in other tabs are left alone, and so is the
--- current window, whose buffer callers still need to resolve `%` against.
--- @return integer closed
function mod.close_fugitive_windows()
  local current = vim.api.nvim_get_current_win()
  local closed = 0
  for _, win in ipairs(vim.api.nvim_tabpage_list_wins(0)) do
    if win ~= current and vim.api.nvim_win_is_valid(win) then
      local name = vim.api.nvim_buf_get_name(vim.api.nvim_win_get_buf(win))
      -- pcall: a fugitive buffer with unsaved edits refuses to close.
      if vim.startswith(name, "fugitive://") and pcall(vim.api.nvim_win_close, win, false) then
        closed = closed + 1
      end
    end
  end
  return closed
end

--- Open `target` (a `<rev>:<path>` fugitive spec) in a vertical diff split,
--- unfold both panes, and leave the cursor where it started -- on the working
--- copy. Returning to the origin window by id rather than `wincmd l` keeps
--- this correct whichever side `Gvdiffsplit` puts the new window on.
--- @param target string
function mod.diff_split(target)
  local origin = vim.api.nvim_get_current_win()
  vim.cmd("Gvdiffsplit " .. target)
  vim.cmd("norm! zR")
  if vim.api.nvim_win_is_valid(origin) then
    vim.api.nvim_set_current_win(origin)
    vim.cmd("norm! zR")
  end
end

--- Run a shell command and populate the quickfix list with filenames from the output.
--- @param cmd string
--- @param title string|nil
function mod.shell_to_quickfix(cmd, title)
  local lines = vim.fn.systemlist(cmd)
  if vim.v.shell_error ~= 0 then
    vim.notify("Command failed: " .. cmd, vim.log.levels.ERROR)
    return
  end
  local items = {}
  for _, line in ipairs(lines) do
    if #line > 0 then
      table.insert(items, { filename = line, lnum = 1 })
    end
  end
  vim.fn.setqflist({}, " ", { title = title or cmd, items = items })
  vim.cmd("copen")
end

return mod
