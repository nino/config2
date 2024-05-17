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


-- Diagnostics
function diagnostic_sign()
  if #vim.diagnostic.get(0) == 0 then
    return '♥︎'
  else
    return '×'
  end
end

-- REPLs
local iron = require "iron.core"
iron.setup {
  config = {
    repl_definition = {
      lua = { command = "lua" },
      ruby = { command = "pry" },
      python = { command = "python" },
      fennel = { command = "fennel" },
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

require("ohne-accidents").setup({ welcomeOnStartup = false })

require("nfnl").setup()


require('spectre').setup({
  default = {
    replace = {
      cmd = "sd"
    }
  }
})

vim.keymap.set('n', '<leader>S', '<cmd>lua require("spectre").toggle()<CR>', {
  desc = "Toggle Spectre"
})
vim.keymap.set('n', '<leader>sw', '<cmd>lua require("spectre").open_visual({select_word=true})<CR>', {
  desc = "Search current word"
})
vim.keymap.set('v', '<leader>sw', '<esc><cmd>lua require("spectre").open_visual()<CR>', {
  desc = "Search current word"
})
vim.keymap.set('n', '<leader>sp', '<cmd>lua require("spectre").open_file_search({select_word=true})<CR>', {
  desc = "Search on current file"
})
