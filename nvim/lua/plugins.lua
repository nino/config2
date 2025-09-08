-- This file can be loaded by calling `lua require('plugins')` from your init.vim

local js_languages = { 'javascript', 'typescript', 'javascriptreact', 'typescriptreact' }

return {
  'williamboman/mason.nvim',
  { 'nvim-treesitter/nvim-treesitter',                                 run = ':TSUpdate' },
  'https://github.com/tpope/vim-commentary',
  'mbbill/undotree',
  'tpope/vim-fugitive',
  'tpope/vim-rhubarb',
  'tpope/vim-surround',
  -- 'editorconfig/editorconfig-vim', -- (might not need this anymore?)
  'tpope/vim-characterize',
  -- 'rhysd/git-messenger.vim',
  {
    'neovim/nvim-lspconfig',
    dependencies = { {
      "folke/lazydev.nvim",
      ft = "lua", -- only load on lua files
      opts = {
        library = {
          -- See the configuration section for more details
          -- Load luvit types when the `vim.uv` word is found
          { path = "${3rd}/luv/library", words = { "vim%.uv" } },
        },
      },
    }, }
  },
  'hrsh7th/nvim-cmp',
  'hrsh7th/cmp-nvim-lsp',
  'hrsh7th/cmp-buffer',
  'L3MON4D3/LuaSnip', -- Required

  {
    'VonHeikemen/lsp-zero.nvim',
    branch = 'v2.x',
    requires = {
      -- LSP Support
      { 'neovim/nvim-lspconfig' }, -- Required
      {
        -- Optional
        'williamboman/mason.nvim',
        run = function()
          pcall(vim.cmd, 'MasonUpdate')
        end,
      },
      { 'williamboman/mason-lspconfig.nvim' }, -- Optional

      -- Autocompletion
      -- { 'hrsh7th/nvim-cmp' },     -- Required
      -- { 'hrsh7th/cmp-nvim-lsp' }, -- Required
      -- { 'hrsh7th/cmp-buffer' },
      { 'L3MON4D3/LuaSnip' }, -- Required
    }
  },
  {
    'https://github.com/nvim-telescope/telescope.nvim',
    requires = { { 'nvim-lua/plenary.nvim' } }
  },
  { 'https://github.com/nvim-telescope/telescope-live-grep-args.nvim', enabled = false },
  'tpope/vim-repeat',
  'preservim/nerdtree',
  { 'https://github.com/gleam-lang/gleam.vim',                       enabled = false },
  'https://github.com/godlygeek/tabular',
  { 'https://github.com/guns/vim-sexp',                              enabled = false },
  { 'https://github.com/tpope/vim-sexp-mappings-for-regular-people', enabled = false },
  'https://github.com/duane9/nvim-rg',
  -- { 'elixir-editors/vim-elixir',             enabled = false },

  -- DAP
  {
    enabled = false,
    'https://github.com/mfussenegger/nvim-dap',
    config = function()
      local dap = require "dap"
      -- local Config = require "lazyvim.config"
      -- vim.api.nvim


      for _, language in ipairs(js_languages) do
        dap.configurations[language] = {
          -- Debug single nodejs files
          {
            type = "pwa-node",
            request = "launch",
            name = "Launch file",
            program = "${file}",
            cwd = vim.fn.getcwd(),
            sourceMaps = true,
          },
          -- Debug nodejs processes (make sure to add --inspect when you run the process)
          {
            type = "pwa-node",
            request = "attach",
            name = "Attach",
            processId = require("dap.utils").pick_process,
            cwd = vim.fn.getcwd(),
            sourceMaps = true,
          },
          -- Debug web applications (client side)
          {
            type = "pwa-chrome",
            request = "launch",
            name = "Launch & Debug Chrome",
            url = function()
              local co = coroutine.running()
              return coroutine.create(function()
                vim.ui.input({
                  prompt = "Enter URL: ",
                  default = "http://localhost:3000",
                }, function(url)
                  if url == nil or url == "" then
                    return
                  else
                    coroutine.resume(co, url)
                  end
                end)
              end)
            end,
            webRoot = vim.fn.getcwd(),
            protocol = "inspector",
            sourceMaps = true,
            userDataDir = false,
          },
          -- Divider for the launch.json derived configs
          {
            name = "----- ↓ launch.json configs ↓ -----",
            type = "",
            request = "launch",
          },
        }
      end
    end,
    keys = {
      -- {
      --   "<leader>da",
      --   function()
      --     if vim.fn.filereadable(".vscode/launch.json") then
      --       local dap_vscode = require("dap.ext.vscode")
      --       dap_vscode.load_launchjs(nil, {
      --         ["pwa-node"] = js_languages,
      --         ["node"] = js_languages,
      --       })
      --     end
      --     require("dap").continue()
      --   end,
      --   desc = "Run with Args",
      -- }
    },
    dependencies = {
      -- {
      --   "microsoft/vscode-js-debug",
      --   -- After install, build it and rename the dist directory to out
      --   build = "npm install && npx gulp vsDebugServerBundle && mv dist out",
      --   -- version = "1.*",
      -- },
      --{
      --  "mxsdev/nvim-dap-vscode-js",
      --  config = function()
      --    ---@diagnostic disable-next-line: missing-fields
      --    require("dap-vscode-js").setup({
      --      -- Path of node executable. Defaults to $NODE_PATH, and then "node"
      --      -- node_path = "node",

      --      -- Path to vscode-js-debug installation.
      --      debugger_path = vim.fn.resolve(vim.fn.stdpath("data") .. "/lazy/vscode-js-debug"),

      --      -- Command to use to launch the debug server. Takes precedence over "node_path" and "debugger_path"
      --      -- debugger_cmd = { "js-debug-adapter" },

      --      -- which adapters to register in nvim-dap
      --      adapters = {
      --        "chrome",
      --        "pwa-node",
      --        "pwa-chrome",
      --        "pwa-msedge",
      --        "pwa-extensionHost",
      --        "node-terminal",
      --        "node",
      --      },

      --      -- Path for file logging
      --      -- log_file_path = "(stdpath cache)/dap_vscode_js.log",

      --      -- Logging level for output to file. Set to false to disable logging.
      --      -- log_file_level = false,

      --      -- Logging level for output to console. Set to false to disable console output.
      --      -- log_console_level = vim.log.levels.ERROR,
      --    })
      --  end,
      --},
      {
        "Joakker/lua-json5",
        build = "./install.sh",
      },
    }
  },
  -- 'https://github.com/mxsdev/nvim-dap-vscode-js',
  { 'https://github.com/leoluz/nvim-dap-go',                enabled = false },
  "nvim-neotest/nvim-nio",
  { 'https://github.com/rcarriga/nvim-dap-ui',              requires = { "nvim-neotest/nvim-nio" } },
  { 'https://github.com/theHamsta/nvim-dap-virtual-text',   enabled = false },
  { 'https://github.com/nvim-telescope/telescope-dap.nvim', enabled = false },
  { 'https://github.com/mfussenegger/nvim-dap-python',      enabled = false },
  {
    enabled = false,
    "julianolf/nvim-dap-lldb",
    dependencies = { "mfussenegger/nvim-dap" },
    opts = {
      codelldb_path = "~/.local/share/nvim/mason/bin/codelldb"
    },
  },

  'https://github.com/wsdjeg/vim-fetch', -- Allow opening `path:linenr`
  'https://github.com/mfussenegger/nvim-lint',
  'https://github.com/NoahTheDuke/vim-just',
  -- 'https://github.com/lukas-reineke/indent-blankline.nvim',
  -- 'https://github.com/chrisbra/vim-diff-enhanced',
  {
    "https://github.com/stevearc/conform.nvim",
    config = function()
      require("conform").setup()
    end,
  },
  -- {
  --   'https://github.com/stevearc/oil.nvim',
  --   config = function()
  --     require('oil').setup()
  --   end
  -- },
  -- {
  --   'https://github.com/lewis6991/gitsigns.nvim',
  --   config = function()
  --     require('gitsigns').setup()
  --   end
  -- },
  {
    'https://github.com/nvim-pack/nvim-spectre',
    config = function()
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
    end
  },
  -- { 'https://github.com/cweagans/vim-taskpaper', enabled = false },
  -- {
  --   'Julian/lean.nvim',
  --   enabled = false,
  --   event = { 'BufReadPre *.lean', 'BufNewFile *.lean' },

  --   dependencies = {
  --     'neovim/nvim-lspconfig',
  --     'nvim-lua/plenary.nvim',
  --     -- you also will likely want nvim-cmp or some completion engine
  --   },

  --   -- see details below for full configuration options
  --   opts = {
  --     lsp = {},
  --     mappings = true,
  --   }
  -- },
  -- 'https://github.com/mg979/vim-visual-multi',
  { "https://github.com/Olical/nfnl",            ft = "fennel" },
  { 'https://github.com/stevearc/dressing.nvim', enabled = true },
  'https://github.com/vlime/vlime',
  {
    enabled = false,
    'https://github.com/Olical/conjure',
    ft = { "clojure", "fennel" },
    lazy = true,
    init = function()
      -- Any additional configuration can go here
    end
  },

  -- Colors
  { 'https://github.com/miikanissi/modus-themes.nvim', priority = 1000,    enabled = true },                  -- "Highly accessible"
  { "MeanderingProgrammer/render-markdown.nvim",       ft = { "markdown" } },
  {
    "christoomey/vim-tmux-navigator",
    cmd = {
      "TmuxNavigateLeft",
      "TmuxNavigateDown",
      "TmuxNavigateUp",
      "TmuxNavigateRight",
      "TmuxNavigatePrevious",
      "TmuxNavigatorProcessList",
    },
    keys = {
      { "<c-h>",  "<cmd><C-U>TmuxNavigateLeft<cr>" },
      { "<c-j>",  "<cmd><C-U>TmuxNavigateDown<cr>" },
      { "<c-k>",  "<cmd><C-U>TmuxNavigateUp<cr>" },
      { "<c-l>",  "<cmd><C-U>TmuxNavigateRight<cr>" },
      { "<c-\\>", "<cmd><C-U>TmuxNavigatePrevious<cr>" },
    },
  },
}
