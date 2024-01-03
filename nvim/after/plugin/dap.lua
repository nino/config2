local dap = require("dap")

vim.keymap.set("n", "<leader>db", function() dap.toggle_breakpoint() end, { noremap = true, silent = true })
vim.keymap.set("n", "<m-1>", function() dap.step_into() end, { noremap = true, silent = true })
vim.keymap.set("n", "<m-2>", function() dap.step_over() end, { noremap = true, silent = true })
vim.keymap.set("n", "<m-3>", function() dap.step_out() end, { noremap = true, silent = true })
vim.keymap.set("n", "<m-4>", function() dap.continue() end, { noremap = true, silent = true })

require("dap-go").setup()
require("dap-python").setup()
local dapui = require("dapui")
dapui.setup()

vim.api.nvim_create_user_command("DUI", function() dapui.toggle() end, {})
