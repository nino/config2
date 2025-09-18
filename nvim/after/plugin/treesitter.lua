require("nvim-treesitter.configs").setup {
  -- ensure_installed = { "lua", "javascript", "typescript", "python", "html", "css", "astro" },
  highlight = { enable = true },
  incremental_selection = { enable = true },
  indent = { enable = true },
  config = function()
    vim.api.nvim_create_autocmd('FileType', {
      pattern = { "javascript", "javascriptreact", "typescript", "typescriptreact" },
      callback = function()
        vim.treesitter.start()
        vim.wo.foldexpr = 'v:lua.vim.treesitter.foldexpr()'
        vim.bo.indentexpr =
        'v:lua.require\'nvim-treesitter\'.indentexpr()'
      end,
    })
  end
}
