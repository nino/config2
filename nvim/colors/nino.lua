-- The `nino` colourscheme. See `lua/nino/init.lua` for the highlight groups
-- and `lua/nino/palette.lua` for the colours.

-- Forget the cached modules, so that `:colorscheme nino` shows the colours as
-- they are on disk while you edit them.
for module in pairs(package.loaded) do
  if module == "nino" or module:match("^nino%.") then
    package.loaded[module] = nil
  end
end

require("nino").load()
