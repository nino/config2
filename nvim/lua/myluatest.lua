local api = vim.api

local mod = {}

api.nvim_command('echo "hello"')
vim.wo.number = false

return mod
