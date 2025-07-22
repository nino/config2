require("nvim-treesitter.configs").setup {
  ensure_installed = { "lua", "javascript", "typescript", "python", "html", "css", "astro" },
  highlight = { enable = true },
  incremental_selection = { enable = true },
  indent = { enable = true },
}
