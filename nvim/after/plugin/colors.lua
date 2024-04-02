if vim.o.bg == 'light' then
  vim.cmd [[
    hi Comment cterm=italic gui=italic
    hi DiffText cterm=bold gui=bold ctermbg=225 guibg=LightRed
  ]]
end
