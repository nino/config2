-- VS Code provides its own LSP, completion, linting and formatting.
if vim.g.vscode then
  return
end

vim.diagnostic.config({ virtual_text = false, jump = { float = true } })

-- Completion capabilities (blink.cmp) applied to *every* server via the "*"
-- wildcard, instead of repeating `capabilities = ...` on each server config.
vim.lsp.config("*", {
  capabilities = require("blink.cmp").get_lsp_capabilities(),
})

-- Buffer-local LSP keymaps
vim.api.nvim_create_autocmd("LspAttach", {
  callback = function(args)
    local bufnr = args.buf
    vim.keymap.set("n", "gd", vim.lsp.buf.definition, { buffer = bufnr })
    vim.keymap.set("n", "gD", vim.lsp.buf.declaration, { buffer = bufnr })
    vim.keymap.set("n", "gi", vim.lsp.buf.implementation, { buffer = bufnr })
    -- Call hierarchy (VS Code's "Show Call Hierarchy"), rendered in Trouble.
    -- Sits under the same <leader>x prefix as the other Trouble panels.
    vim.keymap.set("n", "<leader>xi", "<cmd>Trouble lsp_incoming_calls toggle<cr>", { buffer = bufnr })
    vim.keymap.set("n", "<leader>xo", "<cmd>Trouble lsp_outgoing_calls toggle<cr>", { buffer = bufnr })
  end,
})

-- Inlay hints are off by default (distracting); toggle them per-buffer here.
vim.keymap.set("n", "<leader>h", function()
  local filter = { bufnr = 0 }
  vim.lsp.inlay_hint.enable(not vim.lsp.inlay_hint.is_enabled(filter), filter)
end, { desc = "Toggle inlay hints" })

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
local javascript_formatters = { "prettier" }
require("conform").setup({
  formatters_by_ft = {
    lua = { "stylua" },
    javascript = javascript_formatters,
    javascriptreact = javascript_formatters,
    typescript = javascript_formatters,
    typescriptreact = javascript_formatters,
    swift = { "swiftformat" },
    asm = { "asmfmt" },
    python = { "ruff" },
  },
  format_on_save = function(bufnr)
    if vim.api.nvim_buf_get_name(bufnr):find("^fugitive://") then
      return
    end
    return {
      timeout_ms = 2000,
      lsp_format = "fallback",
    }
  end,
})

-- LSP servers.
--
-- nvim-lspconfig ships the cmd / filetypes / root_markers for every server in
-- its `lsp/` directory, so we only declare the servers we want (below) and
-- override the handful of settings that differ from those bundled defaults.
-- Each override is deep-merged on top of both the bundled config and the "*"
-- config above, so e.g. clangd still gets the blink capabilities.

vim.lsp.config("clangd", {
  -- clangd warns unless the offset encoding is pinned
  capabilities = { offsetEncoding = "utf-8" },
})

vim.lsp.config("lua_ls", {
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

vim.lsp.config("gopls", {
  settings = {
    gopls = {
      hints = {
        assignVariableTypes = true,
        compositeLiteralFields = true,
        compositeLiteralTypes = true,
        constantValues = true,
        functionTypeParameters = true,
        parameterNames = true,
        rangeVariableTypes = true,
      },
    },
  },
})

-- Inlay-hint settings shared by the TS/JS server config below.
local ts_inlay_hints = {
  includeInlayParameterNameHints = "all",
  includeInlayParameterNameHintsWhenArgumentMatchesName = false,
  includeInlayFunctionParameterTypeHints = true,
  includeInlayVariableTypeHints = true,
  includeInlayVariableTypeHintsWhenTypeMatchesName = false,
  includeInlayPropertyDeclarationTypeHints = true,
  includeInlayFunctionLikeReturnTypeHints = true,
  includeInlayEnumMemberValueHints = true,
}
local ts_format = { indentSize = 2, tabSize = 2, convertTabsToSpaces = true }

vim.lsp.config("ts_ls", {
  single_file_support = false,
  settings = {
    typescript = { format = ts_format, inlayHints = ts_inlay_hints },
    javascript = { format = ts_format, inlayHints = ts_inlay_hints },
  },
})

-- The native TypeScript 7 server (`tsc --lsp`) reads its own settings key and
-- spells the inlay hints differently; keep them in step with ts_inlay_hints.
vim.lsp.config("tsc", {
  settings = {
    ["js/ts"] = {
      inlayHints = {
        parameterNames = { enabled = "all", suppressWhenArgumentMatchesName = true },
        parameterTypes = { enabled = true },
        variableTypes = { enabled = true },
        propertyDeclarationTypes = { enabled = true },
        functionLikeReturnTypes = { enabled = true },
        enumMemberValues = { enabled = true },
      },
    },
  },
})

-- ocamllsp is installed per-project inside an opam switch (`_opam/`), so it is
-- not on the global PATH. `opam exec` resolves the right switch from the cwd.
vim.lsp.config("ocamllsp", {
  cmd = { "opam", "exec", "--", "ocamllsp" },
})

-- Servers that work as-is with lspconfig's bundled defaults.
vim.lsp.enable({
  "zls",
  "tailwindcss",
  "astro",
  "rust_analyzer",
  "cmake",
  "pyright",
  "gopls",
  "kotlin_language_server",
  "dartls",
  "solargraph",
  "clangd",
  "eslint",
  "lua_ls",
  "ocamllsp",
})

-- ts_ls, tsc and denols all conflict, so enable exactly one based on the project
-- root. (None is in the enable() list above — this autocmd turns one on per
-- project.)
--
-- TypeScript 7 replaced the JS tsserver with a native binary, so its
-- node_modules/typescript ships no tsserver.js and ts_ls bails out on startup
-- with "provides no tsserver.js". lspconfig's `tsc` config speaks to the native
-- server over `tsc --lsp` instead, so projects whose own TypeScript has dropped
-- tsserver.js get that one.
local function needs_native_tsserver(root_dir)
  local ts_dir = root_dir .. "/node_modules/typescript"
  return vim.uv.fs_stat(ts_dir) ~= nil and vim.uv.fs_stat(ts_dir .. "/lib/tsserver.js") == nil
end

vim.api.nvim_create_autocmd("FileType", {
  pattern = { "javascript", "javascriptreact", "typescript", "typescriptreact" },
  callback = function(args)
    local bufnr = args.buf
    local root_dir = vim.fs.root(bufnr, { "package.json", "deno.json", "deno.jsonc" })

    if not root_dir then
      return
    end

    local is_deno = vim.uv.fs_stat(root_dir .. "/deno.json") or vim.uv.fs_stat(root_dir .. "/deno.jsonc")

    if is_deno then
      vim.lsp.enable("denols", true)
    elseif needs_native_tsserver(root_dir) then
      vim.lsp.enable("tsc", true)
    else
      vim.lsp.enable("ts_ls", true)
    end
  end,
})
