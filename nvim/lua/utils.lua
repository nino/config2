local mod = {}

function mod.color(colorscheme)
    vim.cmd("color " .. colorscheme)
end

return mod
