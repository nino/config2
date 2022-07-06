local utils = require("utils")

-- Colors
local use_light_bg = false
vim.opt.termguicolors = true
if use_light_bg then
    utils.color("thinglight")
else
    utils.color("thing")
end

-- Defaults
vim.opt.laststatus = 2
vim.opt.lazyredraw = true
vim.opt.autoread = true
vim.opt.diffopt = vim.opt.diffopt + "iwhite"
-- vim.opt.signcolumn = "yes"
vim.opt.list = true
vim.opt.listchars = "tab:→ ,nbsp:␣,trail:⌁,extends:→,precedes:←"

vim.opt.rulerformat = '♥︎ %l/%L %P %c'

-- Providers
-- TODO Make this depend on the computer because this is problably breaking the
-- Linux
vim.cmd[[
let g:python3_host_prog = '/Users/nino/.pyenv/shims/python'
let g:python_host_prog = '/Users/nino/.pyenv/shims/python'
]]

-- Mappings
vim.g.mapleader = " "
vim.cmd[[
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

-- Variables
vim.env.FZF_DEFAULT_COMMAND = "fd --type f"

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
        client.resolved_capabilities.document_formatting = false
    end
}
require('lspconfig').ember.setup {}
require('lspconfig').tailwindcss.setup {}
require('lspconfig').sumneko_lua.setup {
    settings = {
        Lua = {
            diagnostics = {
                globals = {"vim", "use"},
                disable = {"lowercase-global"}
            }
        }
    }
}
require('lspconfig').julials.setup {}
require('lspconfig').pylsp.setup {}
require('lspconfig').solargraph.setup {}
require('lspconfig').rls.setup {
    on_attach = function(client)
        client.resolved_capabilities.document_formatting = false
    end
}
-- require('lspconfig').clangd.setup {}
require('lspconfig').gopls.setup {}

-- local function on_attach(client) print('Attached to ' .. client.name) end

local dlsconfig = require 'diagnosticls-configs'

dlsconfig.init {}

local eslint = require "diagnosticls-configs.linters.eslint"
local eslint_fmt = require 'diagnosticls-configs.formatters.eslint_fmt'
local lua_format = require "diagnosticls-configs.formatters.lua_format"
local rustfmt = require "rust_fmt"
dlsconfig.setup {
    ['javascript'] = {linter = eslint, formatter = eslint_fmt},
    ['javascriptreact'] = {linter = eslint, formatter = {eslint_fmt}},
    ['typescript'] = {linter = eslint, formatter = eslint_fmt},
    ['typescriptreact'] = {linter = eslint, formatter = {eslint_fmt}},
    ['lua'] = {formatter = {lua_format}},
    ['rust'] = {formatter = {rustfmt}}
}

function format_file()
    -- Looks like this works without that weird hack now \o/
    -- if vim.o.filetype == "typescriptreact" or vim.o.filetype == "javascriptreact" then
    --     vim.lsp.buf.formatting_sync(nil, 8000)
    --     vim.cmd('e!')
    -- else
    vim.lsp.buf.formatting()
    -- end
end

-- LSP Mappings
vim.cmd([[
  nnoremap <silent> K :lua vim.lsp.buf.hover()<CR>
  nnoremap <silent> gd :lua vim.lsp.buf.definition()<CR>
  nnoremap <silent> _ :lua format_file()<CR>
  nnoremap <silent> ,n :lua vim.diagnostic.goto_next()<CR>
  nnoremap <silent> <leader>a :lua vim.diagnostic.open_float()<CR>
  nnoremap - F r_
  nnoremap <Leader>e :e!<CR>
]])

vim.cmd("command! -nargs=1 Rename lua vim.lsp.buf.rename(<f-args>)")

vim.cmd("nnoremap <silent> <ESC> <ESC>:nohlsearch<CR>")

-- Set up bleep bloop

-- audio = require "libaudio"
-- audio.initialize({
--     "sounds/alarm01.mp3",
--     "sounds/alarm02.mp3",
--     "sounds/alarm03.mp3",
--     "sounds/alert01.mp3",
--     -- "sounds/alert02.mp3",
--     -- "sounds/alert03.mp3",
--     -- "sounds/alert04.mp3",
--     -- "sounds/alert05.mp3",
--     -- "sounds/alert06.mp3",
--     -- "sounds/alert07.mp3",
--     -- "sounds/alert08.mp3",
--     -- "sounds/alert09.mp3",
--     -- "sounds/alert10.mp3",
--     -- "sounds/alert12.mp3",
--     -- "sounds/alert13.mp3",
--     -- "sounds/alert14.mp3",
--     -- "sounds/alert15.mp3",
--     -- "sounds/alert16.mp3",
--     -- "sounds/alert17.mp3",
--     -- "sounds/alert18.mp3",
--     -- "sounds/alert19.mp3",
--     -- "sounds/alert20.mp3",
--     -- "sounds/alert21.mp3",
--     -- "sounds/alert22.mp3",
--     -- "sounds/alert23.mp3",
--     -- "sounds/alert24.mp3",
--     -- "sounds/communications_end_transmission.mp3",
--     -- "sounds/communications_start_transmission.mp3",
--     -- "sounds/computer_error.mp3",
--     -- "sounds/computer_work_beep.mp3",
--     -- "sounds/computerbeep_1.mp3",
--     -- "sounds/computerbeep_2.mp3",
--     -- "sounds/computerbeep_3.mp3",
--     -- "sounds/computerbeep_4.mp3",
--     -- "sounds/computerbeep_5.mp3",
--     -- "sounds/computerbeep_6.mp3",
--     -- "sounds/computerbeep_7.mp3",
--     -- "sounds/computerbeep_8.mp3",
--     -- "sounds/computerbeep_9.mp3",
--     -- "sounds/computerbeep_10.mp3",
--     -- "sounds/computerbeep_11.mp3",
--     -- "sounds/computerbeep_12.mp3",
--     -- "sounds/computerbeep_13.mp3",
--     -- "sounds/computerbeep_14.mp3",
--     -- "sounds/computerbeep_15.mp3",
--     -- "sounds/computerbeep_16.mp3",
--     -- "sounds/computerbeep_17.mp3",
--     -- "sounds/computerbeep_18.mp3",
--     -- "sounds/computerbeep_19.mp3",
--     -- "sounds/computerbeep_20.mp3",
--     -- "sounds/computerbeep_21.mp3",
--     -- "sounds/computerbeep_22.mp3",
--     -- "sounds/computerbeep_23.mp3",
--     -- "sounds/computerbeep_24.mp3",
--     -- "sounds/computerbeep_25.mp3",
--     -- "sounds/computerbeep_26.mp3",
--     -- "sounds/computerbeep_27.mp3",
--     -- "sounds/computerbeep_28.mp3",
--     -- "sounds/computerbeep_29.mp3",
--     -- "sounds/computerbeep_30.mp3",
--     -- "sounds/computerbeep_31.mp3",
--     -- "sounds/computerbeep_32.mp3",
--     -- "sounds/computerbeep_33.mp3",
--     -- "sounds/computerbeep_34.mp3",
--     -- "sounds/computerbeep_35.mp3",
--     -- "sounds/computerbeep_36.mp3",
--     -- "sounds/computerbeep_37.mp3",
--     -- "sounds/computerbeep_38.mp3",
--     -- "sounds/computerbeep_39.mp3",
--     -- "sounds/computerbeep_40.mp3",
--     -- "sounds/computerbeep_41.mp3",
--     -- "sounds/computerbeep_42.mp3",
--     -- "sounds/computerbeep_43.mp3",
--     -- "sounds/computerbeep_44.mp3",
--     -- "sounds/computerbeep_45.mp3",
--     -- "sounds/computerbeep_46.mp3",
--     -- "sounds/computerbeep_47.mp3",
--     -- "sounds/computerbeep_48.mp3",
--     -- "sounds/computerbeep_49.mp3",
--     -- "sounds/computerbeep_50.mp3",
--     -- "sounds/computerbeep_51.mp3",
--     -- "sounds/computerbeep_52.mp3",
--     -- "sounds/computerbeep_53.mp3",
--     -- "sounds/computerbeep_54.mp3",
--     -- "sounds/computerbeep_55.mp3",
--     -- "sounds/computerbeep_56.mp3",
--     -- "sounds/computerbeep_57.mp3",
--     -- "sounds/computerbeep_58.mp3",
--     -- "sounds/computerbeep_59.mp3",
--     -- "sounds/computerbeep_60.mp3",
--     -- "sounds/computerbeep_61.mp3",
--     -- "sounds/computerbeep_62.mp3",
--     -- "sounds/computerbeep_63.mp3",
--     -- "sounds/computerbeep_64.mp3",
--     -- "sounds/computerbeep_65.mp3",
--     -- "sounds/computerbeep_66.mp3",
--     -- "sounds/computerbeep_67.mp3",
--     -- "sounds/computerbeep_68.mp3",
--     -- "sounds/computerbeep_69.mp3",
--     -- "sounds/computerbeep_70.mp3",
--     -- "sounds/computerbeep_71.mp3",
--     -- "sounds/computerbeep_72.mp3",
--     -- "sounds/computerbeep_73.mp3",
--     -- "sounds/computerbeep_74.mp3",
--     -- "sounds/computerbeep_75.mp3",
--     -- "sounds/computerbeep_76.mp3",
--     -- "sounds/computerbeep_77.mp3",
--     -- "sounds/consolewarning.mp3",
--     -- "sounds/critical.mp3",
--     -- "sounds/damagealarm.mp3",
--     -- "sounds/denybeep1.mp3",
--     -- "sounds/denybeep2.mp3",
--     -- "sounds/denybeep3.mp3",
--     -- "sounds/denybeep4.mp3",
--     -- "sounds/deskviewer1.mp3",
--     -- "sounds/deskviewer2.mp3",
--     -- "sounds/deskviewerbeep.mp3",
--     -- "sounds/ds9intercom.mp3",
--     -- "sounds/energize.mp3",
--     -- "sounds/engage.mp3",
--     -- "sounds/hail_allship_ep.mp3",
--     -- "sounds/hailalert_1.mp3",
--     -- "sounds/hailalert_2.mp3",
--     -- "sounds/hailbeep_5.mp3",
--     -- "sounds/hailbeep_clean.mp3",
--     -- "sounds/hailbeep2_clean.mp3",
--     -- "sounds/hailbeep3_clean.mp3",
--     -- "sounds/hailbeep4_clean.mp3",
--     -- "sounds/hailingfrequencies_open1.mp3",
--     -- "sounds/hailingfrequencies_open2.mp3",
--     -- "sounds/hailingfrequencies_open3.mp3",
--     -- "sounds/hailingfrequencies_open4.mp3",
--     -- "sounds/helm_engage_clean.mp3",
--     -- "sounds/incoming_hail1.mp3",
--     -- "sounds/incoming_hail2.mp3",
--     -- "sounds/incoming_hail3.mp3",
--     -- "sounds/input_failed_clean.mp3",
--     -- "sounds/input_failed2_clean.mp3",
--     -- "sounds/input_ok_1_clean.mp3",
--     -- "sounds/input_ok_2_clean.mp3",
--     -- "sounds/input_ok_3_clean.mp3",
--     -- "sounds/input_ok_4.mp3",
--     -- "sounds/keyok1.mp3",
--     -- "sounds/keyok2.mp3",
--     -- "sounds/keyok3.mp3",
--     -- "sounds/keyok4.mp3",
--     -- "sounds/keyok5.mp3",
--     -- "sounds/keyok6.mp3",
--     -- "sounds/processing.mp3",
--     -- "sounds/processing2.mp3",
--     -- "sounds/processing3.mp3",
--     -- "sounds/scrscroll1.mp3",
--     -- "sounds/scrscroll2.mp3",
--     -- "sounds/scrscroll3.mp3",
--     -- "sounds/scrsearch.mp3",
--     -- "sounds/scrshow.mp3",
--     -- "sounds/transporter_beep.mp3",
--     -- "sounds/voy_hail.mp3",
-- })

if audio ~= nil then
    vim.cmd("augroup sounds\n" .. "autocmd!\n" ..
                "autocmd BufWritePre * lua audio.play(2)" .. "augroup END")
end

-- Tree Sitter
require'nvim-treesitter.configs'.setup {
    -- One of "all", "maintained" (parsers with maintainers), or a list of languages
    ensure_installed = "all",

    -- Install languages synchronously (only applied to `ensure_installed`)
    sync_install = false,

    -- List of parsers to ignore installing
    -- ignore_install = { "javascript" },

    highlight = {
        -- `false` will disable the whole extension
        enable = true,

        -- NOTE: these are the names of the parsers and not the filetype. (for example if you want to disable highlighting for the `tex` filetype, you need to include `latex` in this list as this is the name of the parser)
        -- list of language that will be disabled
        disable = {"c", "rust"},

        -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
        -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
        -- Using this option may slow down your editor, and you may see some duplicate highlights.
        -- Instead of true it can also be a list of languages
        additional_vim_regex_highlighting = false
    }
}

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
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav',
        '/Users/nino/code/lua-audio/assets/hihat2.wav'
        --    '/Users/nino/.config/secret-config2/sounds/alarm01.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alarm02.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alarm03.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert01.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert02.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert03.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert04.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert05.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert06.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert07.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert08.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert09.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert10.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert12.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert13.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert14.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert15.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert16.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert17.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert18.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert19.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert20.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert21.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert22.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert23.wav',
        --    '/Users/nino/.config/secret-config2/sounds/alert24.wav',
        --    '/Users/nino/.config/secret-config2/sounds/communications_end_transmission.wav',
        --    '/Users/nino/.config/secret-config2/sounds/communications_start_transmission.wav'
        --    '/Users/nino/.config/secret-config2/sounds/computer_error.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computer_work_beep.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_1.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_10.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_11.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_12.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_13.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_14.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_15.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_16.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_17.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_18.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_19.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_20.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_21.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_22.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_23.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_24.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_25.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_26.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_27.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_28.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_29.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_3.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_30.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_31.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_32.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_33.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_34.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_35.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_36.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_37.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_38.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_39.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_4.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_40.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_41.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_42.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_43.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_44.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_45.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_46.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_47.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_48.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_49.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_5.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_50.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_51.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_52.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_53.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_54.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_55.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_56.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_57.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_58.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_59.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_6.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_60.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_61.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_62.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_63.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_64.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_65.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_66.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_67.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_68.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_69.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_7.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_70.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_71.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_72.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_73.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_74.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_75.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_76.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_77.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_8.wav',
        --    '/Users/nino/.config/secret-config2/sounds/computerbeep_9.wav',
        --    '/Users/nino/.config/secret-config2/sounds/consolewarning.wav',
        --    '/Users/nino/.config/secret-config2/sounds/critical.wav',
        --    '/Users/nino/.config/secret-config2/sounds/damagealarm.wav',
        --    '/Users/nino/.config/secret-config2/sounds/denybeep1.wav',
        --    '/Users/nino/.config/secret-config2/sounds/denybeep2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/denybeep3.wav',
        --    '/Users/nino/.config/secret-config2/sounds/denybeep4.wav',
        --    '/Users/nino/.config/secret-config2/sounds/deskviewer1.wav',
        --    '/Users/nino/.config/secret-config2/sounds/deskviewer2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/deskviewerbeep.wav',
        --    '/Users/nino/.config/secret-config2/sounds/ds9intercom.wav',
        --    '/Users/nino/.config/secret-config2/sounds/energize.wav',
        --    '/Users/nino/.config/secret-config2/sounds/engage.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hail_allship_ep.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailalert_1.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailalert_2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailbeep2_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailbeep3_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailbeep4_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailbeep_5.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailbeep_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailingfrequencies_open1.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailingfrequencies_open2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailingfrequencies_open3.wav',
        --    '/Users/nino/.config/secret-config2/sounds/hailingfrequencies_open4.wav',
        --    '/Users/nino/.config/secret-config2/sounds/helm_engage_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/incoming_hail1.wav',
        --    '/Users/nino/.config/secret-config2/sounds/incoming_hail2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/incoming_hail3.wav',
        --    '/Users/nino/.config/secret-config2/sounds/input_failed2_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/input_failed_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/input_ok_1_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/input_ok_2_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/input_ok_3_clean.wav',
        --    '/Users/nino/.config/secret-config2/sounds/input_ok_4.wav',
        --    '/Users/nino/.config/secret-config2/sounds/keyok1.wav',
        --    '/Users/nino/.config/secret-config2/sounds/keyok2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/keyok3.wav',
        --    '/Users/nino/.config/secret-config2/sounds/keyok4.wav',
        --    '/Users/nino/.config/secret-config2/sounds/keyok5.wav',
        --    '/Users/nino/.config/secret-config2/sounds/keyok6.wav',
        --    '/Users/nino/.config/secret-config2/sounds/processing.wav',
        --    '/Users/nino/.config/secret-config2/sounds/processing2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/processing3.wav',
        --    '/Users/nino/.config/secret-config2/sounds/scrscroll1.wav',
        --    '/Users/nino/.config/secret-config2/sounds/scrscroll2.wav',
        --    '/Users/nino/.config/secret-config2/sounds/scrscroll3.wav',
        --    '/Users/nino/.config/secret-config2/sounds/scrsearch.wav',
        --    '/Users/nino/.config/secret-config2/sounds/scrshow.wav',
        --    '/Users/nino/.config/secret-config2/sounds/transporter_beep.wav',
        --    '/Users/nino/.config/secret-config2/sounds/voy_hail.wav'
    })
end
-- loadaudio()

function play(idx)
    local c_index = ffi.new("int", idx - 1)
    libaudio.lj_play(c_index)
end

if libaudio ~= nil then
    --          vim.cmd [[
    --          autocmd! InsertEnter * :lua play(1)
    --          autocmd! InsertLeave * :lua play(2)
    --        ]]
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
