-- [nfnl] Compiled from fnlutils.fnl by https://github.com/Olical/nfnl, do not edit.
local function current_word()
  return vim.fn.expand("<cword>")
end
local function current_WORD()
  return vim.fn.expand("<cWORD>")
end
local function diagnostic_sign()
  local diagnostics = vim.diagnostic.get(0)
  local total = #diagnostics
  local errors
  do
    local count = 0
    for _, msg in pairs(diagnostics) do
      if (msg.severity == 1) then
        count = (count + 1)
      else
        count = count
      end
    end
    errors = count
  end
  if (total == 0) then
    return "\226\153\165\239\184\142"
  else
    if (errors == 0) then
      return "\226\138\153"
    else
      return "\195\151"
    end
  end
end
return {["current-word"] = current_word, ["current-WORD"] = current_WORD, ["diagnostic-sign"] = diagnostic_sign}
