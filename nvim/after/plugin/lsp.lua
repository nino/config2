-- VS Code provides its own LSP, completion, linting and formatting.
if vim.g.vscode then
  return
end

vim.diagnostic.config({ virtual_text = false, jump = { float = true } })

-- Which inlay hints the language servers send. They are off until <leader>h
-- turns them on in a buffer; this table decides what shows up when they do.
-- Edit the flags here rather than the per-server settings below, which are
-- generated from them -- every server spells these differently, and some
-- support only a few of them.
local inlay_hints = {
  -- Names of the parameters an argument is being passed to: false, "literals"
  -- (only for literal arguments, e.g. `foo(bar: true)`) or "all". gopls reads
  -- anything other than false as "all".
  parameter_names = false,
  -- Types of the parameters in a function's own signature.
  parameter_types = false,
  -- Types of variables at their declaration.
  variable_types = true,
  -- Types of variables whose name already says the type, e.g.
  -- `const user = getUser()`. Only applies when variable_types is on. (TS/JS)
  variable_types_matching_name = false,
  -- Types of class properties at their declaration. (TS/JS)
  property_types = true,
  -- Return types of functions that do not write one out.
  return_types = false,
  -- Values of enum members, and of Go constants, that do not write one out.
  enum_member_values = false,
  -- Field names inside composite literals, e.g. `Point{1, 2}`. (Go)
  composite_literal_fields = false,
  -- Types of nested composite literals. (Go)
  composite_literal_types = false,
  -- Types inferred for a function's type parameters. (Go)
  function_type_parameters = false,
  -- Types of the variables bound by a `range` clause. (Go)
  range_variable_types = false,
}

-- Completion capabilities (blink.cmp) applied to *every* server via the "*"
-- wildcard, instead of repeating `capabilities = ...` on each server config.
vim.lsp.config("*", {
  capabilities = require("blink.cmp").get_lsp_capabilities(),
})

-- References without imports.
--
-- Half of a `grr` quickfix list is usually the identifier's import statements
-- rather than anything that uses it. The filtering is done with treesitter, not
-- by matching /import/ against the quickfix line: prettier wraps a long import
-- across lines, and the entry for `foo` in such a block is the bare line
-- "  foo," with no "import" on it.

-- Nodes whose subtree does not count as a use: whole import statements, plus
-- js/ts export clauses, which cover both `export { foo }` and
-- `export { foo } from "./foo"`. An export clause is names only, so nothing
-- real hides in one -- `export const bar = foo` has no export_clause ancestor
-- and survives.
local non_use_nodes = {
  import_statement = true, -- js/ts, python
  import_from_statement = true, -- python
  import_declaration = true, -- go, java
  use_declaration = true, -- rust
  using_directive = true, -- c#
  export_clause = true, -- js/ts
}

--- Root node of `filename`, parsed from the file on disk. Going via a buffer
--- would fire BufRead, and with it the linter below, once per file in the list.
--- @param filename string
--- @return TSNode|nil root, nil when the file has no treesitter parser
local function parse_file(filename)
  local ft = vim.filetype.match({ filename = filename })
  local lang = ft and vim.treesitter.language.get_lang(ft)
  if not lang then
    return nil
  end
  local ok, lines = pcall(vim.fn.readfile, filename)
  if not ok then
    return nil
  end
  local parsed, parser = pcall(vim.treesitter.get_string_parser, table.concat(lines, "\n"), lang)
  if not parsed then
    return nil
  end
  local tree = parser:parse()[1]
  return tree and tree:root() or nil
end

--- Whether the reference at `item` sits inside an import (or export clause).
--- @param root TSNode
--- @param item table quickfix item, with 1-indexed lnum and byte col
--- @return boolean
local function is_import(root, item)
  local node = root:named_descendant_for_range(item.lnum - 1, item.col - 1, item.lnum - 1, item.col - 1)
  while node do
    if non_use_nodes[node:type()] then
      return true
    end
    node = node:parent()
  end
  return false
end

--- Like vim.lsp.buf.references, minus the import statements. Files are parsed
--- once each, so the cost is one read and parse per file in the list.
local function references_excluding_imports()
  vim.lsp.buf.references({ includeDeclaration = false }, {
    on_list = function(list)
      local roots = {}
      list.items = vim.tbl_filter(function(item)
        if roots[item.filename] == nil then
          roots[item.filename] = parse_file(item.filename) or false
        end
        local root = roots[item.filename]
        return not (root and is_import(root, item))
      end, list.items)
      if #list.items == 0 then
        vim.notify("No references outside imports", vim.log.levels.INFO)
        return
      end
      vim.fn.setqflist({}, " ", list)
      vim.cmd.copen()
    end,
  })
end

-- Buffer-local LSP keymaps
vim.api.nvim_create_autocmd("LspAttach", {
  callback = function(args)
    local bufnr = args.buf
    vim.keymap.set("n", "gd", vim.lsp.buf.definition, { buffer = bufnr })
    vim.keymap.set("n", "gD", vim.lsp.buf.declaration, { buffer = bufnr })
    vim.keymap.set("n", "gi", vim.lsp.buf.implementation, { buffer = bufnr })
    -- Overrides the built-in grr, which lists imports alongside the uses.
    -- `:lua vim.lsp.buf.references()` still gives the unfiltered list.
    vim.keymap.set("n", "grr", references_excluding_imports, { buffer = bufnr })
    -- Call hierarchy (VS Code's "Show Call Hierarchy"), rendered in Trouble.
    -- Sits under the same <leader>x prefix as the other Trouble panels.
    vim.keymap.set("n", "<leader>xi", "<cmd>Trouble lsp_incoming_calls toggle<cr>", { buffer = bufnr })
    vim.keymap.set("n", "<leader>xo", "<cmd>Trouble lsp_outgoing_calls toggle<cr>", { buffer = bufnr })
  end,
})

-- Inlay hints start off everywhere; this turns them on for one buffer, showing
-- the kinds the `inlay_hints` table at the top of the file asks for.
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
        assignVariableTypes = inlay_hints.variable_types,
        compositeLiteralFields = inlay_hints.composite_literal_fields,
        compositeLiteralTypes = inlay_hints.composite_literal_types,
        constantValues = inlay_hints.enum_member_values,
        functionTypeParameters = inlay_hints.function_type_parameters,
        parameterNames = inlay_hints.parameter_names ~= false,
        rangeVariableTypes = inlay_hints.range_variable_types,
      },
    },
  },
})

-- Inlay-hint settings shared by the TS/JS server config below.
local ts_inlay_hints = {
  includeInlayParameterNameHints = inlay_hints.parameter_names or "none",
  includeInlayFunctionParameterTypeHints = inlay_hints.parameter_types,
  includeInlayVariableTypeHints = inlay_hints.variable_types,
  includeInlayVariableTypeHintsWhenTypeMatchesName = inlay_hints.variable_types_matching_name,
  includeInlayPropertyDeclarationTypeHints = inlay_hints.property_types,
  includeInlayFunctionLikeReturnTypeHints = inlay_hints.return_types,
  includeInlayEnumMemberValueHints = inlay_hints.enum_member_values,
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
        parameterNames = { enabled = inlay_hints.parameter_names or "none" },
        parameterTypes = { enabled = inlay_hints.parameter_types },
        variableTypes = { enabled = inlay_hints.variable_types },
        propertyDeclarationTypes = { enabled = inlay_hints.property_types },
        functionLikeReturnTypes = { enabled = inlay_hints.return_types },
        enumMemberValues = { enabled = inlay_hints.enum_member_values },
      },
    },
  },
})

-- ocamllsp is installed per-project inside an opam switch (`_opam/`), so it is
-- not on the global PATH. `opam exec` resolves the right switch from the cwd.
vim.lsp.config("ocamllsp", {
  cmd = { "opam", "exec", "--", "ocamllsp" },
})

-- The Gleam compiler ships its own language server (`gleam lsp`) and
-- lspconfig's bundled config already points at it, so no override is needed
-- here. The binary comes from a mise shim, which picks the version from the
-- process cwd -- so start nvim inside the project. From elsewhere the shim
-- reports "No version is set for shim: gleam"; `mise use -g gleam@latest`
-- makes it cwd-independent.

-- pyright resolves imports against whatever `python` is on PATH, which in a
-- uv project is not the project's interpreter. Point it at the local venv
-- (`.venv/`, which uv and `python -m venv` both create by default) or at an
-- already-activated one, so third-party packages resolve.
--
-- The pyright binary itself is pip-installed in the mise python, reached via
-- a mise shim. The shim only resolves where a python version is active, so
-- the global mise config pins one; without that, opening a file in a uv
-- project fails with "No version is set for shim: pyright-langserver".
local function find_python(root_dir)
  local venv = vim.env.VIRTUAL_ENV
  if venv and vim.uv.fs_stat(venv .. "/bin/python") then
    return venv .. "/bin/python"
  end
  for _, dir in ipairs({ ".venv", "venv" }) do
    local python = root_dir .. "/" .. dir .. "/bin/python"
    if vim.uv.fs_stat(python) then
      return python
    end
  end
end

-- (`on_init` rather than `before_init`: the client copies `settings` when it
-- is created, so edits to the config in `before_init` never reach the server.)
vim.lsp.config("pyright", {
  on_init = function(client)
    local python = client.root_dir and find_python(client.root_dir)
    if python then
      client.settings = vim.tbl_deep_extend("force", client.settings, {
        python = { pythonPath = python },
      })
      client:notify("workspace/didChangeConfiguration", { settings = client.settings })
    end
  end,
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
  "gleam",
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
