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
  vim.api.nvim_set_hl(0, "DarkRainbowRed", { fg = "#450a0a" })
  vim.api.nvim_set_hl(0, "DarkRainbowYellow", { fg = "#713f12" })
  vim.api.nvim_set_hl(0, "DarkRainbowBlue", { fg = "#172554" })
  vim.api.nvim_set_hl(0, "DarkRainbowOrange", { fg = "#9a3412" })
  vim.api.nvim_set_hl(0, "DarkRainbowGreen", { fg = "#166534" })
  vim.api.nvim_set_hl(0, "DarkRainbowViolet", { fg = "#4a044e" })
  vim.api.nvim_set_hl(0, "DarkRainbowCyan", { fg = "#083344" })
end)

require("ibl").setup { indent = { highlight = highlight } }
