-- This file can be loaded by calling `lua require('plugins')` from your init.vim

return {
  { "nvim-treesitter/nvim-treesitter", branch = "main", build = ":TSUpdate" },
  "mbbill/undotree",
  "tpope/vim-fugitive",
  "tpope/vim-rhubarb",
  "tpope/vim-surround",
  "tpope/vim-characterize",
  "tpope/vim-repeat",
  "https://github.com/godlygeek/tabular",
  "https://github.com/duane9/nvim-rg",
  "https://github.com/wsdjeg/vim-fetch", -- Allow opening `path:linenr`
  "https://github.com/mfussenegger/nvim-lint",
  "https://github.com/NoahTheDuke/vim-just",
  "https://github.com/vlime/vlime",

  -- Git
  {
    "https://github.com/lewis6991/gitsigns.nvim",
    opts = {}, -- opts = {} makes lazy call require("gitsigns").setup()
  },

  -- LSP
  {
    "neovim/nvim-lspconfig",
    dependencies = {
      {
        "folke/lazydev.nvim",
        ft = "lua", -- only load on lua files
        opts = {
          library = {
            -- Load luvit types when the `vim.uv` word is found
            { path = "${3rd}/luv/library", words = { "vim%.uv" } },
          },
        },
      },
    },
  },

  -- Completion (blink.cmp; replaces nvim-cmp + cmp-* + vim-vsnip)
  {
    "saghen/blink.cmp",
    version = "1.*", -- a release tag pulls down the prebuilt fuzzy-matcher binary
    dependencies = { "rafamadriz/friendly-snippets" },
    opts = {
      keymap = { preset = "enter" }, -- <CR> accepts, like the old nvim-cmp mapping
      appearance = { nerd_font_variant = "mono" },
      completion = {
        documentation = { auto_show = true, auto_show_delay_ms = 200 },
        list = { selection = { preselect = true, auto_insert = false } },
      },
      sources = {
        default = { "lazydev", "lsp", "path", "snippets", "buffer" },
        providers = {
          lazydev = { name = "LazyDev", module = "lazydev.integrations.blink", score_offset = 100 },
        },
      },
      signature = { enabled = true },
      fuzzy = { implementation = "prefer_rust_with_warning" },
    },
  },

  -- Fuzzy finder
  {
    "https://github.com/nvim-telescope/telescope.nvim",
    dependencies = { "nvim-lua/plenary.nvim" },
  },

  -- File explorer (neo-tree; replaces NERDTree)
  {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    cmd = "Neotree",
    dependencies = {
      "nvim-lua/plenary.nvim",
      "MunifTanjim/nui.nvim",
      "nvim-tree/nvim-web-devicons",
    },
    opts = {
      close_if_last_window = true,
      filesystem = {
        follow_current_file = { enabled = true },
        use_libuv_file_watcher = true,
        filtered_items = {
          hide_dotfiles = false,
          hide_gitignored = false,
          never_show = { "__pycache__" },
          hide_by_pattern = { "*.pyc" },
        },
      },
      window = { width = 32 },
    },
  },

  -- Statusline
  {
    "nvim-lualine/lualine.nvim",
    dependencies = { "nvim-tree/nvim-web-devicons" },
    opts = {
      options = {
        theme = "auto",
        globalstatus = true,
        section_separators = "",
        component_separators = "",
      },
      sections = {
        lualine_c = { { "filename", path = 1 } }, -- show the relative path
      },
    },
  },

  -- Diagnostics / quickfix panel
  {
    "folke/trouble.nvim",
    cmd = "Trouble",
    opts = {},
    keys = {
      { "<leader>xx", "<cmd>Trouble diagnostics toggle<cr>", desc = "Diagnostics (Trouble)" },
      { "<leader>xX", "<cmd>Trouble diagnostics toggle filter.buf=0<cr>", desc = "Buffer Diagnostics (Trouble)" },
      { "<leader>xq", "<cmd>Trouble qflist toggle<cr>", desc = "Quickfix List (Trouble)" },
      { "<leader>xl", "<cmd>Trouble loclist toggle<cr>", desc = "Location List (Trouble)" },
    },
  },

  -- Search & replace
  {
    "https://github.com/nvim-pack/nvim-spectre",
    config = function()
      require("spectre").setup({
        default = {
          replace = {
            cmd = "oxi",
          },
        },
      })

      vim.keymap.set("n", "<leader>S", '<cmd>lua require("spectre").toggle()<CR>', {
        desc = "Toggle Spectre",
      })
      vim.keymap.set("n", "<m-f>", '<cmd>lua require("spectre").toggle()<CR>', {
        desc = "Toggle Spectre",
      })
      vim.keymap.set("n", "<leader>sw", '<cmd>lua require("spectre").open_visual({select_word=true})<CR>', {
        desc = "Search current word",
      })
      vim.keymap.set("v", "<leader>sw", '<esc><cmd>lua require("spectre").open_visual()<CR>', {
        desc = "Search current word",
      })
      vim.keymap.set("n", "<leader>sp", '<cmd>lua require("spectre").open_file_search({select_word=true})<CR>', {
        desc = "Search on current file",
      })
    end,
  },

  -- Formatting
  {
    "https://github.com/stevearc/conform.nvim",
    config = function()
      require("conform").setup()
    end,
  },

  -- Lean theorem prover
  {
    "Julian/lean.nvim",
    event = { "BufReadPre *.lean", "BufNewFile *.lean" },

    dependencies = {
      "neovim/nvim-lspconfig",
      "nvim-lua/plenary.nvim",
    },

    opts = {
      lsp = {},
      mappings = true,
    },
  },

  -- UI niceties
  { "https://github.com/stevearc/dressing.nvim", enabled = true },
  {
    "https://github.com/hedyhli/outline.nvim",
    init = function()
      require("outline").setup({
        outline_window = { auto_close = true },
      })
      vim.keymap.set("n", "<M-s>", "<cmd>Outline<CR>", { desc = "Toggle Outline" })
    end,
  },
  {
    "https://github.com/nvim-treesitter/nvim-treesitter-context",
    init = function()
      require("treesitter-context").setup({
        enable = true, -- Enable this plugin (Can be enabled/disabled later via commands)
        multiwindow = false, -- Enable multiwindow support.
        max_lines = 0, -- How many lines the window should span. Values <= 0 mean no limit.
        min_window_height = 0, -- Minimum editor window height to enable context. Values <= 0 mean no limit.
        line_numbers = true,
        multiline_threshold = 1, -- Maximum number of lines to show for a single context
        trim_scope = "outer", -- Which context lines to discard if `max_lines` is exceeded. Choices: 'inner', 'outer'
        mode = "cursor", -- Line used to calculate context. Choices: 'cursor', 'topline'
        -- Separator between context and content. Should be a single character string, like '-'.
        -- When separator is set, the context will only show up when there are at least 2 lines above cursorline.
        separator = nil,
        zindex = 20, -- The Z-index of the context window
        on_attach = nil, -- (fun(buf: integer): boolean) return false to disable attaching
      })
    end,
  },

  -- Disabled, but kept for the custom rainbow config (slows the UI when on)
  {
    "https://github.com/lukas-reineke/indent-blankline.nvim",
    enabled = false,
    config = function()
      local highlight = {
        "RainbowRed",
        "RainbowYellow",
        "RainbowBlue",
        "RainbowOrange",
        "RainbowGreen",
        "RainbowViolet",
        "RainbowCyan",
      }

      local hooks = require("ibl.hooks")
      -- create the highlight groups in the highlight setup hook, so they are reset
      -- every time the colorscheme changes
      hooks.register(hooks.type.HIGHLIGHT_SETUP, function()
        vim.api.nvim_set_hl(0, "RainbowRed", { fg = "#FFC8CE" })
        vim.api.nvim_set_hl(0, "RainbowYellow", { fg = "#FFEEBE" })
        vim.api.nvim_set_hl(0, "RainbowBlue", { fg = "#C0E5FF" })
        vim.api.nvim_set_hl(0, "RainbowOrange", { fg = "#FFE0C0" })
        vim.api.nvim_set_hl(0, "RainbowGreen", { fg = "#D9F5C8" })
        vim.api.nvim_set_hl(0, "RainbowViolet", { fg = "#F0D4FF" })
        vim.api.nvim_set_hl(0, "RainbowCyan", { fg = "#BEF5FA" })
      end)

      require("ibl").setup({ indent = { highlight = highlight } })
    end,
  },
}
