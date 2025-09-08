--- Check whether macOS is set to light or dark mode, and update the
--- colourscheme accordingly.
function CheckAppearance()
  local theme = vim.fn.system('defaults read -g AppleInterfaceStyle'):gsub('\n', '')
  if theme == 'Dark' then
    vim.o.background = 'dark'
    -- vim.cmd('colorscheme modus')
    vim.cmd [[
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
    ]]
  else
    vim.o.background = 'light'
    vim.cmd('colorscheme modus')
    vim.cmd [[
      " hi Normal guibg=clear
      " hi NormalNC guibg=clear
      " hi Pmenu guibg=#eeeeee
      " hi DiagnosticError guifg=#660000
      " hi DiagnosticFloatingHint guifg=#111111
      " hi TabLineSel guibg=#EEEEEE

      " hi DiffAdd guibg=#DDFFDD
      " hi DiffChange guibg=#DDFFDD
      " hi DiffText cterm=bold gui=bold ctermbg=225 guibg=#BBEEBB
      " hi DiffDelete guifg=#FFDDDD guibg=#FFEEEE
      " hi diffRemoved guibg=#FFEEEE

      " hi RenderMarkdown_bgtofg_RenderMarkdownCode guifg=#f2f2f2
      " hi NonText guifg=#eeeeee
      " hi CursorLine guibg=#fafafd
      " hi CursorColumn guibg=#eeeeff
      " hi ColorColumn guibg=#eeeeff
      " hi htmlBold gui=bold
      " hi DiagnosticUnderlineError gui=underline guisp=#f2AAAA
      " hi DiagnosticUnderlineWarn gui=underline guisp=#e2e222
      " hi DiagnosticUnderlineHint gui=underline guisp=#cccccc
      " hi SignColumn guibg=#eeeeee
      " hi LineNr guifg=#777777
      " hi Comment cterm=italic gui=italic guifg=#885588
    ]]
  end
  pcall(function()
    require('smear_cursor').setup({ cursor_color = "#FF00EE" })
  end)

  vim.cmd [[
    hi DiagnosticUnderlineError gui=none
    hi DiagnosticUnderlineWarn gui=none
    hi Cursor guibg=#FF00EE
    " hi Comment cterm=italic gui=italic
    hi htmlItalic gui=italic
    syntax match SpecialChar "…"
    syntax match SpecialChar "–"
    highlight SpecialChar guifg=#5555FF ctermfg=63 gui=bold cterm=bold
  ]]
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


