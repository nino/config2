local mod = {}

function mod.color(colorscheme)
    vim.cmd("color " .. colorscheme)
end


---@alias color
---| { rgb: { r: integer, g: integer, b: integer } }
---| { grey: integer }
---| { basic: integer }

---@param color color
---@return integer
function mod.ctermcolor(color)
  if color.rgb then
    return 16 + color.rgb.b + 6 * color.rgb.g + 36 * color.rgb.r
  elseif color['grey'] then
    return 232 + color['grey']
  else
    return color['basic']
  end
end

---@param r integer
---@param g integer
---@param b integer
---@return color
function mod.rgb(r, g, b)
  return { rgb = { r = r, g = g, b = b } }
end

---@param level integer
---@return color
function mod.grey(level)
  return { grey = level }
end

---@param level integer
---@return color
function mod.basic(level)
  return { basic = level }
end

-- function mod.gui_rgb(r, g, b)
--   local r_hex = string.format("%x", math.floor(r / 6 * 256))
--   local g_hex = string.format("%x", math.floor(g / 6 * 256))
--   local b_hex = string.format("%x", math.floor(b / 6 * 256))
--   return "#" .. r_hex .. g_hex .. b_hex
-- end

---@param group string
---@param attrs { fg?: color, bg?: color, decoration?: string }
function mod.colorize(group, attrs)
  local cmd = "highlight " .. group
  if attrs.bg == "none" then
    cmd = cmd .. " ctermbg=none guibg=none"
  elseif attrs.bg then
    local ctermbg = mod.ctermcolor(attrs.bg)
    -- local guibg = mod.guicolor[attrs.bg]
    cmd = cmd .. " ctermbg=" .. ctermbg -- .. " guibg=" .. guibg
  end

  if attrs.fg == "none" then
    cmd = cmd .. " ctermfg=none guifg=none"
  elseif attrs.fg then
    local ctermfg = mod.ctermcolor(attrs.fg)
    -- local guifg = mod.guicolor[attrs.fg]
    cmd = cmd .. " ctermfg=" .. ctermfg --  .. " guifg=" .. guifg
  end

  if attrs.decoration then
    cmd = cmd .. " cterm=" .. attrs.decoration .. " gui=" ..
        attrs.decoration
  end

  vim.api.nvim_command(cmd)
end

return mod
