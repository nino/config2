require("plugins")
require("abbreviations")

-- Defaults
vim.opt.tabstop = 4
vim.opt.softtabstop = 4
vim.opt.shiftwidth = 4
vim.opt.textwidth = 80
vim.opt.expandtab = true
vim.opt.number = true
vim.opt.termguicolors = true
vim.opt.signcolumn = "yes"
vim.opt.scrolloff = 4
vim.opt.smartindent = true
vim.opt.autoread = true

vim.opt.wildignorecase = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.linebreak = true
vim.opt.diffopt = vim.opt.diffopt + {"vertical" ,"followwrap"}
vim.opt.diffopt = vim.opt.diffopt + "iwhite"
vim.opt.diffopt = vim.opt.diffopt + "linematch:40"
vim.opt.listchars = "tab:→ ,nbsp:␣,trail:⌁,extends:→,precedes:←"
vim.opt.numberwidth = 1
vim.opt.rulerformat = '♥︎ %l/%L %P %c'

vim.opt.clipboard = "unnamed"

vim.opt.swapfile = false
vim.opt.wrap = true
vim.opt.undodir = os.getenv("HOME") .. "/.vim/undodir"
vim.opt.undofile = true

vim.opt.hlsearch = true
vim.opt.incsearch = true

vim.opt.foldmethod = "manual"
vim.opt.breakindent = true
vim.opt.breakindentopt = "shift:4"
vim.opt.title = true
vim.opt.inccommand = "nosplit"

-- Keep the visual textwidth but don't add new line in insert mode:
vim.opt.formatoptions = vim.opt.formatoptions - "t"

vim.opt.updatetime = 50

-- Mappings
vim.g.mapleader = " "

local telescope_builtin = require('telescope.builtin')
vim.keymap.set('n', '<leader>ff', telescope_builtin.find_files, {})
vim.keymap.set('n', '<leader>fg', telescope_builtin.live_grep, {})
vim.keymap.set('n', '<leader>fb', telescope_builtin.buffers, {})
vim.keymap.set('n', '<leader>fh', telescope_builtin.help_tags, {})

vim.keymap.set("x", "<leader>p", [["_dP]])

vim.keymap.set("n", "<c-s>", vim.cmd.w)
vim.keymap.set("n", ",s", vim.cmd.wa)
vim.keymap.set("n", "<esc>", vim.cmd.nohlsearch)

vim.keymap.set("n", "j", "gj")
vim.keymap.set("n", "k", "gk")
vim.keymap.set("n", "gj", "j")
vim.keymap.set("n", "gk", "k")

vim.keymap.set("n", "T", "gT")
vim.keymap.set("n", "t", "gt")
vim.keymap.set("v", "<", "<gv")
vim.keymap.set("v", ">", ">gv")
vim.keymap.set("n", "<Leader>c", "/<<<<<<<\\|=======\\|>>>>>>><CR>") 
vim.keymap.set("n", "<Leader>w", ":set wrap!<CR>")
vim.keymap.set("n", "<Leader>D", ":Gdiff<CR>")
vim.keymap.set("n", "<Leader>s", ":G<CR>")
vim.keymap.set("n", "zs", "v%zf")
vim.keymap.set("n", "zS", "$v%zf")


vim.keymap.set("n", "¬", "5zl")
vim.keymap.set("n", "˙", "5zh")
vim.keymap.set("n", "<M-l>", "5zl")
vim.keymap.set("n", "<M-h>", "5zh")
vim.keymap.set("n", "∑", "<c-w><c-c>")
vim.keymap.set("n", "<M-w>", "<c-w><c-c>")
vim.keymap.set("n", "ø", "<c-w><c-o>")
vim.keymap.set("n", "<M-o>", "<c-w><c-o>")

vim.keymap.set("n", "™", "@@")
vim.keymap.set("n", "<M-2>", "@@")

-- TODO map cp to copy the current file's path
