-- This file can be loaded by calling `lua require('plugins')` from your init.vim

local js_languages = { 'javascript', 'typescript', 'javascriptreact', 'typescriptreact' }

return {
  'williamboman/mason.nvim',
  { 'nvim-treesitter/nvim-treesitter',         run = ':TSUpdate' },
  'https://github.com/tpope/vim-commentary',
  'mbbill/undotree',
  'tpope/vim-fugitive',
  'tpope/vim-rhubarb',
  'tpope/vim-surround',
  'editorconfig/editorconfig-vim',
  'tpope/vim-characterize',
  'rhysd/git-messenger.vim',
  {
    'https://github.com/github/copilot.vim',
    enabled = false,
    config = function()
      vim.cmd [[imap <silent><script><expr> <C-J> copilot#Accept("\<CR>")
        let g:copilot_no_tab_map = v:true
        ]]
    end
  },
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
      { 'hrsh7th/nvim-cmp' },     -- Required
      { 'hrsh7th/cmp-nvim-lsp' }, -- Required
      { 'hrsh7th/cmp-buffer' },
      { 'L3MON4D3/LuaSnip' },     -- Required
    }
  },
  {
    'https://github.com/nvim-telescope/telescope.nvim',
    requires = { { 'nvim-lua/plenary.nvim' } }
  },
  'https://github.com/nvim-telescope/telescope-live-grep-args.nvim',
  {
    "nvim-telescope/telescope-frecency.nvim",
    config = function()
      require("telescope").load_extension "frecency"
    end,
  },
  'tpope/vim-repeat',
  'preservim/nerdtree',
  'https://github.com/gleam-lang/gleam.vim',
  'https://github.com/godlygeek/tabular',
  'https://github.com/guns/vim-sexp',
  'https://github.com/tpope/vim-sexp-mappings-for-regular-people',
  'https://github.com/duane9/nvim-rg',
  'elixir-editors/vim-elixir',

  -- DAP
  {
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
  'https://github.com/leoluz/nvim-dap-go',
  "nvim-neotest/nvim-nio",
  { 'https://github.com/rcarriga/nvim-dap-ui', requires = { "nvim-neotest/nvim-nio" } },
  'https://github.com/theHamsta/nvim-dap-virtual-text',
  'https://github.com/nvim-telescope/telescope-dap.nvim',
  'https://github.com/mfussenegger/nvim-dap-python',
  {
    "julianolf/nvim-dap-lldb",
    dependencies = { "mfussenegger/nvim-dap" },
    opts = {
      codelldb_path = "~/.local/share/nvim/mason/bin/codelldb"
    },
  },

  'https://github.com/wsdjeg/vim-fetch',    -- Allow opening `path:linenr`
  {
    'https://github.com/Vigemus/iron.nvim', -- REPLs
    enabled = false,
    config = function()
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
    end
  },
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
  'https://github.com/Olical/nfnl',
  {
    'https://github.com/stevearc/oil.nvim',
    config = function()
      require('oil').setup()
    end
  },
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
  { 'https://github.com/cweagans/vim-taskpaper', enabled = false },
  {
    'Julian/lean.nvim',
    enabled = false,
    event = { 'BufReadPre *.lean', 'BufNewFile *.lean' },

    dependencies = {
      'neovim/nvim-lspconfig',
      'nvim-lua/plenary.nvim',
      -- you also will likely want nvim-cmp or some completion engine
    },

    -- see details below for full configuration options
    opts = {
      lsp = {},
      mappings = true,
    }
  },
  -- 'https://github.com/mg979/vim-visual-multi',
  { "https://github.com/Olical/nfnl",            ft = "fennel" },
  {
    "yetone/avante.nvim",
    enabled = true,
    event = "VeryLazy",
    lazy = false,
    version = "*", -- set this to "*" if you want to always pull the latest change, false to update on release
    opts = {
      -- add any opts here
      behaviour = {
        auto_suggestions = false, -- Experimental stage
      }
    },
    -- if you want to build from source then do `make BUILD_FROM_SOURCE=true`
    build = "make",
    -- build = "powershell -ExecutionPolicy Bypass -File Build.ps1 -BuildFromSource false" -- for windows
    dependencies = {
      "stevearc/dressing.nvim",
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
      --- The below dependencies are optional,
      "hrsh7th/nvim-cmp",            -- autocompletion for avante commands and mentions
      "nvim-tree/nvim-web-devicons", -- or echasnovski/mini.icons
      "zbirenbaum/copilot.lua",      -- for providers='copilot'
      {
        -- support for image pasting
        "HakonHarnes/img-clip.nvim",
        event = "VeryLazy",
        opts = {
          -- recommended settings
          default = {
            embed_image_as_base64 = false,
            prompt_for_file_name = false,
            drag_and_drop = {
              insert_mode = true,
            },
            -- required for Windows users
            use_absolute_path = true,
          },
        },
      },
      {
        -- Make sure to set this up properly if you have lazy=true
        'MeanderingProgrammer/render-markdown.nvim',
        opts = {
          file_types = { "markdown", "Avante" },
        },
        ft = { "markdown", "Avante" },
      },
    },
  },
  {
    "olimorris/codecompanion.nvim",
    enabled = false,
    dependencies = {
      "nvim-lua/plenary.nvim",
      "nvim-treesitter/nvim-treesitter",
    },
    config = function()
      require("codecompanion").setup({
        display = {
          -- diff = {
          --   provider = "mini_diff",
          -- },
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
    end
  },
  { 'https://github.com/stevearc/dressing.nvim', enabled = true },
  'https://github.com/Sangdol/mintabline.vim',
  'https://github.com/vlime/vlime',
  {
    {

      'https://github.com/Olical/conjure',
      ft = { "clojure", "fennel" },
      lazy = true,
      init = function()
        -- Any additional configuration can go here
      end
    }
  },
  -- 'https://gitlab.com/HiPhish/rainbow-delimiters.nvim',
  -- { 'https://github.com/chentau/marks.nvim' },

  -- Colors
  { 'https://github.com/miikanissi/modus-themes.nvim', priority = 1000 }, -- "Highly accessible"
  -- 'https://github.com/echasnovski/mini.diff',
  { "MeanderingProgrammer/render-markdown.nvim", ft = { "markdown", "codecompanion" } },
  {
    'https://github.com/sphamba/smear-cursor.nvim',
    enabled = false,
    opts = {                         -- Default  Range
      stiffness = 0.8,               -- 0.6      [0, 1]
      trailing_stiffness = 0.5,      -- 0.3      [0, 1]
      distance_stop_animating = 0.5, -- 0.1      > 0
      hide_target_hack = false,      -- true     boolean
      cursor_color = "#FF00EE",
    },
  },
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
  { 'https://github.com/delphinus/vim-firestore' },
}
