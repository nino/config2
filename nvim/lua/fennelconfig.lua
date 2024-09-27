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
return vim.keymap.set("n", "gu", _2_)
