-- Keep buffers in sync with on-disk changes made by other tools (coding
-- agents, formatters, git checkouts).
--
-- 'autoread' only reloads when something actually runs `checktime` -- and nvim
-- does that on surprisingly few occasions, never while you sit idle in a
-- buffer. So we trigger it on the events that matter plus a slow background
-- timer for the unfocused case.

local mod = {}

local group = vim.api.nvim_create_augroup("AutoReload", { clear = true })

--- Checking is unsafe while the cmdline is open or an operator is pending: it
--- can interrupt what you're typing. Skip non-file buffers too (terminals,
--- neo-tree, trouble) -- they have nothing on disk to compare against.
--- @return boolean
local function safe_to_check()
  local mode = vim.fn.mode()
  if mode:match("^[cro!t]") then
    return false
  end
  return vim.bo.buftype == ""
end

local function checktime()
  if safe_to_check() then
    -- `silent!` because checktime errors on buffers with no backing file.
    vim.cmd("silent! checktime")
  end
end

vim.api.nvim_create_autocmd(
  { "FocusGained", "BufEnter", "CursorHold", "CursorHoldI", "TermLeave" },
  { group = group, callback = checktime }
)

-- Backstop for when nvim is unfocused and idle: neither FocusGained nor
-- CursorHold will fire, so nothing above would ever notice the change.
-- 2s is slow enough to be free, fast enough that alt-tabbing feels instant.
local timer = vim.uv.new_timer()
timer:start(
  2000,
  2000,
  vim.schedule_wrap(function()
    checktime()
  end)
)

-- Don't let a reload be silent -- a buffer changing under you without any
-- indication is worse than the stale contents.
vim.api.nvim_create_autocmd("FileChangedShellPost", {
  group = group,
  callback = function()
    vim.notify("Reloaded from disk (u to undo)", vim.log.levels.WARN)
  end,
})

--- Diff the current buffer against its on-disk contents.
---
--- For a modified buffer nvim's W12 prompt makes you choose blind; this shows
--- what you'd actually be choosing between. Close the scratch window (or
--- :diffoff!) to dismiss.
function mod.diff_disk()
  local src_buf = vim.api.nvim_get_current_buf()
  local path = vim.api.nvim_buf_get_name(src_buf)
  if path == "" then
    vim.notify("Buffer has no file on disk", vim.log.levels.ERROR)
    return
  end
  if vim.fn.filereadable(path) == 0 then
    vim.notify("Not readable on disk: " .. path, vim.log.levels.ERROR)
    return
  end

  local disk_lines = vim.fn.readfile(path)
  local filetype = vim.bo[src_buf].filetype
  local src_win = vim.api.nvim_get_current_win()

  vim.cmd("diffthis")

  vim.cmd("vertical rightbelow new")
  local scratch = vim.api.nvim_get_current_buf()
  vim.bo[scratch].buftype = "nofile"
  vim.bo[scratch].bufhidden = "wipe"
  vim.bo[scratch].swapfile = false
  vim.api.nvim_buf_set_lines(scratch, 0, -1, false, disk_lines)
  vim.bo[scratch].modifiable = false
  vim.bo[scratch].filetype = filetype
  vim.api.nvim_buf_set_name(scratch, "[on disk] " .. vim.fn.fnamemodify(path, ":~:."))
  vim.cmd("diffthis")

  -- Leave the source window in a clean state once the scratch goes away.
  vim.api.nvim_create_autocmd("BufWipeout", {
    buffer = scratch,
    once = true,
    callback = function()
      if vim.api.nvim_win_is_valid(src_win) then
        vim.api.nvim_win_call(src_win, function()
          vim.cmd("diffoff")
        end)
      end
    end,
  })
end

vim.api.nvim_create_user_command("DiffDisk", mod.diff_disk, {
  desc = "Diff the current buffer against its on-disk contents",
})

return mod
