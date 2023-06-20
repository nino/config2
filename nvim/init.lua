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
vim.opt.bg = 'dark'

vim.opt.wildignorecase = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.linebreak = true
vim.opt.diffopt = vim.opt.diffopt + { "vertical", "followwrap" }
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
vim.g.maplocalleader = ","

local telescope_builtin = require('telescope.builtin')
local telescope = require("telescope")
vim.keymap.set('n', '<leader>ff', function() telescope_builtin.git_files({ show_untracked = true }) end, {})
vim.keymap.set('n', '<leader>F', telescope_builtin.find_files, {})
vim.keymap.set('n', '<leader>fg', telescope.extensions.live_grep_args.live_grep_args, {})
vim.keymap.set('n', '<leader>fb', telescope_builtin.buffers, {})
vim.keymap.set('n', '<leader>fh', telescope_builtin.help_tags, {})

vim.keymap.set("x", "<leader>P", [["0p]])

vim.keymap.set("n", "<leader>d",
    function()
        vim.fn.setreg('/', '\\<' .. vim.fn.expand('<cword>') .. '\\>'); vim.cmd "set hls"
    end, {})


vim.keymap.set("n", "<c-s>", vim.cmd.w)
vim.keymap.set("n", "<localleader>s", vim.cmd.wa)
vim.keymap.set("n", "<esc>", vim.cmd.nohlsearch)

vim.keymap.set("n", "j", "gj")
vim.keymap.set("n", "k", "gk")
vim.keymap.set("n", "gj", "j")
vim.keymap.set("n", "gk", "k")

vim.keymap.set("n", "T", "gT")
vim.keymap.set("n", "t", "gt")
vim.keymap.set("n", "<Leader>t", function() vim.cmd("tabe") end)
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

vim.keymap.set("n", "<M-n>", ":cnext<CR>")
vim.keymap.set("n", "<M-p>", ":cprev<CR>")
vim.keymap.set("n", "<C-n>", vim.diagnostic.goto_next)
vim.keymap.set("n", "<C-p>", vim.diagnostic.goto_prev)
vim.keymap.set("n", "<M-a>", vim.lsp.buf.code_action)

vim.keymap.set("n", "™", "@@")
vim.keymap.set("n", "<M-2>", "@@")

vim.keymap.set("n", "<leader>ut", ":UndotreeToggle<CR>")
vim.keymap.set("n", "_", vim.lsp.buf.format)
vim.keymap.set("n", "<leader>-", ":!eslint --fix %<cr>")
vim.keymap.set("n", "<leader>p", ":!prettier --write %<cr>")

vim.keymap.set("n", "cp", function()
    local filepath = vim.fn.expand('%')
    os.execute("echo '" .. filepath .. "' | pbcopy")
end)

vim.cmd [[imap <silent><script><expr> <C-J> copilot#Accept("\<CR>")]]

vim.cmd [[command! -range=% DP :<line1>,<line2>diffput]]
vim.api.nvim_create_user_command("GP", function() vim.cmd(":Git push -u") end, {})
vim.api.nvim_create_user_command("NF", function() vim.cmd(":NERDTreeFind") end, {})
vim.api.nvim_create_user_command("NT", function() vim.cmd(":NERDTreeToggle") end, {})

vim.cmd [[
function! s:MkNonExDir(file, buf)
    if empty(getbufvar(a:buf, '&buftype')) && a:file!~#'\v^\w+\:\/'
        let dir=fnamemodify(a:file, ':h')
        if !isdirectory(dir)
            call mkdir(dir, 'p')
        endif
    endif
endfunction
augroup BWCCreateDir
    autocmd!
    autocmd BufWritePre * :call s:MkNonExDir(expand('<afile>'), +expand('<abuf>'))
augroup END

" Visual @
xnoremap @ :<C-u>call ExecuteMacroOverVisualRange()<CR>

function! ExecuteMacroOverVisualRange()
  echo "@".getcmdline()
  execute ":'<,'>normal @".nr2char(getchar())
endfunction
]]
