local dap = require("dap")

vim.keymap.set("n", "<leader><m-b>", function() dap.toggle_breakpoint() end, { noremap = true, silent = true })
vim.keymap.set("n", "<m-1>", function() dap.step_into() end, { noremap = true, silent = true })
vim.keymap.set("n", "<m-2>", function() dap.step_over() end, { noremap = true, silent = true })
vim.keymap.set("n", "<m-3>", function() dap.step_out() end, { noremap = true, silent = true })
vim.keymap.set("n", "<m-4>", function() dap.continue() end, { noremap = true, silent = true })

require("dap-go").setup()
require("dap-python").setup()
require("dap-vscode-js").setup({
  adapters = { 'pwa-node' },
})

for _, language in ipairs({ "typescript", "javascript" }) do
  require("dap").configurations[language] = {
    {
      type = "pwa-node",
      request = "launch",
      name = "Launch file",
      program = "${file}",
      cwd = "${workspaceFolder}",
    },
    {
      type = "pwa-node",
      request = "attach",
      name = "Attach",
      processId = require 'dap.utils'.pick_process,
      cwd = "${workspaceFolder}",
    }
  }
end

local dapui = require("dapui")
dapui.setup()

if vim.o.bg == 'light' then
  vim.cmd [[
    hi DapUIScope guifg=#000000 guibg=#ffffff gui=bold
    hi DapUIStoppedThread guifg=#000000 guibg=#ffffff gui=bold
    hi DapUIBreakpointsCurrentLine guifg=#000000 guibg=#ffffff gui=bold
    hi DapUIBreakpointsPath guifg=#000000 guibg=#ffffff gui=bold
    hi DapUILineNumber guifg=#000000 guibg=#ffffff
    hi DapUIDecoration guifg=##10b981
  ]]
end


vim.api.nvim_create_user_command("DUI", function() dapui.toggle() end, {})
