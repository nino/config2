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
local function _3_()
  vim.bo.tabstop = 4
  vim.bo.softtabstop = 4
  vim.bo.shiftwidth = 4
  vim.bo.expandtab = true
  return nil
end
return vim.api.nvim_create_autocmd("FileType", {pattern = "cpp", callback = _3_})
