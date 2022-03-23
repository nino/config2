" fun! s:SaveWorkDir()
"   call writefile(['cd ' . getcwd()], expand('~/.config/nvim/CurrentWorkingDirectory.vim'))
" endf

" autocmd! DirChanged * :call s:SaveWorkDir()

" autocmd! InsertLeave * :set nopaste
