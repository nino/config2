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

require("nfnl").setup()

require('spectre').setup({
  default = {
    replace = {
      cmd = "oxi"
    }
  }
})

vim.keymap.set('n', '<leader>S', '<cmd>lua require("spectre").toggle()<CR>', {
  desc = "Toggle Spectre"
})
vim.keymap.set('n', '<m-f>', '<cmd>lua require("spectre").toggle()<CR>', {
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

-- AI
require("codecompanion").setup({
  strategies = {
    chat = {
      adapter = "anthropic",
    },
    inline = {
      adapter = "copilot",
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
