-- [nfnl] fnldefaults.fnl
local util = require("fnlutils")
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
vim.opt.colorcolumn = {}
vim.opt.wildignorecase = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.linebreak = true
vim.opt.diffopt = (vim.opt.diffopt + {"vertical", "followwrap"})
vim.opt.diffopt = (vim.opt.diffopt + "iwhite")
vim.opt.diffopt = (vim.opt.diffopt + "linematch:40")
vim.opt.listchars = "tab:  ,nbsp:\226\144\163,trail:\226\136\183,extends:\226\134\146,precedes:\226\134\144"
vim.opt.fillchars = (vim.opt.fillchars + "eob:\194\183")
vim.opt.list = true
vim.opt.numberwidth = 1
vim.opt.rulerformat = "%{v:lua.diagnostic_sign()} %l/%L %P %c"
vim.opt.clipboard = "unnamed"
local function _1_()
  vim.fn.setreg("/", ("\\<" .. util["current-word"]() .. "\\>"))
  return vim.cmd("set hls")
end
vim.keymap.set("n", "<leader>d", _1_, {})
return {}
