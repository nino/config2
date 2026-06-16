-- Reference counts as annotations above functions and classes.
--
-- For every function/method/class/etc. in the buffer this queries the LSP for
-- the number of references and renders it as virtual text on the line above the
-- definition, similar to VS Code's "references" CodeLens.

local M = {}

local ns = vim.api.nvim_create_namespace("reference_count")

vim.api.nvim_set_hl(0, "ReferenceCount", { default = true, fg = "#808080", ctermfg = 244 })

-- Symbol kinds we want to annotate. Values come from the LSP spec.
local SymbolKind = vim.lsp.protocol.SymbolKind
local annotated_kinds = {
  [SymbolKind.Function] = true,
  [SymbolKind.Method] = true,
  [SymbolKind.Class] = true,
  [SymbolKind.Constructor] = true,
  [SymbolKind.Interface] = true,
  [SymbolKind.Struct] = true,
  [SymbolKind.Enum] = true,
  -- Variables/Constants are only kept when bound to a function (see
  -- value_is_function); plain value constants are filtered out below.
  [SymbolKind.Variable] = true,
  [SymbolKind.Constant] = true,
}

-- Treesitter node types that represent a function value bound to a variable,
-- e.g. `const foo = () => ...` or `const foo = function () {}`.
local function_value_types = {
  arrow_function = true,
  function_expression = true,
  ["function"] = true,
  generator_function = true,
}

-- Whether annotations are currently enabled. Toggle with :ReferenceCountToggle.
local enabled = true

-- Per-buffer debounce timers, keyed by bufnr.
local timers = {}

--- Whether `range` covers a bare identifier in the buffer. Anonymous functions
--- come back with a synthesized name (e.g. "createLookupByKey() callback") whose
--- selectionRange spans the whole expression rather than a name, so this rejects
--- them — and with them anything not anchored to a real, referenceable symbol.
--- @param bufnr integer
--- @param range table LSP range with 0-indexed start/end
--- @return boolean
local function is_identifier(bufnr, range)
  -- Names always live on a single line.
  if range.start.line ~= range["end"].line then
    return false
  end
  local text = vim.api.nvim_buf_get_text(
    bufnr,
    range.start.line, range.start.character,
    range["end"].line, range["end"].character,
    {}
  )[1] or ""
  -- `$` is a valid identifier character in JS/TS.
  return text:match("^[%a_$][%w_$]*$") ~= nil
end

--- Whether the variable whose name sits at (line, character) is initialised to a
--- function. The LSP collapses `const foo = () => ...` into a single Constant
--- symbol with no detail, so treesitter is the only way to tell a function-valued
--- binding from a plain value constant like `const x = 5`.
--- @param bufnr integer
--- @param line integer 0-indexed
--- @param character integer 0-indexed
--- @return boolean
local function value_is_function(bufnr, line, character)
  local ok, node = pcall(vim.treesitter.get_node, { bufnr = bufnr, pos = { line, character } })
  if not ok or not node then
    return false
  end
  local declarator = node
  while declarator and declarator:type() ~= "variable_declarator" do
    declarator = declarator:parent()
  end
  if not declarator then
    return false
  end
  local value = declarator:field("value")[1]
  return value ~= nil and function_value_types[value:type()] == true
end

--- Flatten a documentSymbol response (which may be hierarchical DocumentSymbol[]
--- or flat SymbolInformation[]) into a list of { kind, line, character } entries
--- describing where to anchor and where to query each annotation.
--- @param bufnr integer
--- @param symbols table[]
--- @param out table[]
local function collect_symbols(bufnr, symbols, out)
  for _, symbol in ipairs(symbols) do
    -- DocumentSymbol has selectionRange (the name); SymbolInformation only
    -- has location.range. Prefer the name position for the reference query.
    local range = symbol.selectionRange or (symbol.location and symbol.location.range)
    if range and annotated_kinds[symbol.kind] and is_identifier(bufnr, range) then
      -- Variables/constants are only worth annotating when they hold a function.
      local kind_ok = symbol.kind ~= SymbolKind.Variable and symbol.kind ~= SymbolKind.Constant
        or value_is_function(bufnr, range.start.line, range.start.character)
      if kind_ok then
        table.insert(out, {
          query_line = range.start.line,
          query_character = range.start.character,
          anchor_line = range.start.line,
        })
      end
    end
    if symbol.children then
      collect_symbols(bufnr, symbol.children, out)
    end
  end
end

--- Place the annotation for a single symbol once its reference count is known.
--- @param bufnr integer
--- @param anchor_line integer 0-indexed line the definition lives on
--- @param count integer
local function place_annotation(bufnr, anchor_line, count)
  if not vim.api.nvim_buf_is_valid(bufnr) then
    return
  end
  -- Align the annotation with the indentation of the definition below it.
  local line_text = vim.api.nvim_buf_get_lines(bufnr, anchor_line, anchor_line + 1, false)[1] or ""
  local indent = line_text:match("^%s*") or ""
  local label = count == 1 and "1 reference" or (count .. " references")

  vim.api.nvim_buf_set_extmark(bufnr, ns, anchor_line, 0, {
    virt_lines = { { { indent .. label, "ReferenceCount" } } },
    virt_lines_above = true,
  })
end

--- Recompute and redraw all annotations for a buffer.
--- @param bufnr integer
function M.refresh(bufnr)
  bufnr = bufnr or vim.api.nvim_get_current_buf()
  if not enabled or not vim.api.nvim_buf_is_valid(bufnr) then
    return
  end

  local symbol_clients = vim.lsp.get_clients({ bufnr = bufnr, method = "textDocument/documentSymbol" })
  local reference_clients = vim.lsp.get_clients({ bufnr = bufnr, method = "textDocument/references" })
  if #symbol_clients == 0 or #reference_clients == 0 then
    return
  end
  local symbol_client = symbol_clients[1]
  local reference_client = reference_clients[1]

  local symbol_params = { textDocument = vim.lsp.util.make_text_document_params(bufnr) }
  symbol_client:request("textDocument/documentSymbol", symbol_params, function(err, result)
    if err or not result or not vim.api.nvim_buf_is_valid(bufnr) then
      return
    end

    local symbols = {}
    collect_symbols(bufnr, result, symbols)

    -- Clear only once we have a fresh symbol list, to avoid flicker.
    vim.api.nvim_buf_clear_namespace(bufnr, ns, 0, -1)

    for _, symbol in ipairs(symbols) do
      local ref_params = {
        textDocument = vim.lsp.util.make_text_document_params(bufnr),
        position = { line = symbol.query_line, character = symbol.query_character },
        context = { includeDeclaration = false },
      }
      reference_client:request("textDocument/references", ref_params, function(ref_err, ref_result)
        if ref_err or not ref_result then
          return
        end
        place_annotation(bufnr, symbol.anchor_line, #ref_result)
      end, bufnr)
    end
  end, bufnr)
end

--- Debounced refresh so rapid events (typing, cursor moves) don't spam the LSP.
--- @param bufnr integer
local function schedule_refresh(bufnr)
  bufnr = bufnr or vim.api.nvim_get_current_buf()
  if timers[bufnr] then
    timers[bufnr]:stop()
    timers[bufnr]:close()
    timers[bufnr] = nil
  end
  local timer = vim.uv.new_timer()
  timers[bufnr] = timer
  timer:start(300, 0, function()
    timer:stop()
    timer:close()
    timers[bufnr] = nil
    vim.schedule(function()
      M.refresh(bufnr)
    end)
  end)
end

function M.clear(bufnr)
  bufnr = bufnr or vim.api.nvim_get_current_buf()
  if vim.api.nvim_buf_is_valid(bufnr) then
    vim.api.nvim_buf_clear_namespace(bufnr, ns, 0, -1)
  end
end

function M.enable()
  enabled = true
  schedule_refresh(vim.api.nvim_get_current_buf())
end

function M.disable()
  enabled = false
  for _, bufnr in ipairs(vim.api.nvim_list_bufs()) do
    M.clear(bufnr)
  end
end

function M.toggle()
  if enabled then
    M.disable()
  else
    M.enable()
  end
end

local group = vim.api.nvim_create_augroup("ReferenceCount", { clear = true })

vim.api.nvim_create_autocmd("LspAttach", {
  group = group,
  callback = function(args)
    schedule_refresh(args.buf)
  end,
})

-- Refresh when the buffer's contents settle (after save / leaving insert) since
-- edits change both symbol positions and reference counts.
vim.api.nvim_create_autocmd({ "BufEnter", "BufWritePost", "InsertLeave" }, {
  group = group,
  callback = function(args)
    schedule_refresh(args.buf)
  end,
})

vim.api.nvim_create_user_command("ReferenceCountToggle", M.toggle, {})
vim.api.nvim_create_user_command("ReferenceCountRefresh", function()
  M.refresh(vim.api.nvim_get_current_buf())
end, {})

return M
