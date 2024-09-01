-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
-- vim.cmd [[packadd packer.nvim]]
-- local packer = require('packer')
-- packer.init({
--   git = {
--     clone_timeout = 600, -- Timeout, in seconds, for git clones
--   },
-- })
--
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
  'https://github.com/github/copilot.vim',
  'neovim/nvim-lspconfig',
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
  'tpope/vim-repeat',
  'christoomey/vim-tmux-navigator',
  'preservim/nerdtree',
  'https://github.com/JuliaEditorSupport/julia-vim',
  'https://github.com/leafOfTree/vim-svelte-plugin',
  'https://github.com/gleam-lang/gleam.vim',
  'https://github.com/godlygeek/tabular',
  'https://github.com/elixir-tools/elixir-tools.nvim',
  'elixir-editors/vim-elixir',
  'https://github.com/guns/vim-sexp',
  'https://github.com/tpope/vim-sexp-mappings-for-regular-people',
  'https://github.com/duane9/nvim-rg',
  'https://github.com/kaarmu/typst.vim',
  'https://github.com/dstein64/nvim-scrollview',

  -- DAP
  'https://github.com/mfussenegger/nvim-dap',
  'https://github.com/mxsdev/nvim-dap-vscode-js',
  'https://github.com/leoluz/nvim-dap-go',
  "nvim-neotest/nvim-nio",
  { 'https://github.com/rcarriga/nvim-dap-ui', requires = { "nvim-neotest/nvim-nio" } },
  'https://github.com/theHamsta/nvim-dap-virtual-text',
  'https://github.com/nvim-telescope/telescope-dap.nvim',
  'https://github.com/mfussenegger/nvim-dap-python',

  'https://github.com/wsdjeg/vim-fetch',  -- Allow opening `path:linenr`
  'https://github.com/Vigemus/iron.nvim', -- REPLs
  'https://github.com/prisma/vim-prisma',
  'https://github.com/simrat39/symbols-outline.nvim',
  'https://github.com/mfussenegger/nvim-lint',
  'https://github.com/NoahTheDuke/vim-just',
  'https://github.com/lukas-reineke/indent-blankline.nvim',
  'https://github.com/chrisbra/vim-diff-enhanced',
  ({
    "https://github.com/stevearc/conform.nvim",
    config = function()
      require("conform").setup()
    end,
  }),
  'https://github.com/blumaa/ohne-accidents.nvim',
  'https://github.com/sputnick1124/uiua.vim',
  'https://github.com/Olical/nfnl',
  {
    'https://github.com/stevearc/oil.nvim',
    config = function()
      require('oil').setup()
    end
  },
  {
    'https://github.com/lewis6991/gitsigns.nvim',
    config = function()
      require('gitsigns').setup()
    end
  },
  'https://github.com/nvim-pack/nvim-spectre',
  'https://github.com/sourcegraph/sg.nvim',
  {
    "julianolf/nvim-dap-lldb",
    dependencies = { "mfussenegger/nvim-dap" },
    opts = {
      codelldb_path = "~/.local/share/nvim/mason/bin/codelldb"
    },
  },
  'https://github.com/catppuccin/nvim',
  'https://github.com/Shatur/neovim-ayu',
  'https://github.com/uloco/bluloco.nvim',
  'https://github.com/cweagans/vim-taskpaper',
}
