local highlight = {
  "DarkRainbowRed",
  "DarkRainbowYellow",
  "DarkRainbowBlue",
  "DarkRainbowOrange",
  "DarkRainbowGreen",
  "DarkRainbowViolet",
  "DarkRainbowCyan",
}

local hooks = require "ibl.hooks"
-- create the highlight groups in the highlight setup hook, so they are reset
-- every time the colorscheme changes
hooks.register(hooks.type.HIGHLIGHT_SETUP, function()
  if vim.o.bg == 'light' then
    vim.api.nvim_set_hl(0, "DarkRainbowRed", { fg = "#fecaca" })
    vim.api.nvim_set_hl(0, "DarkRainbowYellow", { fg = "#f0f0D0" })
    vim.api.nvim_set_hl(0, "DarkRainbowBlue", { fg = "#bae6fd" })
    vim.api.nvim_set_hl(0, "DarkRainbowOrange", { fg = "#fed7aa" })
    vim.api.nvim_set_hl(0, "DarkRainbowGreen", { fg = "#bbf7d0" })
    vim.api.nvim_set_hl(0, "DarkRainbowViolet", { fg = "#ddd6fe" })
    vim.api.nvim_set_hl(0, "DarkRainbowCyan", { fg = "#a5f3fc" })
  else
    vim.api.nvim_set_hl(0, "DarkRainbowRed", { fg = "#450a0a" })
    vim.api.nvim_set_hl(0, "DarkRainbowYellow", { fg = "#713f12" })
    vim.api.nvim_set_hl(0, "DarkRainbowBlue", { fg = "#172554" })
    vim.api.nvim_set_hl(0, "DarkRainbowOrange", { fg = "#9a3412" })
    vim.api.nvim_set_hl(0, "DarkRainbowGreen", { fg = "#166534" })
    vim.api.nvim_set_hl(0, "DarkRainbowViolet", { fg = "#4a044e" })
    vim.api.nvim_set_hl(0, "DarkRainbowCyan", { fg = "#083344" })
  end
end)

require("ibl").setup { indent = { highlight = highlight } }
