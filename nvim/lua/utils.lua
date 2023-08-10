local mod = {}

--- @param c string
--- @return integer
function mod.utf8_to_unicode_codepoint(c)
    local b1, b2, b3, b4 = c:byte(1, -1)
    local codepoint --- @type integer
    if b1 < 0x80 then
        codepoint = b1
    elseif b1 < 0xE0 then
        codepoint = (b1 - 0xC0) * 0x40 + b2 - 0x80
    elseif b1 < 0xF0 then
        codepoint = (b1 - 0xE0) * 0x1000 + (b2 - 0x80) * 0x40 + b3 - 0x80
    else
        codepoint = (b1 - 0xF0) * 0x40000 + (b2 - 0x80) * 0x1000 + (b3 - 0x80) * 0x40 + b4 - 0x80
    end
    return codepoint
end

--- @param keys string
--- @param char string
--- @return nil
function mod.set_digraph(keys, char)
    vim.cmd("digraph " .. keys .. " " .. mod.utf8_to_unicode_codepoint(char))
end

return mod
