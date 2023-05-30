local utils = require "utils"

local mod = {}

function mod.light_colors()
  vim.o.background = "light"
  utils.color("catppuccin")
  -- utils.color("zellner")
end


function mod.catppuccin_dark()
  vim.o.background = "dark"
    require("catppuccin").setup({
        flavour = "macchiato", -- latte, frappe, macchiato, mocha
        background = { -- :h background
            light = "latte",
            dark = "mocha",
        },
        transparent_background = false,
        show_end_of_buffer = false, -- show the '~' characters after the end of buffers
        term_colors = false,
        dim_inactive = {
            enabled = false,
            shade = "dark",
            percentage = 0.15,
        },
        no_italic = true, -- Force no italic
        no_bold = false, -- Force no bold
        styles = {
            comments = {},
            conditionals = {},
            loops = {},
            functions = {},
            keywords = {},
            strings = {},
            variables = {},
            numbers = {},
            booleans = {},
            properties = {},
            types = {},
            operators = {},
        },
        color_overrides = {},
        custom_highlights = {},
    })
    utils.color("catppuccin")
end


function mod.catppuccin()
  vim.o.background = "light"
    require("catppuccin").setup({
        flavour = "latte", -- latte, frappe, macchiato, mocha
        background = { -- :h background
            light = "latte",
            dark = "mocha",
        },
        transparent_background = false,
        show_end_of_buffer = false, -- show the '~' characters after the end of buffers
        term_colors = false,
        dim_inactive = {
            enabled = false,
            shade = "dark",
            percentage = 0.15,
        },
        no_italic = true, -- Force no italic
        no_bold = false, -- Force no bold
        styles = {
            comments = {},
            conditionals = {},
            loops = {},
            functions = {},
            keywords = {},
            strings = {},
            variables = {},
            numbers = {},
            booleans = {},
            properties = {},
            types = {},
            operators = {},
        },
        color_overrides = {},
        custom_highlights = {},
    })
    utils.color("catppuccin")
end

function mod.everforest()
  vim.o.background = "light"
  vim.cmd [[
    let g:everforest_background = 'hard'
    let g:everforest_enable_italic = 0
    let g:everforest_disable_italic_comment = 1
  ]]
  utils.color("everforest")
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
