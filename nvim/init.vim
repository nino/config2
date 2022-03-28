" Deprecated, use initialize.lua instead

filetype off                  " required by Vundle

if has('nvim')
  let s:editor_root=expand("~/.config/nvim")
else
  let s:editor_root=expand("~/.vim")
endif

" set the runtime path to include Vundle and initialize
let &rtp = &rtp . ',' . s:editor_root . '/bundle/Vundle.vim/'
call vundle#begin(s:editor_root . '/bundle')
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-commentary'
Plugin 'tpope/vim-endwise'
Plugin 'mbbill/undotree'
Plugin 'tpope/vim-fugitive'
Plugin 'tpope/vim-rhubarb'
Plugin 'tpope/vim-surround'
Plugin 'SirVer/ultisnips'
Plugin 'raimondi/delimitmate'
Plugin 'neovim/node-host'
Plugin 'tpope/vim-repeat'
Plugin 'tpope/vim-ragtag'
Plugin 'mileszs/ack.vim'
Plugin 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plugin 'https://github.com/Shougo/ddc.vim'
Plugin 'https://github.com/vim-denops/denops.vim'
Plugin 'editorconfig/editorconfig-vim'
Plugin 'christoomey/vim-tmux-navigator'
Plugin 'ervandew/supertab'
Plugin 'godlygeek/tabular'
Plugin 'nino/itspronouncedmoove'
Plugin 'rizzatti/dash.vim'
Plugin 'keith/swift.vim'
Plugin 'preservim/nerdtree'
Plugin 'https://github.com/udalov/kotlin-vim'
Plugin 'tpope/vim-characterize'
Plugin 'https://github.com/guns/vim-sexp'
Plugin 'https://github.com/tpope/vim-sexp-mappings-for-regular-people'
Plugin 'https://github.com/morhetz/gruvbox'
Plugin 'https://github.com/fweep/vim-zsh-path-completion'
Plugin 'https://github.com/davidoc/taskpaper.vim'
Plugin 'https://github.com/petertriho/nvim-scrollbar'
Plugin 'https://github.com/gutenye/json5.vim'
Plugin 'https://github.com/jxnblk/vim-mdx-js'
Plugin 'https://github.com/neovim/nvim-lspconfig'
Plugin 'https://github.com/sickill/vim-monokai'
Plugin 'https://github.com/creativenull/diagnosticls-configs-nvim'
Plugin 'https://github.com/ziglang/zig.vim'
Plugin 'https://github.com/nino/bleepbloopvim'
Plugin 'https://github.com/nvim-treesitter/nvim-treesitter', { 'do': ':TSUpdate' }
Plugin 'https://github.com/jakwings/vim-pony'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

lua << EOF
  require("scrollbar").setup()
  require("initialize")
EOF


" DDC
call ddc#custom#patch_global('completionMode', 'manual')
call ddc#enable()

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

" RIPGREP

if executable('rg')
  " let g:ctrlp_user_command = 'rg --files %s'
  " let g:ctrlp_use_caching = 1
  " let g:ctrlp_working_path_mode = 'ra'
  " let g:ctrlp_switch_buffer = 'et'

  let g:ackprg = 'rg --vimgrep --no-heading --glob=!tags'
endif

" /RIPGREP

nnoremap <silent> <Leader>ut :UndotreeShow \| UndotreeFocus<CR>
nnoremap <silent> <Leader>uc :UndotreeHide<CR>

augroup quickfix
    autocmd!
    autocmd FileType qf setlocal nowrap
augroup END

augroup gitcommit
  autocmd!
  autocmd FileType gitcommit setlocal nowrap
augroup END

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

" Temp mappings

nnoremap gy mzggyG`z
" nnoremap <silent> <leader>r :wa<CR>:!tmux send-keys -tb up enter<CR><CR>

" Visual @
xnoremap @ :<C-u>call ExecuteMacroOverVisualRange()<CR>

function! ExecuteMacroOverVisualRange()
  echo "@".getcmdline()
  execute ":'<,'>normal @".nr2char(getchar())
endfunction
