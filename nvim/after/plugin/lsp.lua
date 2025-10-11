vim.diagnostic.config({ virtual_text = false, jump = { float = true } })

vim.diagnostic.config({
  signs = {
    text = {
      [vim.diagnostic.severity.ERROR] = "❌",
      [vim.diagnostic.severity.WARN] = "⚠️",
      [vim.diagnostic.severity.HINT] = "💡",
    }
  }
})

-- Add toggle function and keymap for diagnostic virtual text
local diagnostic_virtual_text = false
vim.keymap.set("n", "<leader><M-d>", function()
  diagnostic_virtual_text = not diagnostic_virtual_text
  vim.diagnostic.config({ virtual_text = diagnostic_virtual_text })
end)

-- LSP keymaps
vim.api.nvim_create_autocmd('LspAttach', {
  callback = function(args)
    local bufnr = args.buf
    vim.keymap.set('n', 'gd', vim.lsp.buf.definition, { buffer = bufnr })
    vim.keymap.set('n', 'gD', vim.lsp.buf.declaration, { buffer = bufnr })
    vim.keymap.set('n', 'gi', vim.lsp.buf.implementation, { buffer = bufnr })
  end,
})

-- Linting setup
require("lint").linters_by_ft = {
  typescript = { "eslint" },
  typescriptreact = { "eslint" },
  javascript = { "eslint" },
  javascriptreact = { "eslint" },
}
vim.api.nvim_create_autocmd({ "BufWritePost", "InsertLeave", "BufRead" }, {
  callback = function()
    require("lint").try_lint()
  end,
})

-- Formatting setup
local javascript_formatters = { "prettierd" }
require("conform").setup({
  formatters_by_ft = {
    lua = { "stylua" },
    javascript = javascript_formatters,
    javascriptreact = javascript_formatters,
    typescript = javascript_formatters,
    typescriptreact = javascript_formatters,
    swift = { "swiftformat" },
    asm = { "asmfmt" },
  },
})

-- LSP Configuration using new vim.lsp.config API
-- Note: vim.lsp.config() defines the config, vim.lsp.enable() starts the server

vim.lsp.config('zls', {
  cmd = { 'zls' },
  filetypes = { 'zig' },
  root_markers = { 'build.zig', '.git' },
})

vim.lsp.config('tailwindcss', {
  cmd = { 'tailwindcss-language-server', '--stdio' },
  filetypes = { 'html', 'css', 'scss', 'javascript', 'javascriptreact', 'typescript', 'typescriptreact', 'vue', 'svelte' },
  root_markers = { 'tailwind.config.js', 'tailwind.config.ts', 'tailwind.config.cjs' },
})

vim.lsp.config('astro', {
  cmd = { 'astro-ls', '--stdio' },
  filetypes = { 'astro' },
  root_markers = { 'package.json', 'astro.config.mjs', '.git' },
})

vim.lsp.config('rust_analyzer', {
  cmd = { 'rust-analyzer' },
  filetypes = { 'rust' },
  root_markers = { 'Cargo.toml', 'rust-project.json' },
})

vim.lsp.config('cmake', {
  cmd = { 'cmake-language-server' },
  filetypes = { 'cmake' },
  root_markers = { 'CMakeLists.txt', '.git' },
})

vim.lsp.config('pyright', {
  cmd = { 'pyright-langserver', '--stdio' },
  filetypes = { 'python' },
  root_markers = { 'pyproject.toml', 'setup.py', 'setup.cfg', 'requirements.txt', 'Pipfile', '.git' },
  on_attach = function(client, bufnr)
    client.server_capabilities.documentFormattingProvider = false
  end,
})

vim.lsp.config('gopls', {
  cmd = { 'gopls' },
  filetypes = { 'go', 'gomod', 'gowork', 'gotmpl' },
  root_markers = { 'go.work', 'go.mod', '.git' },
})

vim.lsp.config('kotlin_language_server', {
  cmd = { 'kotlin-language-server' },
  filetypes = { 'kotlin' },
  root_markers = { 'settings.gradle', 'settings.gradle.kts', '.git' },
})

vim.lsp.config('dartls', {
  cmd = { 'dart', 'language-server', '--protocol=lsp' },
  filetypes = { 'dart' },
  root_markers = { 'pubspec.yaml', '.git' },
})

vim.lsp.config('solargraph', {
  cmd = { 'solargraph', 'stdio' },
  filetypes = { 'ruby' },
  root_markers = { 'Gemfile', '.git' },
})

vim.lsp.config('clangd', {
  cmd = { 'clangd' },
  filetypes = { 'c', 'cpp', 'objc', 'objcpp', 'cuda', 'proto' },
  root_markers = { '.clangd', '.clang-tidy', '.clang-format', 'compile_commands.json', 'compile_flags.txt', 'configure.ac', '.git' },
  capabilities = {
    offsetEncoding = "utf-8"
  }
})

vim.lsp.config('denols', {
  cmd = { 'deno', 'lsp' },
  filetypes = { 'javascript', 'javascriptreact', 'javascript.jsx', 'typescript', 'typescriptreact', 'typescript.tsx' },
  root_markers = { 'deno.json', 'deno.jsonc' },
})

vim.lsp.config('eslint', {
  cmd = { 'vscode-eslint-language-server', '--stdio' },
  filetypes = { 'javascript', 'javascriptreact', 'javascript.jsx', 'typescript', 'typescriptreact', 'typescript.tsx', 'vue', 'svelte', 'astro' },
  root_markers = { '.eslintrc', '.eslintrc.js', '.eslintrc.cjs', '.eslintrc.yaml', '.eslintrc.yml', '.eslintrc.json', 'eslint.config.js', 'package.json' },
})

vim.lsp.config('ts_ls', {
  cmd = { 'typescript-language-server', '--stdio' },
  filetypes = { 'javascript', 'javascriptreact', 'javascript.jsx', 'typescript', 'typescriptreact', 'typescript.tsx' },
  root_markers = { 'package.json' },
  single_file_support = false,
  -- on_attach = function(client, bufnr)
  --   client.server_capabilities.documentFormattingProvider = true
  -- end,
  settings = {
    typescript = {
      format = {
        indentSize = 2,
        tabSize = 2,
        convertTabsToSpaces = true,
      }
    },
    javascript = {
      format = {
        indentSize = 2,
        tabSize = 2,
        convertTabsToSpaces = true,
      }
    }
  }
})

vim.lsp.config('lua_ls', {
  cmd = { 'lua-language-server' },
  filetypes = { 'lua' },
  root_markers = { '.luarc.json', '.luarc.jsonc', '.luacheckrc', '.stylua.toml', 'stylua.toml', 'selene.toml', 'selene.yml', '.git' },
  settings = {
    Lua = {
      diagnostics = {
        globals = { "vim" },
        unusedLocalVariable = "Warning",
        enable = true,
        undefinedGlobal = "Error",
        ["lowercase-global"] = "Error",
      },
    },
  },
})

-- Enable all configured LSP servers
vim.lsp.enable('zls')
vim.lsp.enable('tailwindcss')
vim.lsp.enable('astro')
vim.lsp.enable('rust_analyzer')
vim.lsp.enable('cmake')
vim.lsp.enable('pyright')
vim.lsp.enable('gopls')
vim.lsp.enable('kotlin_language_server')
vim.lsp.enable('dartls')
vim.lsp.enable('solargraph')
vim.lsp.enable('clangd')
vim.lsp.enable('eslint')
vim.lsp.enable('lua_ls')

-- Conditionally enable ts_ls OR denols based on project type
-- This autocmd runs when opening JS/TS files and determines which server to use
vim.api.nvim_create_autocmd('FileType', {
  pattern = { 'javascript', 'javascriptreact', 'typescript', 'typescriptreact' },
  callback = function(args)
    local bufnr = args.buf
    local root_dir = vim.fs.root(bufnr, { 'package.json', 'deno.json', 'deno.jsonc' })

    if not root_dir then
      return
    end

    -- Check if it's a Deno project
    local is_deno = vim.uv.fs_stat(root_dir .. '/deno.json') or vim.uv.fs_stat(root_dir .. '/deno.jsonc')

    if is_deno then
      vim.lsp.enable('denols', true)
    else
      vim.lsp.enable('ts_ls', true)
    end
  end,
})

-- Completion setup
-- local cmp = require("cmp")
-- local cmp_select = { behavior = cmp.SelectBehavior.Select }

-- cmp.setup({
--   completion = { autocomplete = false },
--   mapping = cmp.mapping.preset.insert({
--     ["<C-p>"] = cmp.mapping.select_prev_item(cmp_select),
--     ["<C-n>"] = cmp.mapping.select_next_item(cmp_select),
--     ["<CR>"] = cmp.mapping.confirm({ select = false }),
--     ["<C-f>"] = cmp.mapping.confirm({ select = true }),
--     ["<C-space>"] = cmp.mapping.complete(),
--   }),
--   sources = {
--     { name = "nvim_lsp" },
--     {
--       name = "buffer",
--       option = {
--         get_bufnrs = function()
--           return vim.api.nvim_list_bufs()
--         end,
--       },
--     },
--   },
-- })
