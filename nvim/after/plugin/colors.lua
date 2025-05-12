--- Check whether macOS is set to light or dark mode, and update the
--- colourscheme accordingly.
function CheckAppearance()
  local theme = vim.fn.system('defaults read -g AppleInterfaceStyle'):gsub('\n', '')
  if theme == 'Dark' then
    vim.o.background = 'dark'
    -- vim.cmd('colorscheme vim')
    vim.cmd [[
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
    -- vim.cmd('colorscheme vim')
    vim.cmd [[
      hi Normal guibg=clear
      " hi AvanteTitle guifg=#1e222a guibg=#98c379
      " hi AvanteReversedTitle guifg=#98c379
      " hi AvanteSubtitle guifg=#1e222a guibg=#56b6c2
      " hi AvanteReversedSubtitle guifg=#56b6c2
      " hi AvanteThirdTitle guifg=#abb2bf guibg=#353b45
      " hi AvanteReversedThirdTitle guifg=#353b45
      " hi AvanteConflictCurrent cterm=bold gui=bold guibg=#66ccff
      " hi AvanteConflictIncoming cterm=bold gui=bold guibg=#33ffaa
      " hi AvanteConflictCurrentLabel guibg=#6f393e
      " hi AvanteConflictIncomingLabel guibg=#3f5c6b
      " hi def link AvantePopupHint NormalFloat
      " hi def link AvanteInlineHint Keyword
      " hi clear AvantePromptInput
      " hi def link AvantePromptInputBorder NormalFloat

      " hi DiffText cterm=bold gui=bold ctermbg=225 guibg=LightRed
      " hi RenderMarkdown_bgtofg_RenderMarkdownCode guifg=#f2f2f2
      " hi NonText guifg=#eeeeee
      " hi CursorLine guibg=#eeeeff
      " hi htmlBold gui=bold
      " hi DiagnosticUnderlineError gui=underline guisp=#f29999
      " hi DiagnosticUnderlineWarn gui=underline guisp=#e2e222
      " hi DiagnosticUnderlineHint gui=underline guisp=#cccccc
      " hi SignColumn guibg=#eeeeee
      " hi LineNr guifg=#777777
    ]]
  end
  pcall(function()
    require('smear_cursor').setup({ cursor_color = "#FF00EE" })
  end)

  vim.cmd [[
    hi Cursor guibg=#FF00EE
    hi Comment cterm=italic gui=italic
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


