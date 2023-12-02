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
   'pyright',
   'erlangls',
   'elixirls',
   'terraformls',
   'kotlin_language_server'
})

vim.cmd ":Copilot disable"

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
   ['<CR>'] = cmp.mapping.confirm({ select = false }), -- Accept currently selected item. Set `select` to `false` to only confirm explicitly selected items.
   ['<C-f>'] = cmp.mapping.confirm({ select = true }),
   ["<C-space>"] = cmp.mapping.complete(),
})

cmp.setup({
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


-- DAP
-- require("dap-vscode-js").setup({
--   -- node_path = "node", -- Path of node executable. Defaults to $NODE_PATH, and then "node"
--   -- debugger_path = "(runtimedir)/site/pack/packer/opt/vscode-js-debug", -- Path to vscode-js-debug installation.
--   -- debugger_cmd = { "js-debug-adapter" }, -- Command to use to launch the debug server. Takes precedence over `node_path` and `debugger_path`.
--   adapters = { 'pwa-node', 'pwa-chrome', 'pwa-msedge', 'node-terminal', 'pwa-extensionHost' }, -- which adapters to register in nvim-dap
--   -- log_file_path = "(stdpath cache)/dap_vscode_js.log" -- Path for file logging
--   -- log_file_level = false -- Logging level for output to file. Set to false to disable file logging.
--   -- log_console_level = vim.log.levels.ERROR -- Logging level for output to console. Set to false to disable console output.
-- })

-- for _, language in ipairs({ "typescript", "javascript" }) do
--   require("dap").configurations[language] = {
--     ... -- see below
--   }
-- end

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
colors.generate()  -- Pass `true` to enable mirage
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

-- require("gruvbox").setup({
--     undercurl = true,
--     underline = true,
--     bold = true,
--     italic = {
--         strings = true,
--         comments = true,
--         operators = false,
--         folds = true,
--     },
--     strikethrough = true,
--     invert_selection = false,
--     invert_signs = false,
--     invert_tabline = false,
--     invert_intend_guides = false,
--     inverse = true, -- invert background for search, diffs, statuslines and errors
--     contrast = "",  -- can be "hard", "soft" or empty string
--     palette_overrides = {},
--     overrides = {},
--     dim_inactive = false,
--     transparent_mode = false,
-- })

vim.cmd.colorscheme('catppuccin-frappe')

vim.cmd [[
nmap <F6> <Plug>ColorstepPrev
nmap <F7> <Plug>ColorstepNext
nmap <S-F7> <Plug>ColorstepReload
]]

-- Diagnostics
function diagnostic_sign()
   if #vim.diagnostic.get(0) == 0 then
      return '♥︎'
   else
      return '×'
   end
end

-- Autocommands
vim.cmd [[
  augroup BQNFileType
    autocmd!
    autocmd BufRead,BufNewFile *.bqn set filetype=bqn
  augroup END

  augroup HCL
    autocmd!
    autocmd BufRead,BufNewFile *.hcl set filetype=tf
  augroup END

  augroup direnv
    autocmd!
    autocmd BufRead,BufNewFile .envrc set filetype=bash
  augroup END
]]


vim.cmd([[silent! autocmd! filetypedetect BufRead,BufNewFile *.ex]])
vim.cmd([[autocmd BufRead,BufNewFile *.ex set filetype=elixir]])


-- REPLs
local iron = require "iron.core"
iron.setup {
   config = {
      repl_definition = {
         lua = { command = "lua" },
         ruby = { command = "pry" },
         python = { command = "ipython" },
      },
      keymaps = {
         send_motion = "<m-i>",
         visual_send = "<c-l>",
         send_file = "<leader>sf",
         send_line = "`ll",
         send_until_cursor = "<leader>su",
         send_mark = "<leader>sm",
         mark_motion = "<leader>mc",
         mark_visual = "<space>mc",
         remove_mark = "<leader>md",
         cr = "<leader>s<cr>",
         interrupt = "<leader>s<leader>",
         exit = "<leader>sq",
         clear = "<leader>cl",
      },
   }
}

vim.keymap.set('n', '<leader>rs', '<cmd>IronRepl<cr>')
vim.keymap.set('n', '<leader>rr', '<cmd>IronRestart<cr>')
vim.keymap.set('n', '<leader>rf', '<cmd>IronFocus<cr>')
vim.keymap.set('n', '<leader>rh', '<cmd>IronHide<cr>')
vim.keymap.set('v', '<c-l>', function() iron.visual_send() end, {})
-- vim.keymap.set('n', '<m-i>', function() iron.send_motion() end, {})

vim.keymap.set(
   { "n", "o", "x" },
   "w",
   "<cmd>lua require('spider').motion('w')<CR>",
   { desc = "Spider-w" }
)
vim.keymap.set(
   { "n", "o", "x" },
   "e",
   "<cmd>lua require('spider').motion('e')<CR>",
   { desc = "Spider-e" }
)
vim.keymap.set(
   { "n", "o", "x" },
   "b",
   "<cmd>lua require('spider').motion('b')<CR>",
   { desc = "Spider-b" }
)
vim.keymap.set(
   { "n", "o", "x" },
   "ge",
   "<cmd>lua require('spider').motion('ge')<CR>",
   { desc = "Spider-ge" }
)
