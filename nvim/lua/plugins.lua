-- This file can be loaded by calling `lua require('plugins')` from your init.vim

-- Only required if you have packer configured as `opt`
vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function(use)
    use 'wbthomason/packer.nvim'
    use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }
    use 'https://github.com/tpope/vim-commentary'
    use 'mbbill/undotree'
    use 'tpope/vim-fugitive'
    use 'tpope/vim-rhubarb'
    use 'tpope/vim-surround'
    use 'editorconfig/editorconfig-vim'
    use 'tpope/vim-characterize'
    use 'github/copilot.vim'
    use 'rhysd/git-messenger.vim'
    use 'https://github.com/catppuccin/nvim'
    use {
        'VonHeikemen/lsp-zero.nvim',
        branch = 'v2.x',
        requires = {
            -- LSP Support
            {'neovim/nvim-lspconfig'},             -- Required
            {                                      -- Optional
                'williamboman/mason.nvim',
                run = function()
                    pcall(vim.cmd, 'MasonUpdate')
                end,
            },
            {'williamboman/mason-lspconfig.nvim'}, -- Optional

            -- Autocompletion
            {'hrsh7th/nvim-cmp'},     -- Required
            {'hrsh7th/cmp-nvim-lsp'}, -- Required
            {'hrsh7th/cmp-buffer'},
            {'L3MON4D3/LuaSnip'},     -- Required
        }
    }
    use {
        'https://github.com/nvim-telescope/telescope.nvim',
        requires = { {'nvim-lua/plenary.nvim'} }
    }
    use 'https://github.com/nvim-telescope/telescope-live-grep-args.nvim'
    use 'tpope/vim-repeat'
    use 'christoomey/vim-tmux-navigator'
    use 'https://github.com/ellisonleao/gruvbox.nvim'
    use 'preservim/nerdtree'
end)
