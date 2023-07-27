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
    'ocamllsp',
    'gopls',
    'eslint',
    'clangd'
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
    flavour = "mocha", -- latte, frappe, macchiato, mocha
    background = {
        -- :h background
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
    no_italic = true, -- Force no italic
    no_bold = false,  -- Force no bold
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
    custom_highlights = {},
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

vim.cmd.colorscheme('gruvbox')

-- Autocommands
vim.cmd [[
  augroup BQNFileType
    autocmd!
    autocmd BufRead,BufNewFile *.bqn set filetype=bqn
  augroup END
]]
