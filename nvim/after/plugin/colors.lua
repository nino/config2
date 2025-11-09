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
  link_highlight("@keyword.cast", "typeScriptCastKeyword")
  link_highlight("@comment.magic", "typeScriptMagicComment")
  hi("DiagnosticUnnecessary", { guifg = "grey", ctermfg = "244" })
  link_highlight("@string.regexp", "Constant")
  link_highlight("@character.special", "Normal")
  link_highlight("typescriptBraces", "@punctuation")
  link_highlight("typescriptParens", "@punctuation")
  link_highlight("typescriptMember", "Identifier")
  link_highlight("typescriptArrayMethod", "function")
  link_highlight("typescriptDestructureLabel", "String")
  link_highlight("Special", "Normal")
  link_highlight("Title", "Normal")
  link_highlight("diffAdded", "DiffAdd")
  link_highlight("diffRemoved", "DiffDelete")
  link_highlight("@string.special.url.tsx", "Normal")
  link_highlight("@markup.strong.tsx", "Normal")

  hi("Visual", { guibg = "#FFFF00", ctermbg = "226", ctermfg = "none" })
  hi("CursorLine", { guibg = "none", ctermbg = "none" })
  hi("CursorColumn", { guibg = "#EEEEEE", ctermbg = "255" })
  hi("ColorColumn", { guibg = "#EEEEEE", ctermbg = "255" })
  hi("Search", { guibg = "#AADDFF", ctermbg = "153" })
  hi("CurSearch", { guibg = "#3388CC", ctermbg = "68" })
  hi("diffNewFile", { gui = "bold", cterm = "bold" })
  hi("diffOldFile", { gui = "bold", cterm = "bold" })
  hi("@keyword.exception", { guifg = "#C64690", ctermfg = "205" })
  hi("@keyword.return", { guifg = "#C64690", ctermfg = "205" })

  hi(
    "StatusLine",
    { guibg = "#3365BB", guifg = "white", gui = "bold", cterm = "bold", ctermbg = "61", ctermfg = "white" }
  )
  hi("StatusLineNC", { guibg = "#AADDFF", guifg = "black", ctermbg = "153", ctermfg = "black" })
  link_highlight("TabLine", "StatusLineNC")
  link_highlight("TabLineFill", "StatusLineNC")
  link_highlight("TabLineSel", "StatusLine")

  hi("DiffChange", { guibg = "#DDDDFF", ctermbg = "189" })
  hi("DiffAdd", { guibg = "#AFF3BC", ctermbg = "157", ctermfg = "none", guifg = "none" })
  hi("DiffDelete", { guibg = "#F9CCCC", gui = "none", cterm = "none", ctermbg = "224" })
end

local function configure_dark()
  vim.o.background = "dark"
  vim.cmd("colorscheme default")
  vim.cmd("syntax reset")
  hi("Normal", { guibg = "none", guifg = "none", ctermbg = "none", ctermfg = "none" })
  hi("NormalNC", { guibg = "none", guifg = "none", ctermbg = "none", ctermfg = "none" })
  hi("Identifier", { guibg = "none", guifg = "none", ctermbg = "none", ctermfg = "none" })
  hi("@variable", { guibg = "none", guifg = "none", ctermfg = "none", ctermbg = "none" })
  hi(
    "String",
    { guibg = "none", guifg = "#66DD88", gui = "none", cterm = "none", ctermbg = "none", ctermfg = "lightgreen" }
  )
  hi("Constant", { guibg = "none", guifg = "#FFAA66", gui = "none", cterm = "none", ctermbg = "none", ctermfg = "216" })
  -- hi("Statement", { guibg = "none", guifg = "none", gui = "none", cterm = "none", ctermbg = "none", ctermfg = "none" })
  hi("function", { guibg = "none", guifg = "#BB88FF", gui = "none", cterm = "none", ctermbg = "none", ctermfg = "141" })
  hi("Comment", { guibg = "#222200", guifg = "#AAAA66", ctermbg = "234", ctermfg = "143" })
  hi("@punctuation", { guifg = "#888888", ctermfg = "244" })

  link_highlight("Statement", "Normal")
  hi("typeScriptMagicComment", { gui = "bold", cterm = "bold" })
  hi("typeScriptCastKeyword", { gui = "bold", cterm = "bold" })
  link_highlight("@keyword.cast", "typeScriptCastKeyword")
  link_highlight("@comment.magic", "typeScriptMagicComment")
  hi("DiagnosticUnnecessary", { guifg = "grey", ctermfg = "244" })
  link_highlight("@string.regexp.javascript", "Constant")
  link_highlight("@character.special", "Normal")
  link_highlight("@character.special.typescript", "Normal")
  link_highlight("typescriptBraces", "@punctuation")
  link_highlight("typescriptParens", "@punctuation")
  link_highlight("typescriptMember", "Identifier")
  link_highlight("typescriptArrayMethod", "function")
  link_highlight("typescriptDestructureLabel", "String")
  link_highlight("Special", "Normal")
  link_highlight("Title", "Normal")
  link_highlight("diffAdded", "DiffAdd")
  link_highlight("diffRemoved", "DiffDelete")
  link_highlight("@string.special.url.tsx", "Normal")
  link_highlight("@markup.strong.tsx", "Normal")

  hi("Visual", { guibg = "#555500", ctermbg = "58", ctermfg = "none" })
  hi("CursorLine", { guibg = "none", ctermbg = "none" })
  hi("CursorColumn", { guibg = "#222222", ctermbg = "235" })
  hi("ColorColumn", { guibg = "#222222", ctermbg = "235" })
  hi("Search", { guibg = "#005588", ctermbg = "24" })
  hi("CurSearch", { guibg = "#3388CC", ctermbg = "68" })
  hi("diffNewFile", { gui = "bold", cterm = "bold" })
  hi("diffOldFile", { gui = "bold", cterm = "bold" })

  hi(
    "StatusLine",
    { guibg = "#3365BB", guifg = "white", gui = "bold", cterm = "bold", ctermbg = "61", ctermfg = "white" }
  )
  hi("StatusLineNC", { guibg = "#223355", guifg = "#AAAAAA", ctermbg = "237", ctermfg = "248" })
  link_highlight("TabLine", "StatusLineNC")
  link_highlight("TabLineFill", "StatusLineNC")
  link_highlight("TabLineSel", "StatusLine")

  hi("DiffChange", { guibg = "#222244", ctermbg = "235" })
  hi("DiffAdd", { guibg = "#223322", ctermbg = "22", ctermfg = "none", guifg = "none" })
  hi("DiffDelete", { guibg = "#442222", gui = "none", cterm = "none", ctermbg = "52" })
end

--- Check whether macOS is set to light or dark mode, and update the
--- colourscheme accordingly.
function CheckAppearance()
  local theme = vim.fn.system("defaults read -g AppleInterfaceStyle"):gsub("\n", "")
  if theme == "Dark" then
    configure_dark()
  else
    configure_light()
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
