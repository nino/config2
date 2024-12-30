local fnlutils = require("fnlutils")
local actions = require("telescope.actions")
require "telescope".setup {
  defaults = {
    layout_strategy = "vertical",
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



-- Diagnostics
function diagnostic_sign()
  return fnlutils["diagnostic-sign"]()
end

-- REPLs
local iron = require "iron.core"
iron.setup {
  config = {
    repl_definition = {
      lisp = { command = "sbcl" },
      lua = { command = "lua" },
      ruby = { command = "pry" },
      python = { command = "uv run ipython" },
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

require("nfnl").setup()


-- AI
require("codecompanion").setup({
  display = {
    diff = {
      provider = "mini_diff",
    },
  },
  strategies = {
    chat = {
      adapter = "anthropic",
    },
    inline = {
      adapter = "anthropic",
    },
    agent = {
      adapter = "anthropic",
    },
  },
  adapters = {
    anthropic = function()
      return require("codecompanion.adapters").extend("anthropic", {
        env = {
          api_key = os.getenv("ANTHROPIC_API_KEY")
        },
      })
    end,
  },
})

vim.api.nvim_set_keymap("n", "<leader>aa", "<cmd>CodeCompanionActions<cr>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("v", "<leader>aa", "<cmd>CodeCompanionActions<cr>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<leader>at", "<cmd>CodeCompanionChat Toggle<cr>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("v", "<leader>at", "<cmd>CodeCompanionChat Toggle<cr>", { noremap = true, silent = true })
