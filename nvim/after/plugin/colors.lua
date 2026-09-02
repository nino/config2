-- VS Code controls the colour scheme when running in the neovim extension.
if vim.g.vscode then
  return
end

--- Check whether macOS is set to light or dark mode, and update the
--- colourscheme accordingly. The `nino` colourscheme has a variant for each
--- background, and it reads `background` to select one.
function CheckAppearance()
  local theme = vim.fn.system("defaults read -g AppleInterfaceStyle"):gsub("\n", "")
  vim.o.background = theme == "Dark" and "dark" or "light"
  vim.cmd.colorscheme("nino")

  pcall(function()
    require("smear_cursor").setup({ cursor_color = require("nino.palette").cursor })
  end)

  -- These are syntax rules, not highlight groups, so they stay out of the
  -- colourscheme. The colourscheme gives `SpecialChar` its colour.
  vim.cmd([[
    syntax match SpecialChar "…"
    syntax match SpecialChar "–"
  ]])
end

CheckAppearance()

-- macOS can switch appearance while neovim is in the background, so re-check
-- on focus rather than only at startup.
vim.api.nvim_create_autocmd("FocusGained", {
  group = vim.api.nvim_create_augroup("nino_appearance", { clear = true }),
  callback = CheckAppearance,
})
