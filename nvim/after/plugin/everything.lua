-- LSP-zero
local lsp = require('lsp-zero')
local lspconfig = require('lspconfig')
lsp.preset("recommended")
lsp.ensure_installed({
    'tsserver',
    'rust_analyzer',
    'lua_ls',
    'tailwindcss',
    'julials',
    'denols',
    'zls',
    -- 'ocamllsp',
    'gopls',
    'eslint',
    'clangd',
    'svelte',
    'gleam',
    'pylsp',
    'erlangls',
    'elixirls',
    'terraformls',
})

-- vim.cmd ":Copilot disable"

lsp.on_attach(function(client, bufnr)
    lsp.default_keymaps({ buffer = bufnr })
    client.config.flags.allow_incremental_sync = true
    vim.lsp.handlers["textDocument/publishDiagnostics"] =
        vim.lsp.with(vim.lsp.diagnostic.on_publish_diagnostics, {
            -- disable virtual text
            virtual_text = false,
            -- show signs
            signs = true,
            -- delay update diagnostics
            update_in_insert = false
        })
end)

lsp.skip_server_setup({ 'pyright' })
lsp.configure('pylsp', {
    settings = {
        pylsp = {
            configurationSources = { 'flake8' },
            plugins = {
                pycodestyle = { enabled = false },
                flake8 = {
                    enabled = true,
                    ignore = {},
                }
            }
        }
    }
})

lsp.configure('sourcekit', {})
lsp.configure('denols', {
    root_dir = lspconfig.util.root_pattern("deno.json", "deno.jsonc"),
})

lsp.configure('tsserver', {
    on_attach = function(client, bufnr)
        client.server_capabilities.document_formatting = false
    end,
    root_dir = lspconfig.util.root_pattern("package.json"),
    single_file_support = false
})
lsp.configure('svelte', {})

lsp.configure('eslint', {
    root_dir = lspconfig.util.root_pattern("package.json"),
    single_file_support = false
})

lsp.configure('julials', {})
lsp.configure('clangd', {})
lsp.configure('lua_ls', {
    settings = {
        Lua = {
            diagnostics = {
                globals = { "vim", "use" },
                disable = { "lowercase-global" }
            }
        }
    }
})

lsp.configure('gleam', {
    -- set custom executable path
    -- cmd = { "/Users/nino/.cargo/bin/gleam", "lsp" },
})

lsp.setup()


local actions = require("telescope.actions")
require "telescope".setup {
    defaults = {
        preview = {
            treesitter = false
        },
        mappings = {
            i = {
                ["<M-Q>"] = actions.send_to_qflist + actions.open_qflist,
            },
            n = {
                ["<M-Q>"] = actions.send_to_qflist + actions.open_qflist,
            }
        }
    }
}

-- LSP-zero-powered auto-completion
local cmp = require('cmp')
local cmp_select = { behavior = cmp.SelectBehavior.Select }
local cmp_mappings = lsp.defaults.cmp_mappings({
    ['<C-p>'] = cmp.mapping.select_prev_item(cmp_select),
    ['<C-n>'] = cmp.mapping.select_next_item(cmp_select),
    ['<C-y>'] = cmp.mapping.confirm({ select = true }),
    ["<C-space>"] = cmp.mapping.complete(),
})

cmp.setup({
    sources = {
        { name = 'nvim_lsp' },
        {
            name = 'buffer',
            option = {
                get_bufnrs = function()
                    return vim.api.nvim_list_bufs()
                end
            }
        },
    },
})

-- Colors
require("catppuccin").setup({
    background = {
        light = "latte",
        dark = "mocha",
    },
    transparent_background = false,
    show_end_of_buffer = false, -- show the '~' characters after the end of buffers
    term_colors = false,
    dim_inactive = {
        enabled = false,
        shade = "dark",
        percentage = 0.15,
    },
    no_italic = false, -- Force no italic
    no_bold = false,   -- Force no bold
    no_underline = true,
    styles = {
        comments = {},
        conditionals = {},
        loops = {},
        functions = {},
        keywords = {},
        strings = {},
        variables = {},
        numbers = {},
        booleans = {},
        properties = {},
        types = {},
        operators = {},
    },
    color_overrides = {},
    custom_highlights = function(colors)
        return {
            DiagnosticUnderlineError = { bg = colors.surface1 },
            DiagnosticUnderlineWarn = { bg = colors.surface0 },
            -- Comment = { fg = colors.flamingo },
            -- TabLineSel = { bg = colors.pink },
            -- CmpBorder = { fg = colors.surface2 },
            -- Pmenu = { bg = colors.none },
        }
    end
})

local colors = require('ayu.colors')
colors.generate()   -- Pass `true` to enable mirage
require('ayu').setup({
    mirage = false, -- Set to `true` to use `mirage` variant instead of `dark` for dark background.
    overrides = function()
        return {
            Comment = { fg = colors.comment },
            NonText = { fg = colors.comment },
            LineNr = { fg = colors.comment },
            SpecialKey = { fg = colors.comment },
        }
    end
})

require("gruvbox").setup({
    undercurl = true,
    underline = true,
    bold = true,
    italic = {
        strings = true,
        comments = true,
        operators = false,
        folds = true,
    },
    strikethrough = true,
    invert_selection = false,
    invert_signs = false,
    invert_tabline = false,
    invert_intend_guides = false,
    inverse = true, -- invert background for search, diffs, statuslines and errors
    contrast = "",  -- can be "hard", "soft" or empty string
    palette_overrides = {},
    overrides = {},
    dim_inactive = false,
    transparent_mode = false,
})

vim.cmd.colorscheme('gruvbox')

vim.cmd [[
nmap <F6> <Plug>ColorstepPrev
nmap <F7> <Plug>ColorstepNext
nmap <S-F7> <Plug>ColorstepReload
]]

-- Autocommands
vim.cmd [[
  augroup BQNFileType
    autocmd!
    autocmd BufRead,BufNewFile *.bqn set filetype=bqn
  augroup END

  augroup direnv
    autocmd!
    autocmd BufRead,BufNewFile .envrc set filetype=bash
  augroup END
]]


vim.cmd([[silent! autocmd! filetypedetect BufRead,BufNewFile *.ex]])
vim.cmd([[autocmd BufRead,BufNewFile *.ex set filetype=elixir]])
