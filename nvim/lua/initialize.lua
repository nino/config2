local utils = require("utils")

-- Colors
local use_light_bg = false
vim.opt.termguicolors = false
if use_light_bg then
  utils.color("thinglight")
else
  utils.color("thing")
  -- utils.color("plaindark")

  -- vim.o.background = "dark"
  -- require("gruvbox").setup({
  --   undercurl = true,
  --   underline = true,
  --   bold = true,
  --   italic = false,
  --   strikethrough = true,
  --   invert_selection = false,
  --   invert_signs = false,
  --   invert_tabline = false,
  --   invert_intend_guides = false,
  --   inverse = true, -- invert background for search, diffs, statuslines and errors
  --   contrast = "", -- can be "hard", "soft" or empty string
  --   palette_overrides = {},
  --   overrides = {},
  --   dim_inactive = false,
  --   transparent_mode = false,
  -- })

  -- utils.color("gruvbox")
end

-- Defaults
vim.opt.laststatus = 2
vim.opt.ch = 1 -- command-height
vim.opt.lazyredraw = true
vim.opt.autoread = true
vim.opt.diffopt = vim.opt.diffopt + "iwhite"
-- vim.opt.signcolumn = "yes"
vim.opt.list = true
vim.opt.number = true
vim.opt.listchars = "tab:→ ,nbsp:␣,trail:⌁,extends:→,precedes:←"

vim.opt.rulerformat = '♥︎ %l/%L %P %c'

-- Providers
if vim.fn.has("macunix") == 1 then
  vim.cmd [[
let g:python3_host_prog = '/Users/nino/.pyenv/shims/python'
let g:python_host_prog = '/Users/nino/.pyenv/shims/python'
]]
else
  vim.cmd [[
let g:python3_host_prog = '/home/nino/.pyenv/shims/python'
let g:python_host_prog = '/home/nino/.pyenv/shims/python'
]]
end

-- Mappings
vim.g.mapleader = " "
vim.cmd [[
inoremap <C-l> =>
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

-- Variables
vim.env.FZF_DEFAULT_COMMAND = "fd --type f --hidden --exclude .git"

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
require('lspconfig').ember.setup {}
require('lspconfig').tailwindcss.setup {}
require('lspconfig').sumneko_lua.setup {
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
require('lspconfig').solargraph.setup {
  on_attach = function(client)
    client.server_capabilities.document_formatting = false
  end
}
require('lspconfig').rls.setup {
  on_attach = function(client)
    client.server_capabilities.document_formatting = false
  end
}
-- require('lspconfig').clangd.setup {}
require('lspconfig').gopls.setup {}

-- local function on_attach(client) print('Attached to ' .. client.name) end

local dlsconfig = require 'diagnosticls-configs'

dlsconfig.init {}

function make_eslint_fmt()
  local fs = require('diagnosticls-configs.fs')
  return {
    sourceName = 'eslint_fmt_custom',
    command = fs.executable('yarn', fs.Scope.NODE),
    args = {
      'exec',
      'eslint',
      '--fix',
      '%file',
    },
    isStdout = false,
    doesWriteToFile = true,
    rootPatterns = {
      '.eslintrc',
      '.eslintrc.cjs',
      '.eslintrc.js',
      '.eslintrc.json',
      '.eslintrc.yaml',
      '.eslintrc.yml',
    },
  }
end

local eslint_fmt = make_eslint_fmt()

local eslint = require "diagnosticls-configs.linters.eslint"
-- local eslint_fmt = require 'diagnosticls-configs.formatters.eslint_fmt'
local rustfmt = require "rust_fmt"
dlsconfig.setup {
  ['javascript'] = { linter = eslint },
  ['javascriptreact'] = { linter = eslint },
  ['typescript'] = { linter = eslint },
  ['typescriptreact'] = { linter = eslint, formatter = eslint_fmt },
  ['rust'] = { formatter = { rustfmt } }
}

function format_file() vim.lsp.buf.format { async = true } end

-- LSP Mappings
vim.cmd([[
  nnoremap <silent> K :lua vim.lsp.buf.hover()<CR>
  nnoremap <silent> gd :lua vim.lsp.buf.definition()<CR>
  nnoremap <silent> _ :lua format_file()<CR>
  nnoremap <silent> ,n :lua vim.diagnostic.goto_next()<CR>
  nnoremap <silent> ,a :lua vim.lsp.buf.code_action()<CR>
  nnoremap <silent> <leader>a :lua vim.diagnostic.open_float()<CR>
  nnoremap - F r_
  nnoremap <Leader>e :e!<CR>
]])

vim.cmd("command! -nargs=1 Rename lua vim.lsp.buf.rename(<f-args>)")

vim.cmd("nnoremap <silent> <ESC> <ESC>:nohlsearch<CR>")

-- Tree Sitter
if vim.fn.has('macunix') then
  require 'nvim-treesitter.configs'.setup {
    ensure_installed = {
      "javascript", "typescript", "ruby", "ocaml", "lua", "bash", "json",
      "julia", "make", "ninja", "ocaml_interface", "yaml", "toml", "rust",
      "tsx", "latex", "bibtex", "sql"
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
      disable = { "rust" },

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

-- Run stuff in the other pane
current_build_command = 'immo core test --grep typescript'

function send_keys()
  if current_build_command ~= nil then
    os.execute("tmux send-keys -t :.1 '" .. current_build_command .. "' C-m")
  end
end

vim.cmd([[
nnoremap <Leader>r :lua send_keys()<cr>
]])

require "mappings"
