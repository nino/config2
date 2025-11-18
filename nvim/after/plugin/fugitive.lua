-- Configure fugitive status window size
vim.api.nvim_create_autocmd("FileType", {
  pattern = "fugitive",
  callback = function()
    local total_height = vim.o.lines
    local height = math.min(14, math.floor(total_height * 0.3))
    vim.cmd("resize " .. height)
  end,
})
