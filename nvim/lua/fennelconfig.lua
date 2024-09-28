-- [nfnl] Compiled from fennelconfig.fnl by https://github.com/Olical/nfnl, do not edit.
local function current_word()
  return vim.fn.expand("<cword>")
end
local function exec(cmd)
  local handle = io.popen(cmd)
  if handle then
    local result = handle:read("*a")
    handle:close()
    return result
  else
    return ""
  end
end
local function _2_()
  return exec(("open '" .. current_word() .. "'"))
end
vim.keymap.set("n", "gu", _2_)
vim.keymap.set("n", "<C-j>", vim.diagnostic.goto_next)
vim.keymap.set("n", "<C-k>", vim.diagnostic.goto_prev)
local function _3_()
  vim.bo.tabstop = 4
  vim.bo.softtabstop = 4
  vim.bo.shiftwidth = 4
  vim.bo.expandtab = true
  return nil
end
vim.api.nvim_create_autocmd("FileType", {pattern = "cpp", callback = _3_})
local function _4_()
  vim.o.breakindentopt = "shift:0"
  return nil
end
return vim.api.nvim_create_autocmd("FileType", {pattern = "markdown", callback = _4_})
