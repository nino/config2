set shiftwidth=4
set softtabstop=4
set noexpandtab
set wrap

setlocal breakindentopt=shift:2

if stridx(expand('%'), 'nino/immo-platform') != -1
  setlocal textwidth=120
endif
