--- The `nino` colourscheme.
---
--- It has a light and a dark variant. `vim.o.background` selects the variant,
--- as it does for other colourschemes. To load the scheme, use
--- `:colorscheme nino`.
---
--- The scheme keeps `Normal` transparent, so the terminal supplies the
--- background colour.

local palette = require("nino.palette")

local M = {}

--- @class Highlight
--- @field fg? Colour
--- @field bg? Colour
--- @field bold? boolean
--- @field italic? boolean
--- @field link? string Copy another group. All other fields are then ignored.

--- @param p Palette
--- @return table<string, Highlight>
local function highlights(p)
  local none = p.none
  return {
    -- Base
    Normal = { fg = none, bg = none },
    NormalNC = { fg = none, bg = none },
    Identifier = { fg = none, bg = none },
    Statement = { fg = none, bg = none },
    ["@variable"] = { fg = none, bg = none },

    String = { fg = p.string, bg = none },
    Constant = { fg = p.constant, bg = none },
    Function = { fg = p.func, bg = none },
    Comment = { fg = p.comment_fg, bg = p.comment_bg },
    ["@punctuation"] = { fg = p.punctuation },
    ["@keyword.return"] = { fg = p.keyword_control },
    ["@keyword.throw"] = { fg = p.keyword_control },
    SpecialChar = { fg = p.special_char, bold = true },
    Special = { link = "Normal" },
    Title = { link = "Normal" },
    htmlItalic = { italic = true },

    -- TypeScript
    typeScriptMagicComment = { bold = true },
    typeScriptCastKeyword = { bold = true },
    ["@keyword.cast"] = { link = "typeScriptCastKeyword" },
    ["@comment.magic"] = { link = "typeScriptMagicComment" },
    ["@string.regexp"] = { link = "Constant" },
    ["@character.special"] = { link = "Normal" },
    ["@string.special.url.tsx"] = { link = "Normal" },
    ["@markup.strong.tsx"] = { link = "Normal" },
    typescriptBraces = { link = "@punctuation" },
    typescriptParens = { link = "@punctuation" },
    typescriptMember = { link = "Identifier" },
    typescriptArrayMethod = { link = "Function" },
    typescriptDestructureLabel = { link = "String" },

    -- Floating windows and menus
    NormalFloat = { fg = none, bg = p.float_bg },
    FloatBorder = { fg = p.punctuation, bg = p.float_bg },
    Pmenu = { fg = none, bg = p.float_bg },
    PmenuSel = { fg = none, bg = p.select_bg },
    RenderMarkdownCode = { bg = p.code_bg },
    RenderMarkdownCodeInline = { bg = p.code_bg },

    -- Cursor, selection, and search
    Visual = { fg = none, bg = p.visual_bg },
    CursorLine = { bg = p.cursorline_bg },
    CursorColumn = { bg = p.float_bg },
    ColorColumn = { bg = p.float_bg },
    Search = { bg = p.select_bg },
    CurSearch = { bg = p.cursearch_bg },

    -- Status line and tab line
    StatusLine = { fg = p.status_fg, bg = p.status_bg, bold = true },
    StatusLineNC = { fg = p.status_nc_fg, bg = p.status_nc_bg },
    TabLine = { link = "StatusLineNC" },
    TabLineFill = { link = "StatusLineNC" },
    TabLineSel = { link = "StatusLine" },

    -- Diagnostics. The signs sit in the status line, so they use its
    -- background.
    DiagnosticSignError = { fg = p.error, bg = p.status_bg, bold = true },
    DiagnosticSignWarn = { fg = p.warn, bg = p.status_bg, bold = true },
    DiagnosticSignInfo = { fg = p.info, bg = p.status_bg, bold = true },
    DiagnosticSignHint = { fg = p.hint, bg = p.status_bg, bold = true },
    DiagnosticUnnecessary = { fg = p.unnecessary },
    DiagnosticUnderlineWarn = {},

    -- Diffs
    DiffAdd = { fg = none, bg = p.diff_add },
    DiffDelete = { bg = p.diff_delete },
    DiffChange = { bg = p.diff_change },
    DiffText = { bg = p.diff_text },
    diffAdded = { link = "DiffAdd" },
    diffRemoved = { link = "DiffDelete" },
    diffNewFile = { bold = true },
    diffOldFile = { bold = true },
  }
end

--- @param group string
--- @param spec Highlight
local function set_highlight(group, spec)
  if spec.link then
    vim.api.nvim_set_hl(0, group, { link = spec.link, force = true })
    return
  end
  vim.api.nvim_set_hl(0, group, {
    fg = spec.fg and spec.fg.gui,
    ctermfg = spec.fg and spec.fg.cterm,
    bg = spec.bg and spec.bg.gui,
    ctermbg = spec.bg and spec.bg.cterm,
    bold = spec.bold,
    italic = spec.italic,
    -- `nvim_set_hl` keeps the GUI and the terminal attributes apart, so the
    -- terminal needs its own copy.
    cterm = { bold = spec.bold, italic = spec.italic },
  })
end

--- Apply the colourscheme. `colors/nino.lua` calls this.
function M.load()
  vim.cmd("highlight clear")
  if vim.fn.exists("syntax_on") == 1 then
    vim.cmd("syntax reset")
  end
  vim.g.colors_name = "nino"

  local p = vim.o.background == "dark" and palette.dark or palette.light

  for group, spec in pairs(highlights(p)) do
    set_highlight(group, spec)
  end

  -- `guifg=bg` follows the background colour of `Normal`, which stays
  -- transparent. `nvim_set_hl` cannot hold such a reference, so use a command.
  vim.cmd("highlight Cursor guifg=bg guibg=" .. palette.cursor)
end

return M
