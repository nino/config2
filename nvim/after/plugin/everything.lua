-- Telescope is disabled under vscode-neovim (VS Code has its own pickers).
if vim.g.vscode then
  return
end

local actions = require("telescope.actions")
require("telescope").setup({
  defaults = {
    layout_strategy = "vertical",
    preview = {
      treesitter = true,
    },
    mappings = {
      i = {
        ["<M-Q>"] = actions.send_to_qflist + actions.open_qflist,
      },
      n = {
        ["<M-Q>"] = actions.send_to_qflist + actions.open_qflist,
      },
    },
  },
})
