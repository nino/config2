-- This file can be loaded by calling `lua require('plugins')` from your init.vim

return {
  { "nvim-treesitter/nvim-treesitter", branch = "main", build = ":TSUpdate" },
  "mbbill/undotree",
  "tpope/vim-fugitive",
  "tpope/vim-rhubarb",
  -- Pure text-editing plugins: kept on under vscode-neovim (cond = true) since
  -- they enhance editing without duplicating any VS Code feature.
  { "tpope/vim-surround", cond = true },
  { "tpope/vim-characterize", cond = true },
  { "tpope/vim-repeat", cond = true },
  { "https://github.com/godlygeek/tabular", cond = true },
  "https://github.com/duane9/nvim-rg",
  { "https://github.com/wsdjeg/vim-fetch", cond = true }, -- Allow opening `path:linenr`
  "https://github.com/mfussenegger/nvim-lint",
  "https://github.com/NoahTheDuke/vim-just",
  "https://github.com/vlime/vlime",

  -- <C-h/j/k/l> moves between nvim splits and tmux panes alike.
  {
    "alexghergh/nvim-tmux-navigation",
    config = function()
      require("nvim-tmux-navigation").setup({
        keybindings = {
          left = "<C-h>",
          down = "<C-j>",
          up = "<C-k>",
          right = "<C-l>",
          last_active = "<C-\\>",
        },
      })

      local util = require("nvim-tmux-navigation.tmux_util")
      local tmux_socket = vim.fn.split(vim.env.TMUX or "", ",")[1]
      local tmux_dirs = { p = "l", h = "L", j = "D", k = "U", l = "R", n = "t:.+" }

      -- Patch short-circuit bug: the plugin calls is_tmux_pane_zoomed() (a shell
      -- fork) on every keypress even when disable_when_zoomed is false.
      local orig = util.should_tmux_control
      util.should_tmux_control = function(is_same_winnr, disable_nav_when_zoomed)
        if not disable_nav_when_zoomed then
          return is_same_winnr
        end
        return orig(is_same_winnr, disable_nav_when_zoomed)
      end

      -- Replace synchronous vim.fn.system() with async vim.system() and skip
      -- the intermediate shell by passing a list.
      util.tmux_change_pane = function(direction)
        if not tmux_socket then
          return
        end
        vim.system({ "tmux", "-S", tmux_socket, "select-pane", "-" .. tmux_dirs[direction] })
      end
    end,
  },

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
      keymap = {
        preset = "super-tab", -- <Tab> accepts, so <CR> stays a plain newline with the menu open
        -- false drops the key from blink's mappings, so it never maps ^K at
        -- all and digraph entry reads its two characters as it always did.
        ["<C-k>"] = false,
        ["<C-s>"] = { "show_signature", "hide_signature", "fallback" },
      },
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
      fuzzy = {
        implementation = "prefer_rust_with_warning",
        -- blink asks Neovim for *all* completions and does the filtering itself
        -- with a fuzzy score that penalises a case mismatch, so `:la<Tab>` gave
        -- `:labove` and pushed `Lazy` far down the list. Neovim's own ordering is
        -- already what we want -- case-insensitive, but an exact case match wins
        -- (`:la` -> Lazy, LazyDev, labove, ...; `:La` -> Lazy, LazyDev only) --
        -- so on the command line we rank by that order first and keep blink's
        -- score only as the tie-break for items Neovim did not return.
        sorts = function()
          if vim.fn.getcmdtype() == "" then
            return { "score", "sort_text" }
          end

          local rank = {}
          local query = vim.fn.getcmdline():sub(1, vim.fn.getcmdpos() - 1)
          local ok, native = pcall(vim.fn.getcompletion, query, "cmdline")
          if ok then
            for i, name in ipairs(native) do
              rank[name] = rank[name] or i
            end
          end

          return {
            function(a, b)
              local ra, rb = rank[a.label], rank[b.label]
              if ra and rb then
                if ra ~= rb then
                  return ra < rb
                end
                return nil
              end
              -- Anything Neovim itself offers beats anything it does not
              if ra ~= rb then
                return ra ~= nil
              end
              return nil
            end,
            "score",
            "sort_text",
          }
        end,
      },
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
    opts = function()
      -- High-contrast themes, one per background. The "auto" theme derives
      -- washed-out greys from lunaperche; spell the colours out so every
      -- section is legible.
      local dark_text = "#1c1c1c"
      local light_text = "#fafafa"
      local light_theme = {
        normal = {
          a = { fg = light_text, bg = "#005f87", gui = "bold" }, -- blue mode badge
          b = { fg = dark_text, bg = "#d0d0d0" }, -- branch/diagnostics
          c = { fg = dark_text, bg = "#e4e4e4" }, -- filename / fill
        },
        insert = { a = { fg = light_text, bg = "#5f8700", gui = "bold" } },
        visual = { a = { fg = light_text, bg = "#8700af", gui = "bold" } },
        replace = { a = { fg = light_text, bg = "#af0000", gui = "bold" } },
        command = { a = { fg = light_text, bg = "#af5f00", gui = "bold" } },
        inactive = {
          a = { fg = dark_text, bg = "#c6c6c6" },
          b = { fg = dark_text, bg = "#d0d0d0" },
          c = { fg = "#626262", bg = "#e4e4e4" },
        },
      }
      -- The light sections are near-white, which glares on a dark background,
      -- so the dark variant darkens the bar and puts dark text on lighter,
      -- less saturated mode badges.
      local dark_theme = {
        normal = {
          a = { fg = dark_text, bg = "#5fafd7", gui = "bold" }, -- blue mode badge
          b = { fg = "#d0d0d0", bg = "#3a3a3a" }, -- branch/diagnostics
          c = { fg = "#c6c6c6", bg = "#2c2c2c" }, -- filename / fill
        },
        insert = { a = { fg = dark_text, bg = "#87af5f", gui = "bold" } },
        visual = { a = { fg = dark_text, bg = "#af87d7", gui = "bold" } },
        replace = { a = { fg = light_text, bg = "#d75f5f", gui = "bold" } },
        command = { a = { fg = dark_text, bg = "#d7875f", gui = "bold" } },
        inactive = {
          a = { fg = "#9e9e9e", bg = "#303030" },
          b = { fg = "#9e9e9e", bg = "#303030" },
          c = { fg = "#767676", bg = "#262626" },
        },
      }
      -- <col>:<line>/<total> for the window the status line belongs to.
      local function position()
        local pos = vim.api.nvim_win_get_cursor(0)
        return string.format("%d:%d/%d", pos[2] + 1, pos[1], vim.api.nvim_buf_line_count(0))
      end

      return {
        options = {
          -- lualine re-runs `setup()` on ColorScheme and on `background`
          -- changes, and calls a function theme again each time, so the bar
          -- follows the macOS appearance check in after/plugin/colors.lua.
          theme = function()
            return vim.o.background == "dark" and dark_theme or light_theme
          end,
          -- One status line per window, each reporting its own buffer. Under
          -- `globalstatus` lualine renders a single line from the focused
          -- window; laststatus is 2 (init.lua), so every split drew that same
          -- line and described the wrong buffer.
          globalstatus = false,
          section_separators = "",
          component_separators = "",
        },
        sections = {
          -- Single-character mode indicator (N/I/V/C/R/…).
          lualine_a = {
            {
              "mode",
              fmt = function(str)
                return str:sub(1, 1)
              end,
            },
          },
          -- Trim long branch names so they don't dominate the bar.
          lualine_b = {
            {
              "branch",
              fmt = function(name)
                return #name > 12 and name:sub(1, 12) .. "…" or name
              end,
            },
            "diff",
            "diagnostics",
          },
          lualine_c = { { "filename", path = 1 } }, -- show the relative path
          -- Drop "encoding" (utf-8), "fileformat" (the OS logo) and "filetype".
          lualine_x = {},
          -- Replace the default "line:col" location with <col>-<line>/<total>.
          lualine_z = { position },
        },
        -- Unfocused splits: same components, minus the mode badge and the
        -- git/diagnostics section, which only concern the focused window.
        inactive_sections = {
          lualine_a = {},
          lualine_b = {},
          lualine_c = { { "filename", path = 1 } },
          lualine_x = {},
          lualine_y = {},
          lualine_z = { position },
        },
        -- Unfocused splits: just their own relative path, in the dimmed
        -- "inactive" colours.
        inactive_sections = {
          lualine_a = {},
          lualine_b = {},
          lualine_c = { { "filename", path = 1 } },
          lualine_x = {},
          lualine_y = {},
          lualine_z = {},
        },
      }
    end,
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
  -- Renders markdown in the buffer: headings, tables, code blocks, list
  -- bullets, checkboxes. Anti-conceal shows the raw text on the cursor line.
  -- The nino colorscheme already styles RenderMarkdownCode/CodeInline.
  {
    "MeanderingProgrammer/render-markdown.nvim",
    ft = { "markdown" },
    dependencies = { "nvim-tree/nvim-web-devicons" },
    opts = {
      -- Default drops the whole buffer back to raw text in insert mode. Add
      -- "i" so it stays rendered while typing; anti-conceal (on by default)
      -- still un-renders just the cursor line, which is the line being
      -- edited. blink.cmp draws its own popup, so mode() stays "i" while
      -- completing and the buffer does not flicker.
      render_modes = { "n", "c", "t", "i" },
      -- LaTeX rendering needs a `latex2text`/`utftex` binary and the latex
      -- parser, neither of which is installed; leaving it on only warns.
      latex = { enabled = false },
    },
  },
  {
    -- Scrollbar on the right edge, with marks for diagnostics/search/marks.
    -- Off under vscode-neovim, which has its own scrollbar.
    "https://github.com/dstein64/nvim-scrollview",
    opts = {
      signs_on_startup = { "diagnostics", "search", "marks", "quickfix" },
      excluded_filetypes = { "neo-tree", "trouble", "Outline" },
      current_only = true, -- only the focused window gets a bar
    },
  },
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
