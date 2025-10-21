--- @alias HighlightAttributes {
---   cterm: string,
---   ctermfg: string,
---   ctermbg: string,
---   gui: string,
---   guifg: string,
---   guibg: string,
--- }

--- @param group string
--- @param attrs HighlightAttributes
local function hi(group, attrs)
  local cmd = { "hi", group }
  for k, v in pairs(attrs) do
    table.insert(cmd, k .. "=" .. v)
  end
  vim.cmd(table.concat(cmd, " "))
end

--- @param group string
--- @param reference_group string
local function link_highlight(group, reference_group)
  vim.cmd("hi! link " .. group .. " " .. reference_group)
end

local function configure_light()
  vim.o.background = "light"
  vim.cmd("colorscheme default")
  vim.cmd("syntax reset")
  hi("Normal", { guibg = "none", guifg = "none", ctermbg = "none", ctermfg = "none" })
  hi("NormalNC", { guibg = "none", guifg = "none", ctermbg = "none", ctermfg = "none" })
  hi("Identifier", { guibg = "none", guifg = "none", ctermbg = "none", ctermfg = "none" })
  hi("@variable", { guibg = "none", ctermbg = "none" })
  hi(
    "String",
    { guibg = "none", guifg = "#009944", gui = "none", cterm = "none", ctermbg = "none", ctermfg = "darkgreen" }
  )
  hi("Constant", { guibg = "none", guifg = "#BB5500", gui = "none", cterm = "none", ctermbg = "none", ctermfg = "130" })
  hi("Statement", { guibg = "none", guifg = "none", gui = "none", cterm = "none", ctermbg = "none", ctermfg = "none" })
  hi("function", { guibg = "none", guifg = "#6600CC", gui = "none", cterm = "none", ctermbg = "none", ctermfg = "54" })
  hi("Comment", { guibg = "#FFFFEA", guifg = "#444400", ctermbg = "230", ctermfg = "58" })
  hi("@punctuation", { guifg = "#888888", ctermfg = "244" })

  hi("typeScriptMagicComment", { gui = "bold", cterm = "bold" })
  hi("typeScriptCastKeyword", { gui = "bold", cterm = "bold" })
  hi("DiagnosticUnnecessary", { guifg = "grey", ctermfg = "244" })
  link_highlight("@string.regexp.javascript", "Constant")
  link_highlight("@character.special.javascript", "Normal")
  link_highlight("typescriptBraces", "@punctuation")
  link_highlight("typescriptParens", "@punctuation")
  link_highlight("typescriptMember", "Identifier")
  link_highlight("typescriptArrayMethod", "function")
  link_highlight("typescriptDestructureLabel", "String")
  link_highlight("Special", "Normal")
  link_highlight("diffAdded", "DiffAdd")
  link_highlight("diffRemoved", "DiffDelete")

  hi("Visual", { guibg = "#FFFF00", ctermbg = "226" })
  hi("CursorLine", { guibg = "none", ctermbg = "none" })
  hi("CursorColumn", { guibg = "#EEEEEE", ctermbg = "255" })
  hi("ColorColumn", { guibg = "#EEEEEE", ctermbg = "255" })
  hi("Search", { guibg = "#AADDFF", ctermbg = "153" })
  hi("CurSearch", { guibg = "#3388CC", ctermbg = "68" })

  hi(
    "StatusLine",
    { guibg = "#3365BB", guifg = "white", gui = "bold", cterm = "bold", ctermbg = "61", ctermfg = "white" }
  )
  hi("StatusLineNC", { guibg = "#AADDFF", guifg = "black", ctermbg = "153", ctermfg = "black" })
  link_highlight("TabLine", "StatusLineNC")
  link_highlight("TabLineFill", "StatusLineNC")
  link_highlight("TabLineSel", "StatusLine")

  hi("DiffChange", { guibg = "#DDDDFF", ctermbg = "189" })
  hi("DiffAdd", { guibg = "#AFF3BC", ctermbg = "157" })
  hi("DiffDelete", { guibg = "#F9CCCC", gui = "none", cterm = "none", ctermbg = "224" })
end

-- Here's with fg colours:
-- local function configure_light()
--   vim.o.background = "light"
--   vim.cmd("colorscheme default")
--   vim.cmd("syntax reset")
--   hi("Normal", { guibg = "none", guifg = "none" })
--   hi("NormalNC", { guibg = "none", guifg = "none" })
--   hi("Identifier", { guibg = "none", guifg = "none" })
--   hi("@variable", { guibg = "none" })
--   hi("String", { guibg = "none", guifg = "#006622", gui = "none" })
--   hi("Constant", { guibg = "none", guifg = "#663300", gui = "none" })
--   hi("Statement", { guibg = "none", guifg = "none", gui = "none" })
--   hi("function", { guibg = "none", guifg = "#660066", gui = "none" })
--   hi("Comment", { guibg = "none", guifg = "#666600" })

--   hi("@punctuation", { guifg = "#333333" })
--   hi("CursorLine", { guibg = "#EEEEEE" })
--   hi("CursorColumn", { guibg = "#EEEEEE" })
--   hi("ColorColumn", { guibg = "#EEEEEE" })
-- end

--- Check whether macOS is set to light or dark mode, and update the
--- colourscheme accordingly.
function CheckAppearance()
  local theme = vim.fn.system("defaults read -g AppleInterfaceStyle"):gsub("\n", "")
  if theme == "Dark" then
    vim.o.background = "dark"
    vim.cmd("colorscheme retrobox")
    vim.cmd([[
      " hi Normal guibg=clear
      " hi TabLineSel guibg=#999999
      " hi DiagnosticUnderlineError gui=none
      " hi DiagnosticUnderlineWarn gui=none
      " hi DiffText cterm=bold gui=bold ctermbg=225 guibg=DarkRed
      " hi RenderMarkdown_bgtofg_RenderMarkdownCode guifg=#1e1e1e
      " hi NonText guifg=#333333
      " hi CursorLine guibg=#222244
      " hi htmlBold gui=bold
      " hi DiagnosticUnderlineError gui=underline guisp=#aa3333
      " hi AvanteConflictCurrent guibg=#421515
      " hi AvanteConflictIncoming guibg=#2c4215
    ]])
  else
    configure_light()
    -- vim.o.background = 'light'
    -- vim.cmd('colorscheme modus')
    -- vim.cmd [[
    --   hi Normal guibg=#EEEEEE
    --   hi NormalNC guibg=#EEEEEE
    --   " hi Pmenu guibg=#eeeeee
    --   " hi DiagnosticError guifg=#660000
    --   " hi DiagnosticFloatingHint guifg=#111111
    --   " hi TabLineSel guibg=#EEEEEE

    --   " hi DiffAdd guibg=#DDFFDD
    --   " hi DiffChange guibg=#DDFFDD
    --   " hi DiffText cterm=bold gui=bold ctermbg=225 guibg=#BBEEBB
    --   " hi DiffDelete guifg=#FFDDDD guibg=#FFEEEE
    --   " hi diffRemoved guibg=#FFEEEE

    --   " hi RenderMarkdown_bgtofg_RenderMarkdownCode guifg=#f2f2f2
    --   " hi NonText guifg=#eeeeee
    --   hi CursorLine guibg=#eaeaed
    --   hi CursorColumn guibg=#eeeeff
    --   hi ColorColumn guibg=#eeeeff
    --   " hi htmlBold gui=bold
    --   " hi DiagnosticUnderlineError gui=underline guisp=#f2AAAA
    --   " hi DiagnosticUnderlineWarn gui=underline guisp=#e2e222
    --   " hi DiagnosticUnderlineHint gui=underline guisp=#cccccc
    --   " hi SignColumn guibg=#eeeeee
    --   " hi LineNr guifg=#777777
    --   " hi Comment cterm=italic gui=italic guifg=#885588
    -- ]]
  end
  pcall(function()
    require("smear_cursor").setup({ cursor_color = "#FF00EE" })
  end)

  vim.cmd([[
    hi DiagnosticUnderlineError gui=none
    hi DiagnosticUnderlineWarn gui=none
    hi Cursor guibg=#FF00EE
    " hi Comment cterm=italic gui=italic
    hi htmlItalic gui=italic
    syntax match SpecialChar "…"
    syntax match SpecialChar "–"
    highlight SpecialChar guifg=#5555FF ctermfg=63 gui=bold cterm=bold
  ]])
end

CheckAppearance()
-- vim.api.nvim_create_user_command('CheckAppearance', function()
--   CheckAppearance()
-- end, {})
-- vim.api.nvim_create_autocmd("FocusGained", {
--   callback = function()
--     CheckAppearance()
--   end,
-- })
