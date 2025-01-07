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

require("nfnl").setup()

