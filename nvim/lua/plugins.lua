-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]
local packer = require('packer')
packer.init({
  git = {
    clone_timeout = 600, -- Timeout, in seconds, for git clones
  },
})

return packer.startup(function(use)
  use 'wbthomason/packer.nvim'
  use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }
  use 'https://github.com/tpope/vim-commentary'
  use 'mbbill/undotree'
  use 'tpope/vim-fugitive'
  use 'tpope/vim-rhubarb'
  use 'tpope/vim-surround'
  use 'editorconfig/editorconfig-vim'
  use 'tpope/vim-characterize'
  -- use 'github/copilot.vim'
  use 'rhysd/git-messenger.vim'
  use {
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
  }
  use {
    'https://github.com/nvim-telescope/telescope.nvim',
    requires = { { 'nvim-lua/plenary.nvim' } }
  }
  use 'https://github.com/nvim-telescope/telescope-live-grep-args.nvim'
  use 'tpope/vim-repeat'
  use 'christoomey/vim-tmux-navigator'
  use 'preservim/nerdtree'
  -- use 'https://github.com/vantaboard/sqlfluff.nvim'
  use 'https://github.com/JuliaEditorSupport/julia-vim'
  use 'https://github.com/leafOfTree/vim-svelte-plugin'
  use 'https://github.com/gleam-lang/gleam.vim'
  use 'https://github.com/godlygeek/tabular'
  use 'https://github.com/elixir-tools/elixir-tools.nvim'
  use 'elixir-editors/vim-elixir'
  use 'https://github.com/guns/vim-sexp'
  use 'https://github.com/tpope/vim-sexp-mappings-for-regular-people'
  use 'https://github.com/duane9/nvim-rg'
  use 'https://github.com/kaarmu/typst.vim'
  use 'https://github.com/dstein64/nvim-scrollview'

  -- DAP
  use 'https://github.com/mfussenegger/nvim-dap'
  use 'https://github.com/mxsdev/nvim-dap-vscode-js'
  use 'https://github.com/leoluz/nvim-dap-go'
  use { 'https://github.com/rcarriga/nvim-dap-ui', requires = { "nvim-neotest/nvim-nio" } }
  use 'https://github.com/theHamsta/nvim-dap-virtual-text'
  use 'https://github.com/nvim-telescope/telescope-dap.nvim'
  use 'https://github.com/mfussenegger/nvim-dap-python'

  use 'https://github.com/wsdjeg/vim-fetch'  -- Allow opening `path:linenr`
  use 'https://github.com/Vigemus/iron.nvim' -- REPLs
  use 'https://github.com/prisma/vim-prisma'
  use 'https://github.com/simrat39/symbols-outline.nvim'
  use 'https://github.com/mfussenegger/nvim-lint'
  use 'https://github.com/NoahTheDuke/vim-just'
  use 'https://github.com/lukas-reineke/indent-blankline.nvim'
  use 'https://github.com/ellisonleao/gruvbox.nvim'
  use 'https://github.com/chrisbra/vim-diff-enhanced'
  use { 'https://github.com/chomosuke/typst-preview.nvim',
    tag = 'v0.1.*',
    run = function() require 'typst-preview'.update() end,
  }
  use({
    "https://github.com/stevearc/conform.nvim",
    config = function()
      require("conform").setup()
    end,
  })
  -- use 'https://github.com/folke/tokyonight.nvim'
  -- use 'https://github.com/Shatur/neovim-ayu'
  -- use 'https://github.com/RRethy/base16-nvim'
  use 'https://github.com/blumaa/ohne-accidents.nvim'
  use 'https://github.com/sputnick1124/uiua.vim'
  use 'https://github.com/Olical/nfnl'
  use { 'https://github.com/stevearc/oil.nvim',
    config = function()
      require('oil').setup()
    end }
end)
