--- Check whether macOS is set to light or dark mode, and update the
--- colourscheme accordingly.
function CheckAppearance()
    local theme = vim.fn.system('defaults read -g AppleInterfaceStyle'):gsub('\n', '')
    if theme == 'Dark' then
        vim.o.background = 'dark'
        vim.cmd('colorscheme modus_vivendi')
    else
        vim.o.background = 'light'
        vim.cmd('colorscheme modus_operandi')
    end
end

CheckAppearance()

-- vim.cmd [[ colorscheme lunaperche ]]
-- vim.o.bg='light'
vim.cmd [[
  hi Comment cterm=italic gui=italic
  hi DiagnosticUnderlineError cterm=underline gui=undercurl
]]

if vim.o.bg == 'light' then
  vim.cmd [[
    hi DiffText cterm=bold gui=bold ctermbg=225 guibg=LightRed

  ]]
else
  vim.cmd [[
    hi DiffText cterm=bold gui=bold ctermbg=225 guibg=DarkRed
  ]]
end

vim.cmd [[
  syntax match SpecialChar "…"
  syntax match SpecialChar "–"
  highlight SpecialChar guifg=#5555FF ctermfg=63 gui=bold cterm=bold
]]

