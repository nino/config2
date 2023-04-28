local utils = require("utils")

-- Colors
local use_light_bg = false
vim.opt.termguicolors = false
if use_light_bg then
  vim.o.background = "light"
  -- utils.color("lucius")
  utils.color("zellner")
else
  vim.o.background = "dark"

  -- utils.color("thing")
  -- utils.color("deus")
  -- utils.color("desert")

  require("gruvbox").setup({
    undercurl = false,
    underline = false,
    bold = true,
    italic = {},
    strikethrough = true,
    invert_selection = false,
    invert_signs = false,
    invert_tabline = false,
    invert_intend_guides = false,
    inverse = true,    -- invert background for search, diffs, statuslines and errors
    contrast = "hard", -- can be "hard", "soft" or empty string
    palette_overrides = {},
    overrides = {},
    dim_inactive = false,
    transparent_mode = false,
  })
  utils.color("gruvbox")

  utils.colorize("DiagnosticError", { fg = utils.rgb(4, 3, 1) })
end

-- Defaults
vim.opt.laststatus = 2
vim.opt.ch = 1 -- command-height
vim.opt.lazyredraw = true
vim.opt.autoread = true
vim.opt.diffopt = vim.opt.diffopt + "iwhite"
vim.opt.signcolumn = "number" -- no extra column
vim.opt.list = true
vim.opt.number = true
vim.opt.numberwidth = 1
vim.opt.listchars = "tab:→ ,nbsp:␣,trail:⌁,extends:→,precedes:←"
vim.opt.conceallevel = 0
vim.opt.scrolloff = 2

vim.opt.smartindent = true
vim.opt.autoindent = true
vim.opt.cindent = true
vim.opt.copyindent = true

vim.opt.rulerformat = '♥︎ %l/%L %P %c'

vim.g["NERDTreeIgnore"] = { '\\.cm.$', '\\.a$', '\\.cm..$' }
vim.g["coqtail_imap_prefix"] = "…"
vim.g["coqtail_map_prefix"] = "…"
vim.g["coqtail_coq_prog"] = "docker run -it coqorg/coq coqidetop.opt"

-- Disable Python 2
-- vim.g["loaded_python_provider"] = 0

-- Providers
if vim.fn.has("macunix") == 1 then
  -- vim.g["python3_host_prog"] = '/Users/nino/.pyenv/shims/python'
  -- vim.g["python_host_prog"] = '/Users/nino/.pyenv/shims/python'
else
  -- vim.g["python3_host_prog"] = '/home/nino/.pyenv/shims/python'
end

-- Mappings
vim.g.mapleader = " "
vim.cmd [[
inoremap <C-l> =>
nnoremap gy mzggyG`z

" tmp
nnoremap ß :Gw<CR>

imap <silent><script><expr> <C-J> copilot#Accept("\<CR>")
]]


-- Digraphs
vim.cmd [[
exe ":digraph SS " .. 0x1E9E
]]

-- Commands
vim.cmd("command! Q :mksession! ~/Prevsession.vim | qa")
vim.cmd("command! CountBufs :echo len(getbufinfo({'buflisted':1}))")
vim.cmd("command! Sy :syntax sync fromstart")
vim.cmd(
  "command! DiffApi :vert diffsplit ~/tech_recruitment_challenge/tests/frontend_engineer/api.js")
vim.cmd(
  "command! Syncheck echo map(synstack(line('.'), col('.')), 'synIDattr(v:val, \"name\")')")

vim.cmd("command! UT UndotreeToggle")
vim.cmd("command! UF UndotreeToggle")
vim.cmd("command! NF NERDTreeFind")
vim.cmd("command! NT NERDTreeToggle")
vim.cmd("command! NN NERDTreeFocus")


-- Resolve conflicts
vim.cmd("command! A normal ddnVnd")
vim.cmd("command! B normal Vndndd")

-- Git
vim.cmd("command! Gc G commit")
vim.cmd("command! Gp G push -p")
vim.cmd("command! Com G commit -a")

-- Variables
vim.env.FZF_DEFAULT_COMMAND =
"fd --type f --hidden --exclude .git --exclude '*.cmi' --exclude '*.cma' --exclude '*.cmxa' --exclude '*.cmxs' --exclude '*.cmt' --exclude '*.cmti' --exclude '*.a' --exclude '*.cmx'"

-- LSP
local on_attach = function(_, _)
  vim.lsp.handlers["textDocument/publishDiagnostics"] =
      vim.lsp.with(vim.lsp.diagnostic.on_publish_diagnostics, {
        -- disable virtual text
        virtual_text = false,
        -- show signs
        signs = true,
        -- delay update diagnostics
        update_in_insert = false
      })
end

require('lspconfig').tsserver.setup {
  on_attach = function(client, bufnr)
    on_attach(client, bufnr)
    client.server_capabilities.document_formatting = false
  end
}

require('lspconfig').ocamllsp.setup {
  on_attach = function(client, bufnr) on_attach(client, bufnr) end
}
require('lspconfig').tailwindcss.setup {}
require('lspconfig').lua_ls.setup {
  on_attach = function(client, bufnr)
    on_attach(client, bufnr)
    -- client.server_capabilities.document_formatting = false
  end,
  settings = {
    Lua = {
      diagnostics = {
        globals = { "vim", "use" },
        disable = { "lowercase-global" }
      }
    }
  }
}
require('lspconfig').rescriptls.setup {
  cmd = {
    'node', '/Users/nino/code-friends/vim-rescript/server/out/server.js',
    '--stdio'
  },
  on_attach = function(client, bufnr) on_attach(client, bufnr) end
}
require('lspconfig').julials.setup {}
require('lspconfig').pylsp.setup {
  on_attach = function(client, bufnr) on_attach(client, bufnr) end
}
require('lspconfig').pyright.setup {
  on_attach = function(client, bufnr) on_attach(client, bufnr) end
}

function coq_lsp()
  return {
    name = 'coq-lsp',
    cmd = { "coq-lsp" },
    filetypes = "coq",
    root_dir = vim.fs.dirname(vim.fs.find({ '_CoqProject' }, { upward = true })[1]),
    single_file_support = true,
  }
end

-- vim.cmd [[
--   augroup coq
--     autocmd! BufRead *.v lua vim.lsp.start(coq_lsp())
--   augroup END
-- ]]

-- Ruby
require('lspconfig').solargraph.setup {
  on_attach = function(client)
    client.server_capabilities.document_formatting = false
  end
}

-- Rust
require('lspconfig').rust_analyzer.setup {
  cmd = { "rustup", "run", "stable", "rust-analyzer" }
}

-- require('lspconfig').clangd.setup {}
require('lspconfig').gopls.setup {}

-- local function on_attach(client) print('Attached to ' .. client.name) end

local dlsconfig = require 'diagnosticls-configs'

dlsconfig.init {}


local eslint = require "diagnosticls-configs.linters.eslint_d"
local eslint_fmt = require 'diagnosticls-configs.formatters.eslint_d_fmt'
dlsconfig.setup {
  ['javascript'] = { linter = eslint },
  ['javascriptreact'] = { linter = eslint },
  ['typescript'] = { linter = eslint },
  ['typescriptreact'] = { linter = eslint, formatter = eslint_fmt },
}

function format_file()
  vim.lsp.buf.format() -- { async = false, timeout_ms=12000 }
end

-- LSP Mappings
vim.cmd([[
  nnoremap <silent> K :lua vim.lsp.buf.hover()<CR>
  nnoremap <silent> gd :lua vim.lsp.buf.definition()<CR>
  nnoremap <silent> _ :lua format_file()<CR>
  nnoremap <silent> <leader>- :!yarn exec eslint --fix %<CR>
  nnoremap <silent> ,n :lua vim.diagnostic.goto_next()<CR>
  nnoremap <silent> <c-n> :lua vim.diagnostic.goto_next()<CR>
  nnoremap <silent> ,a :lua vim.lsp.buf.code_action()<CR>
  nnoremap <silent> <leader>a :lua vim.diagnostic.open_float()<CR>
  nnoremap - F r_
  nnoremap <Leader>e :e!<CR>
]])

vim.cmd("command! -nargs=1 Rename lua vim.lsp.buf.rename(<f-args>)")

vim.cmd("nnoremap <silent> <ESC> <ESC>:nohlsearch<CR>")

-- Tree Sitter
local use_tree_sitter = true
if vim.fn.has('macunix') and use_tree_sitter then
  require 'nvim-treesitter.configs'.setup {
    ensure_installed = {
      "javascript", "typescript", "ruby", "ocaml", "bash", "json",
      "julia", "make", "ninja", "ocaml_interface", "yaml", "toml", "rust",
      "tsx", "latex", "bibtex", "sql", "lua", "html", "css", "vim"
    },

    -- Install languages synchronously (only applied to `ensure_installed`)
    sync_install = false,

    -- List of parsers to ignore installing
    -- ignore_install = { "javascript" },

    highlight = {
      -- `false` will disable the whole extension
      enable = true,
      -- NOTE: these are the names of the parsers and not the filetype. (for example if you want to disable highlighting for the `tex` filetype, you need to include `latex` in this list as this is the name of the parser)
      -- list of language that will be disabled
      disable = {},
      -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
      -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
      -- Using this option may slow down your editor, and you may see some duplicate highlights.
      -- Instead of true it can also be a list of languages
      additional_vim_regex_highlighting = false
    }
  }
end

function loadaudio()
  ffi = require "ffi"
  ffi.cdef [[
      int lj_play(int idx);
      int lj_initialize(const char** sample_paths, size_t num_samples);
    ]]
  libaudio = ffi.load("/Users/nino/.config/dylibs/libaudio.so")

  function initialize(samples)
    local c_samples = ffi.new("const char*[" .. tostring(#samples) .. "]",
      samples)
    libaudio.lj_initialize(c_samples, #samples)
  end

  initialize({
    '/Users/nino/code/lua-audio/assets/hihat.wav',
    '/Users/nino/code/lua-audio/assets/hihat2.wav'
  })
end

-- loadaudio()

function play(idx)
  local c_index = ffi.new("int", idx - 1)
  libaudio.lj_play(c_index)
end

function read_file(filepath)
  local file = io.open(filepath, "r")
  if file == nil then
    print("File is nil")
    return nil
  end
  local content = file:read("*a")
  file:close()
  return content
end

function set_build_cmd(cmd)
  local file, err = io.open("/Users/nino/build_cmd", "w")
  if file == nil then
    print("Unable to read file: " .. err)
    return
  end
  file:write(cmd)
  file:close()
end

function send_keys()
  local current_build_command = read_file("/Users/nino/build_cmd")
  if current_build_command ~= nil then
    os.execute("tmux send-keys -t :1 '" .. current_build_command .. "' C-m")
  end
end

-- vim.cmd([[
-- nnoremap <Leader>r :lua send_keys()<cr>
-- ]])

require "mappings"


vim.cmd([[
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

" Visual @
xnoremap @ :<C-u>call ExecuteMacroOverVisualRange()<CR>

function! ExecuteMacroOverVisualRange()
  echo "@".getcmdline()
  execute ":'<,'>normal @".nr2char(getchar())
endfunction
]])
