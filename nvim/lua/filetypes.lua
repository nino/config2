vim.keymap.set("n", "gu", function()
  vim.cmd("!open " .. vim.fn.expand("<cWORD>"))
end)

local cpp_indent = tonumber(os.getenv("CPP_INDENT")) or 4

vim.api.nvim_create_autocmd("FileType", {
  pattern = "cpp",
  callback = function()
    vim.bo.tabstop = cpp_indent
    vim.bo.softtabstop = cpp_indent
    vim.bo.shiftwidth = cpp_indent
    vim.bo.expandtab = true
  end,
})

vim.api.nvim_create_autocmd("FileType", {
  pattern = "markdown",
  callback = function()
    vim.o.breakindentopt = "shift:0"
    vim.bo.smartindent = false
    vim.bo.cindent = false
  end,
})

vim.api.nvim_create_autocmd("FileType", {
  pattern = "gitcommit",
  callback = function()
    vim.o.breakindentopt = "shift:0"
    vim.bo.smartindent = false
    vim.bo.cindent = false
  end,
})

vim.api.nvim_create_autocmd("FileType", {
  pattern = "gdscript",
  callback = function()
    vim.bo.tabstop = 4
    vim.bo.shiftwidth = 4
    vim.bo.expandtab = false
  end,
})
