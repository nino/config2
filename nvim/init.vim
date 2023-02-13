" Deprecated, use initialize.lua instead

filetype off                  " required by Vundle

if has('nvim')
  let s:editor_root=expand("~/.config/nvim")
else
  let s:editor_root=expand("~/.vim")
endif

if has('macunix')
  let g:coq_settings = { 'auto_start': 'shut-up', 'keymap.jump_to_mark': '' }
endif


call plug#begin()

" Install with
" sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

Plug 'tpope/vim-commentary'
Plug 'tpope/vim-endwise'
Plug 'mbbill/undotree'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-rhubarb'
Plug 'tpope/vim-surround'
" Plug 'SirVer/ultisnips'
" Plug 'raimondi/delimitmate'
Plug 'neovim/node-host'
Plug 'tpope/vim-repeat'
Plug 'tpope/vim-ragtag'
Plug 'mileszs/ack.vim'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'https://github.com/vim-denops/denops.vim'
Plug 'editorconfig/editorconfig-vim'
Plug 'christoomey/vim-tmux-navigator'
Plug 'godlygeek/tabular'
Plug 'nino/itspronouncedmoove'
Plug 'rizzatti/dash.vim'
Plug 'keith/swift.vim'
Plug 'preservim/nerdtree'
Plug 'https://github.com/udalov/kotlin-vim'
Plug 'tpope/vim-characterize'
Plug 'https://github.com/guns/vim-sexp'
Plug 'https://github.com/tpope/vim-sexp-mappings-for-regular-people'
Plug 'https://github.com/davidoc/taskpaper.vim'
Plug 'https://github.com/gutenye/json5.vim'
Plug 'https://github.com/jxnblk/vim-mdx-js'
Plug 'https://github.com/neovim/nvim-lspconfig'
Plug 'https://github.com/sickill/vim-monokai'
Plug 'https://github.com/creativenull/diagnosticls-configs-nvim'
Plug 'https://github.com/ziglang/zig.vim'
Plug 'https://github.com/nino/bleepbloopvim'
if has('macunix')
  Plug 'https://github.com/ms-jpq/coq_nvim'
  Plug 'https://github.com/ms-jpq/coq.artifacts', {'branch': 'artifacts'}
endif
Plug 'https://github.com/nvim-treesitter/nvim-treesitter', { 'do': ':TSUpdate' }
Plug 'https://github.com/nvim-treesitter/playground'
Plug 'https://github.com/davidoc/taskpaper.vim'
Plug 'https://github.com/koron/nyancat-vim'
Plug 'https://github.com/rescript-lang/vim-rescript'
Plug 'https://github.com/ellisonleao/gruvbox.nvim'
Plug 'https://github.com/mfussenegger/nvim-dap'
Plug 'https://github.com/leoluz/nvim-dap-go'
Plug 'https://github.com/rcarriga/nvim-dap-ui'
Plug 'https://github.com/theHamsta/nvim-dap-virtual-text'
" Plug 'https://github.com/nvim-telescope/telescope-dap.nvim'
Plug 'whonore/Coqtail'
call plug#end()

lua << EOF
  --  require("scrollbar").setup()
  require("initialize")
EOF


" --------------- External ---------------

runtime defaults.vim
runtime abbreviations.vim
runtime mappings.vim
runtime autocmds.vim
runtime Justify.vim

if has("gui_vimr")
  runtime CurrentWorkingDirectory.vim
endif

" ------------- / External ---------------
