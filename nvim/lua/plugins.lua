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
    use 'github/copilot.vim'
    use 'rhysd/git-messenger.vim'
    use 'https://github.com/catppuccin/nvim'
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
    use 'https://github.com/morhetz/gruvbox'
    use 'https://github.com/justin2004/vim-apl'
    use 'Julian/lean.nvim'
    use 'https://github.com/vantaboard/sqlfluff.nvim'
    use 'bdesham/biogoo'
    use 'https://github.com/Shatur/neovim-ayu'
    use 'https://github.com/JuliaEditorSupport/julia-vim'
    use { 'https://github.com/mlochbaum/BQN', rtp = 'editors/vim' }
    use 'https://github.com/leafOfTree/vim-svelte-plugin'
    use 'https://github.com/agude/vim-eldar'
    use 'https://github.com/RRethy/nvim-base16'
    use 'https://github.com/ishan9299/modus-theme-vim'
    use { 'unisonweb/unison', branch = 'trunk', rtp = 'editor-support/vim' }
    use 'https://github.com/ChrisWellsWood/roc.vim'
    use 'https://github.com/gleam-lang/gleam.vim'
    use 'https://github.com/MrcJkb/haskell-tools.nvim'
    use 'https://github.com/kblin/vim-fountain'
    use 'https://github.com/godlygeek/tabular'
    -- use 'https://github.com/sourcegraph/sg.nvim'
    use 'https://github.com/elixir-tools/elixir-tools.nvim'
    use 'elixir-editors/vim-elixir'
    use 'https://github.com/ellisonleao/gruvbox.nvim'
    use 'https://github.com/guns/vim-sexp'
    use 'https://github.com/tpope/vim-sexp-mappings-for-regular-people'
    use 'https://github.com/folke/tokyonight.nvim'
    use 'https://github.com/rebelot/kanagawa.nvim'
    use 'https://github.com/jacoborus/tender.vim'
    use 'https://github.com/AlexvZyl/nordic.nvim'
    use 'https://github.com/ray-x/aurora'
    use 'https://github.com/uloco/bluloco.nvim'
    use 'https://github.com/kartikp10/noctis.nvim'
    use 'https://github.com/lalitmee/cobalt2.nvim'
    use 'https://github.com/rktjmp/lush.nvim'
    use 'https://github.com/metalelf0/jellybeans-nvim'
    use 'https://github.com/sainnhe/sonokai'
    use 'https://github.com/jaredgorski/SpaceCamp'
    use 'https://github.com/qualiabyte/vim-colorstepper'
    use 'https://github.com/duane9/nvim-rg'
    use 'https://github.com/kaarmu/typst.vim'
    -- use 'https://github.com/mfussenegger/nvim-dap'
    -- use 'https://github.com/mxsdev/nvim-dap-vscode-js'
    -- use {
    --     "microsoft/vscode-js-debug",
    --     opt = true,
    --     run = "npm install --legacy-peer-deps && npx gulp vsDebugServerBundle && mv dist out"
    -- }
    use 'https://github.com/wsdjeg/vim-fetch'
    use 'https://github.com/Vigemus/iron.nvim'
end)
