-- [nfnl] Compiled from fnlutils.fnl by https://github.com/Olical/nfnl, do not edit.
local function current_word()
  return vim.fn.expand("<cword>")
end
local function current_WORD()
  return vim.fn.expand("<cWORD>")
end
return {["current-word"] = current_word, ["current-WORD"] = current_WORD}
