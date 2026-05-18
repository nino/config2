vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2
vim.opt.textwidth = 80
vim.opt.expandtab = true
vim.opt.number = true
vim.opt.termguicolors = true
vim.opt.signcolumn = "number"
vim.opt.scrolloff = 1
vim.opt.sidescrolloff = 5
vim.opt.smartindent = false
vim.opt.autoread = true
vim.opt.cursorline = true
vim.opt.smoothscroll = true
vim.opt.cmdheight = 1
-- vim.opt.colorcolumn = {}
-- vim.opt.winborder = "double"
vim.opt.wildignorecase = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.linebreak = true
vim.opt.diffopt = vim.opt.diffopt + { "vertical", "followwrap" }
vim.opt.diffopt = vim.opt.diffopt + "iwhite"
vim.opt.diffopt = vim.opt.diffopt + "linematch:40"
vim.opt.listchars = "tab:  ,nbsp:␣,trail:∷,extends:→,precedes:←"
vim.opt.fillchars = vim.opt.fillchars + "eob:·"
vim.opt.list = true
vim.opt.numberwidth = 1
vim.opt.rulerformat = "%l/%L %P %c"
vim.opt.clipboard = "unnamed"

vim.keymap.set("n", "<leader>d", function()
  vim.fn.setreg("/", "\\<" .. vim.fn.expand("<cword>") .. "\\>")
  vim.cmd("set hls")
end)
