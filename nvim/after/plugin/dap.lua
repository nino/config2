pcall(function()
  local dap = require("dap")

  vim.keymap.set("n", "<leader><m-b>", function() dap.toggle_breakpoint() end, { noremap = true, silent = true })
  vim.keymap.set("n", "<m-1>", function() dap.step_into() end, { noremap = true, silent = true })
  vim.keymap.set("n", "<m-2>", function() dap.step_over() end, { noremap = true, silent = true })
  vim.keymap.set("n", "<m-3>", function() dap.step_out() end, { noremap = true, silent = true })
  vim.keymap.set("n", "<m-4>", function() dap.continue() end, { noremap = true, silent = true })

  require("dap-go").setup()
  require("dap-python").setup()
  -- require("dap-vscode-js").setup({
  --   adapters = { 'pwa-node' },
  -- })
  -- require('dap-lldb').setup({})

  -- for _, language in ipairs({ "typescript", "javascript" }) do
  --   require("dap").configurations[language] = {
  --     {
  --       type = "pwa-node",
  --       request = "launch",
  --       name = "Launch file",
  --       program = "${file}",
  --       cwd = "${workspaceFolder}",
  --     },
  --     {
  --       type = "pwa-node",
  --       request = "attach",
  --       name = "Attach",
  --       processId = require 'dap.utils'.pick_process,
  --       cwd = "${workspaceFolder}",
  --     }
  --   }
  -- end

  -- require('dap').adapters.codelldb = {
  --   type = 'executable',
  --   attach = {
  --     pidProperty = "pid",
  --     pidSelect = "ask"
  --   },
  --   command = '/Users/Nino/.vscode/extensions/lanza.lldb-vscode-0.2.3/bin/darwin/bin/lldb-vscode', -- my binary was called 'lldb-vscode-11'
  --   -- env = {
  --   --   LLDB_LAUNCH_FLAG_LAUNCH_IN_TTY = "YES"
  --   -- },
  --   -- executable = {
  --   --   command =  '/Users/Nino/.vscode/extensions/lanza.lldb-vscode-0.2.3/bin/darwin/bin/lldb-vscode',
  --   --   args = { "--liblldb", '/Users/Nino/.vscode/extensions/lanza.lldb-vscode-0.2.3/bin/darwin/lib/liblldb.9.0.0svn.dylib' },
  --   -- },
  --   name = "lldb"
  -- }
  -- require('dap').configurations.c = {
  --   {
  --     name = "lldb",
  --     type = "codelldb",
  --     request = "launch",
  --     program = function()
  --       return vim.fn.input('Path to executable: ', vim.fn.getcwd() .. '/', 'file')
  --     end,
  --     cwd = '${workspaceFolder}',
  --     externalTerminal = true,
  --     stopOnEntry = false,
  --     args = {}
  --   },
  -- }

  dap.adapters.gdb = {
    type = "executable",
    command = "gdb",
    args = { "-i", "dap" }
  }

  dap.configurations.c = {
    {
      name = "Launch",
      type = "gdb",
      request = "launch",
      program = function()
        return vim.fn.input('Path to executable: ', vim.fn.getcwd() .. '/', 'file')
      end,
      cwd = "${workspaceFolder}",
      stopAtBeginningOfMainSubprogram = false,
    },
  }

  dap.adapters.lldb = {
    type = "executable",
    command = "/Users/Nino/.vscode/extensions/lanza.lldb-vscode-0.2.3/bin/darwin/bin/lldb-vscode", -- adjust as needed
    name = "lldb",
  }

  local lldb = {
    name = "Launch lldb",
    type = "lldb",   -- matches the adapter
    request = "launch", -- could also attach to a currently running process
    program = function()
      return vim.fn.input(
        "Path to executable: ",
        vim.fn.getcwd() .. "/",
        "file"
      )
    end,
    cwd = "${workspaceFolder}",
    stopOnEntry = false,
    args = {},
    runInTerminal = false,
  }

  -- require('dap').configurations.rust = {
  -- 	lldb -- different debuggers or more configurations can be used here
  -- }

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
end)
