(local util (require :fnlutils))

(set vim.opt.tabstop 2)
(set vim.opt.softtabstop 2)
(set vim.opt.shiftwidth 2)
(set vim.opt.textwidth 80)
(set vim.opt.expandtab true)
(set vim.opt.number true)
(set vim.opt.termguicolors true)
(set vim.opt.signcolumn "number")
(set vim.opt.scrolloff 1)
(set vim.opt.sidescrolloff 5)
(set vim.opt.smartindent false)
(set vim.opt.autoread true)
(set vim.opt.cursorline true)
(set vim.opt.smoothscroll true)
(set vim.opt.cmdheight 1)
(set vim.opt.colorcolumn [])

(set vim.opt.wildignorecase true)
(set vim.opt.ignorecase true)
(set vim.opt.smartcase true)
(set vim.opt.linebreak true)
(set vim.opt.diffopt (+ vim.opt.diffopt [ "vertical" "followwrap" ]))
(set vim.opt.diffopt (+ vim.opt.diffopt "iwhite"))
(set vim.opt.diffopt (+ vim.opt.diffopt "linematch:40"))
(set vim.opt.listchars "tab:  ,nbsp:␣,trail:∷,extends:→,precedes:←")
(set vim.opt.fillchars (+ vim.opt.fillchars "eob:·"))
(set vim.opt.list true)
(set vim.opt.numberwidth 1)
(set vim.opt.rulerformat "%{v:lua.diagnostic_sign()} %l/%L %P %c")
; (set vim.opt.lazyredraw true)

(set vim.opt.clipboard "unnamed")

(vim.keymap.set
  "n" "<leader>d"
  (λ [] (vim.fn.setreg "/" (.. "\\<" (util.current-word) "\\>"))
        (vim.cmd "set hls"))
  {})

{}
