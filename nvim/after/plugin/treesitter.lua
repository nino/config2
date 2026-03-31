vim.api.nvim_create_autocmd("FileType", {
  callback = function(args)
    local ft = vim.bo[args.buf].filetype
    if ft == "" then return end
    local lang = vim.treesitter.language.get_lang(ft)
    if lang and pcall(vim.treesitter.language.inspect, lang) then
      vim.treesitter.start(args.buf, lang)
      vim.wo.foldexpr = "v:lua.vim.treesitter.foldexpr()"
      vim.bo.indentexpr = "v:lua.require('nvim-treesitter.indent').get_indent(v:lnum)"
    end
  end,
})
