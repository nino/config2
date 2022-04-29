nnoremap <silent> <Leader>fp :w<CR>:!prettier-eslint --print-width=100 --arrow-parens always --trailing-comma es5 --write '%'<CR>:e!<CR>
nnoremap <silent> <Leader>ff :w<CR>:!prettier --single-quote --trailing-comma es5 --arrow-parens always --print-width 100 --write '%'<CR>:e!<CR>
nnoremap <silent> <Leader>fm :w<CR>:!prettier --write --prose-wrap=always '%'<CR>:e!<CR>
nnoremap <silent> <Leader>pp :w<CR>:!prettier --trailing-comma=all --write '%'<CR>:e!<CR>
nnoremap <silent> <Leader>pn :w<CR>:!prettier --trailing-comma=all --use-tabs --tab-width=4 --write '%'<CR>:e!<CR>
nnoremap <silent> <Leader>pw :w<CR>:!prettier --trailing-comma=all --use-tabs --tab-width=8 --print-width=100 --write '%'<CR>:e!<CR>

" nnoremap _ F r_
" nnoremap - f r_

nnoremap <silent> <Leader>d :let @/ = '\<' . expand('<cword>') . '\>' \|set hls<C-M>

vnoremap <silent> <c-n> "2y:let @/ = @2\|set hls<C-M>

nnoremap <C-P> :FZF<CR>
vnoremap <C-P> "2y:exe 'FZF -q ' . @2<CR>
nnoremap <C-S> :w<CR>
" inoremap <Tab> <C-N>
" inoremap <S-Tab> <C-P>
"
" <TAB>: completion.
inoremap <silent><expr> <TAB>
\ ddc#map#pum_visible() ? '<C-n>' :
\ (col('.') <= 1 <Bar><Bar> getline('.')[col('.') - 2] =~# '\s') ?
\ '<TAB>' : ddc#map#manual_complete()
nnoremap ,s :wa<CR>

inoremap {<CR> {<CR>}<ESC>O
inoremap {,<CR> {<CR>},<ESC>O
inoremap {;<CR> {<CR>};<ESC>O
inoremap [<CR> [<CR>]<ESC>O
inoremap [,<CR> [<CR>],<ESC>O
inoremap [;<CR> [<CR>];<ESC>O

nnoremap Y y$

nnoremap <C-x> :cprev<CR>zz
nnoremap <C-q> :cnext<CR>zz

nnoremap <Leader>m 0f{lr<CR>f}hr<CR>k:s/, /,\r/g<CR>

nnoremap <F2> "7yiw:%s/\<<C-R>7\>/<C-R>7/g<left><left>

nnoremap <c-b> :bprev<CR>
nnoremap <c-n> :bnext<CR>

nnoremap j gj
nnoremap k gk
nnoremap gj j
nnoremap gk k

cnoremap <C-s> <Plug>ZshPathComplete

vnoremap < <gv
vnoremap > >gv

vnoremap <Leader>p :diffput<CR>

nnoremap <silent> <Leader>c /<<<<<<<\\|=======\\|>>>>>>><CR>
nnoremap <silent> <Leader>w :set wrap!<CR>
nnoremap <silent> <Leader>t :tabe<CR>
nnoremap <silent> <Leader>T :tabe %<CR>
nnoremap <silent> <Leader>s :Gstatus<CR>
nnoremap <silent> <Leader>S :tabe .git/index<CR>
nnoremap <silent> <Leader>D :Gdiff<CR>


nnoremap zs v%zf
nnoremap zS $v%zf

" Open issue:
nnoremap <silent> gi "8yiw:!open https://immo.atlassian.net/browse/IMMO-<C-R>8<CR><CR>
nnoremap <silent> gI "8yiw:!open https://github.com/immocapital/immo-platform/issues/<C-R>8<CR><CR>
" nnoremap <silent> gm "8yiw:!open "https://github.com/immocapital/immo-platform/issues?q=is\%3Aissue+is\%3Aopen+assignee\%3Anino+milestone\%3A<C-R>8"<CR><CR>

nnoremap <silent> gu "8yiW:!open "<C-R>8"<CR><CR>
nnoremap <silent> gs "8yiw:!open "https://sourcegraph.com/search?q=<C-R>8&pattern=literal"<CR><CR>
vnoremap <silent> gs "8y:!open "https://sourcegraph.com/search?q=<C-R>8&pattern=literal"<CR><CR>

" Terminal navigation:
" tnoremap <C-H> <C-\><C-N><C-W><C-H>
" tnoremap <C-J> <C-\><C-N><C-W><C-J>
" tnoremap <C-K> <C-\><C-N><C-W><C-K>
" tnoremap <C-L> <C-\><C-N><C-W><C-L>


nnoremap <leader>e 10<C-E>
nnoremap <leader>y yiw

nnoremap ¬ 5zl
nnoremap ˙ 5zh
nnoremap <M-l> 5zl
nnoremap <M-h> 5zh

nnoremap ™ @@

vnoremap <silent> ,a :Tabularize /^[^=]*\zs=<CR>
vnoremap <silent> <C-a> :Tabularize /^[^:]*:\zs/l0l1<CR>

nnoremap <silent> cp :!echo '%' \| ruby -e 'print(STDIN.read.strip)' \| pbcopy<CR><CR>

inoremap jj <ESC>
" command! ADB :ALEDisableBuffer

function! s:setIndentWidth(w)
  exe 'set sw=' . a:w[0]
  exe 'set ts=' . a:w[0]
  exe 'set sts=' . a:w[0]
endfunction
command! -nargs=1 IndentWidth call s:setIndentWidth(<f-args>)

function! s:EnableBoxDrawing()
  inoremap , ┌
  inoremap . ┬
  inoremap p ┐
  inoremap o ├
  inoremap e ┼
  inoremap u ┤
  inoremap q └
  inoremap j ┴
  inoremap k ┘
  inoremap y ─
  inoremap i │

  inoremap < ╔
  inoremap > ╦
  inoremap P ╗
  inoremap O ╠
  inoremap E ╬
  inoremap U ╣
  inoremap Q ╚
  inoremap J ╩
  inoremap K ╝
  inoremap Y ═
  inoremap I ║
endfunction
command! Draw call s:EnableBoxDrawing()

function! s:DisableBoxDrawing()
  iunmap ,
  iunmap .
  iunmap p
  iunmap o
  iunmap e
  iunmap u
  iunmap q
  iunmap j
  iunmap k
  iunmap y
  iunmap i

  iunmap <
  iunmap >
  iunmap P
  iunmap O
  iunmap E
  iunmap U
  iunmap Q
  iunmap J
  iunmap K
  iunmap Y
  iunmap I
endfunction
command! Nodraw call s:DisableBoxDrawing()

command! Gpshu Gpush<CR>

command! VD Gvdiffsplit origin/develop:%|windo se wrap|normal zr
command! T exe 'tabe ' . system('pbpaste')|VD
command! Nums windo set modifiable|%s/\$\d\+/\$xx/g

" vnoremap p "0p

" LSP
" nnoremap <silent> gd    <cmd>lua vim.lsp.buf.declaration()<CR>
" nnoremap <silent> gd    <cmd>lua vim.lsp.buf.definition()<CR>
" nnoremap <silent> K     <cmd>lua vim.lsp.buf.hover()<CR>
" nnoremap <silent> gD    <cmd>lua vim.lsp.buf.implementation()<CR>
" nnoremap <silent> <c-k> <cmd>lua vim.lsp.buf.signature_help()<CR>
" nnoremap <silent> 1gD   <cmd>lua vim.lsp.buf.type_definition()<CR>
" nnoremap <silent> gr    <cmd>lua vim.lsp.buf.references()<CR>


" TYPOS
command! W w
command! Tabe tabe
command! Tabc tabc
" command! AF ALEFix

cabbrev MAP ~/.config/nvim/mappings.vim
cabbrev DAL api/src/data_access_layer
cabbrev DL api/src/domain_layer
cabbrev AL api/src/application_layer
cabbrev EAL api/src/external_access_layer
cabbrev TTA db/transactional/tables
cabbrev TSP db/transactional/stored_procedures
cabbrev DEAL data/immo_etl/src/immo_etl/external_access_layer
cabbrev DDAL data/immo_etl/src/immo_etl/data_ingestion/data_access_layer/oltp
cabbrev WH web/hub
cabbrev WHC web/hub/components

cabbrev WSD web/seller/deu/app
cabbrev WSDC web/seller/deu/app/components
cabbrev WSDW web/seller/deu/app/components/widgets
cabbrev WINT web/intranet
cabbrev CW web/core/addon/components/widgets
cabbrev CT web/core/addon/templates/components/widgets



" iabbrev @wc @immo/web-core
" iabbrev @ic @immo/core
" iabbrev @e @ember

iabbrev constanst constants

function! s:ToggleHere()
	let cursorcolumn = getcurpos()[2]
	if &colorcolumn == cursorcolumn
		let &colorcolumn = ''
	else
		let &colorcolumn = cursorcolumn
	endif
endfunction
command! Here call s:ToggleHere()
nnoremap Q :Here<CR>

command! -nargs=+ TA tabe|Ack <f-args>

command! WTF %s/\d\zs Jan \ze\d/-01-/|%s/\d\zs Feb \ze\d/-02-/|%s/\d\zs Mar \ze\d/-03-/|%s/\d\zs Apr \ze\d/-04-/|%s/\d\zs May \ze\d/-05-/|%s/\d\zs Jun \ze\d/-06-/|%s/\d\zs Jul \ze\d/-07-/|%s/\d\zs Aug \ze\d/-08-/|%s/\d\zs Sep \ze\d/-09-/|%s/\d\zs Oct \ze\d/-10-/|%s/\d\zs Nov \ze\d/-11-/|%s/\d\zs Dec \ze\d/-12-/

command! Nofile set buftype=nofile


