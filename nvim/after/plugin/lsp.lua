vim.diagnostic.config { virtual_text = false }

-- LSP-zero
local lsp = require('lsp-zero')
local lspconfig = require('lspconfig')
lsp.preset("recommended")
lsp.ensure_installed({
  -- 'tsserver',
  'rust_analyzer',
  'lua_ls',
  'tailwindcss',
  -- 'gopls',
  -- 'pyright',
  'diagnosticls',
  'terraformls',
})

require('lint').linters_by_ft = {
  typescript = { 'eslint', },
  typescriptreact = { 'eslint', },
  javascript = { 'eslint', },
  javascriptreact = { 'eslint', },
  -- python = { 'flake8' },
}
vim.api.nvim_create_autocmd({ "BufWritePost", "InsertLeave", "BufRead" }, {
  callback = function()
    require("lint").try_lint()
  end,
})

local javascript_formatters = { "prettierd" }
require("conform").setup({
  formatters_by_ft = {
    lua = { "stylua" },
    -- Conform will run multiple formatters sequentially
    -- python = { "isort", "black" },
    -- Use a sub-list to run only the first available formatter
    javascript = javascript_formatters,
    javascriptreact = javascript_formatters,
    typescript = javascript_formatters,
    typescriptreact = javascript_formatters,
    swift = { "swiftformat" },
    asm = { "asmfmt" },
  },
})

lsp.on_attach(function(client, bufnr)
  lsp.default_keymaps({ buffer = bufnr })
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

lsp.configure('tailwindcss', {})
require('lspconfig').astro.setup({
  -- capabilities = capabilities,
  -- on_attach = on_attach,
  filetypes = { "astro" }
})
lsp.configure('rust_analyzer', {})
lsp.configure('cmake', {})
lsp.configure('asm_lsp', {})

lsp.configure("terraformls", {})
lsp.configure("vale_ls", {})
lsp.configure("gleam", {})
lsp.configure('ruff', {})
lsp.configure("pyright", {
  on_attach = function(client, bufnr)
    client.server_capabilities.documentFormattingProvider = false
  end
})
lsp.skip_server_setup({ 'pylsp' })
lsp.skip_server_setup({ 'eslint' })


lsp.configure('kotlin_language_server', {})

lsp.configure('dartls', {})
lsp.configure('solargraph', {})

lsp.configure('clangd', {
  capabilities = {
    offsetEncoding = "utf-8"
  }
})
lsp.configure('denols', {
  root_dir = lspconfig.util.root_pattern("deno.json", "deno.jsonc"),
})

lsp.configure('ts_ls', {
  on_attach = function(client, bufnr)
    -- client.server_capabilities.documentFormattingProvider = false
  end,
  root_dir = lspconfig.util.root_pattern("package.json"),
  single_file_support = false
})
lsp.configure('svelte', {})

-- lsp.configure('eslint', {
--    root_dir = lspconfig.util.root_pattern("package.json"),
--    single_file_support = false
-- })

-- lsp.configure('diagnosticls', {
--   settings = {
--     linters = {
--       {
--         eslint = {
--           command = "eslint"
--         }
--       }
--     }
--   }
-- })

lsp.configure('julials', {})
lsp.configure('lua_ls', {
  settings = {
    Lua = {
      diagnostics = {
        globals = { "vim" },
        unusedLocalVariable = "Warning",
        enable = true,
        -- Enable the diagnostic for undefined globals
        undefinedGlobal = "Error",
        -- disable = { "lowercase-global" }
        ["lowercase-global"] = "Error",
      }
    }
  }
})

lsp.skip_server_setup('sourcekit')
-- lsp.configure("sourcekit", {})

lsp.setup()

-- LSP-zero-powered auto-completion
local cmp = require('cmp')
local cmp_select = { behavior = cmp.SelectBehavior.Select }
local cmp_mappings = lsp.defaults.cmp_mappings({
  ['<C-p>'] = cmp.mapping.select_prev_item(cmp_select),
  ['<C-n>'] = cmp.mapping.select_next_item(cmp_select),
  ['<CR>'] = cmp.mapping.confirm({ select = false }), -- Accept currently selected item. Set `select` to `false` to only confirm explicitly selected items.
  ['<C-f>'] = cmp.mapping.confirm({ select = true }),
  ["<C-space>"] = cmp.mapping.complete(),
})

cmp.setup({
  completion = { autocomplete = false },
  mapping = cmp_mappings,
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
