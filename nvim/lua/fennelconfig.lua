-- [nfnl] Compiled from fennelconfig.fnl by https://github.com/Olical/nfnl, do not edit.
local util = require("fnlutils")
vim.g["conjure#filetype#fennel"] = "conjure.client.fennel.nfnl"
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
  return vim.cmd(("!open " .. util["current-WORD"]()))
end
vim.keymap.set("n", "gu", _2_)
local cpp_indent
do
  local env = os.getenv("CPP_INDENT")
  if env then
    cpp_indent = tonumber(env)
  else
    cpp_indent = 4
  end
end
local function _4_()
  vim.bo.tabstop = cpp_indent
  vim.bo.softtabstop = cpp_indent
  vim.bo.shiftwidth = cpp_indent
  vim.bo.expandtab = true
  return nil
end
vim.api.nvim_create_autocmd("FileType", {pattern = "cpp", callback = _4_})
local function _5_()
  vim.o.breakindentopt = "shift:0"
  vim.bo.smartindent = false
  vim.bo.cindent = false
  return nil
end
vim.api.nvim_create_autocmd("FileType", {pattern = "markdown", callback = _5_})
local function _6_()
  vim.o.breakindentopt = "shift:0"
  vim.bo.smartindent = false
  vim.bo.cindent = false
  return nil
end
vim.api.nvim_create_autocmd("FileType", {pattern = "gitcommit", callback = _6_})
local function _7_()
  vim.bo.tabstop = 4
  vim.bo.shiftwidth = 4
  vim.bo.expandtab = false
  return nil
end
vim.api.nvim_create_autocmd("FileType", {pattern = "gdscript", callback = _7_})
return {}
