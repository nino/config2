--- Check whether macOS is set to light or dark mode, and update the
--- colourscheme accordingly.
function CheckAppearance()
  local theme = vim.fn.system('defaults read -g AppleInterfaceStyle'):gsub('\n', '')
  if theme == 'Dark' then
    vim.o.background = 'dark'
    vim.cmd('colorscheme modus_vivendi')
    vim.cmd [[
      hi DiffText cterm=bold gui=bold ctermbg=225 guibg=DarkRed
      hi RenderMarkdown_bgtofg_RenderMarkdownCode guifg=#1e1e1e
      hi NonText guifg=#333333
      hi CursorLine guibg=#222244
      hi htmlBold gui=bold
    ]]
  else
    vim.o.background = 'light'
    vim.cmd('colorscheme modus_operandi')
    vim.cmd [[
      hi DiffText cterm=bold gui=bold ctermbg=225 guibg=LightRed
      hi RenderMarkdown_bgtofg_RenderMarkdownCode guifg=#f2f2f2
      hi NonText guifg=#eeeeee
      hi CursorLine guibg=#eeeeff
      hi htmlBold gui=bold
    ]]
  end

  vim.cmd [[
    hi Comment cterm=italic gui=italic
    hi DiagnosticUnderlineError cterm=underline gui=undercurl
    hi htmlItalic gui=italic
    syntax match SpecialChar "…"
    syntax match SpecialChar "–"
    highlight SpecialChar guifg=#5555FF ctermfg=63 gui=bold cterm=bold
  ]]
end

CheckAppearance()
vim.api.nvim_create_user_command('CheckAppearance', function()
  CheckAppearance()
end, {})
-- vim.api.nvim_create_autocmd("FocusGained", {
--   callback = function()
--     CheckAppearance()
--   end,
-- })
