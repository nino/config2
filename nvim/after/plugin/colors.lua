-- vim.cmd [[ colorscheme delek ]]
vim.cmd [[
  hi Comment cterm=italic gui=italic
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
