set tabstop=4
set softtabstop=2
set shiftwidth=2
set textwidth=80
set expandtab

set wildignorecase
set ignorecase
set smartcase
set linebreak
set hidden
set mouse=a
set noswapfile
set diffopt+=vertical,followwrap

" Hopefully make Emoji show up correctly
" set ambiwidth=double

" Use system clipboard as default buffer
set clipboard=unnamed

set undofile
set undodir=~/.vim-undo

set backupdir=~/.local/share/nvim/backup
set backup

set foldmethod=manual
set wrap
set breakindent
set breakindentopt=shift:4
set title

" Preview changes made by :s and others
set inccommand=nosplit

" Keep the visual textwidth but don't add new line in insert mode:
set formatoptions-=t

let g:netrw_liststyle = 3
let g:netrw_banner = 0
let g:netrw_preview = 1 " Opens previews in a v-split

autocmd Filetype javascript setlocal omnifunc=v:lua.vim.lsp.omnifunc
