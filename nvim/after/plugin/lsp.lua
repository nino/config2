vim.diagnostic.config { virtual_text = false }

-- LSP-zero
local nonels = require("null-ls")
local lsp = require('lsp-zero')
local lspconfig = require('lspconfig')
lsp.preset("recommended")
lsp.ensure_installed({
  'tsserver',
  'rust_analyzer',
  'lua_ls',
  'tailwindcss',
  'gopls',
  'pyright',
  'diagnosticls',
  'terraformls',
})

nonels.setup({
  sources = {
    nonels.builtins.diagnostics.eslint,
    nonels.builtins.formatting.eslint,
    nonels.builtins.formatting.black,
    nonels.builtins.diagnostics.flake8,
  }
})

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

lsp.configure("pyright", {
  on_attach = function(client, bufnr)
    client.resolved_capabilities.document_formatting = false
  end
})
lsp.skip_server_setup({ 'pylsp' })
lsp.skip_server_setup({ 'eslint' })


lsp.configure('kotlin_language_server', {})

lsp.configure('dartls', {})

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
        globals = { "vim", "use" },
        disable = { "lowercase-global" }
      }
    }
  }
})

lsp.skip_server_setup({ 'sourcekit' })

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
