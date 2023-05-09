local utils = require "utils"

local mod = {}

function mod.light_colors()
  vim.o.background = "light"
  -- utils.color("lucius")
  utils.color("zellner")
end

function mod.gruvbox_dark()
  vim.o.background = "dark"

  -- utils.color("thing")
  -- utils.color("deus")
  -- utils.color("desert")

  require("gruvbox").setup({
    undercurl = false,
    underline = false,
    bold = true,
    italic = {},
    strikethrough = true,
    invert_selection = false,
    invert_signs = false,
    invert_tabline = false,
    invert_intend_guides = false,
    inverse = true,    -- invert background for search, diffs, statuslines and errors
    contrast = "hard", -- can be "hard", "soft" or empty string
    palette_overrides = {},
    overrides = {},
    dim_inactive = false,
    transparent_mode = false,
  })
  utils.color("gruvbox")

  utils.colorize("DiagnosticError", { fg = utils.rgb(4, 3, 1) })
end

function mod.pink_moon()
  vim.o.background = "dark"
  utils.color("pink-moon")
end

return mod
