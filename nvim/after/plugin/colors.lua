-- vim.cmd [[ colorscheme ayu-light ]]
vim.o.bg='light'
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
