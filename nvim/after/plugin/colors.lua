-- VS Code controls the colour scheme when running in the neovim extension.
if vim.g.vscode then
  return
end

vim.o.background = "dark"
vim.cmd("colorscheme lunaperche")
