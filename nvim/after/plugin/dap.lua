vim.keymap.set("n", "<leader>dc", "<cmd>lua require('dap').continue()<CR>", { noremap = true, silent = true })
vim.keymap.set("n", "<leader>db", "<cmd>lua require('dap').toggle_breakpoint()<CR>", { noremap = true, silent = true })

require("dap-go").setup()
require("dap-python").setup()
require("dapui").setup()
