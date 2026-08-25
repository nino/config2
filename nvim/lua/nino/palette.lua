--- Colours for the `nino` colourscheme.
---
--- Each colour holds a true-colour value and a 256-colour terminal fallback,
--- because the scheme must work in a plain terminal and in a GUI.
--- Use "NONE" to keep the terminal (or GUI) default.

--- @class Colour
--- @field gui string Hex value, colour name, or "NONE"
--- @field cterm string|integer Colour index, colour name, or "NONE"

--- @param gui string
--- @param cterm string|integer
--- @return Colour
local function colour(gui, cterm)
  return { gui = gui, cterm = cterm }
end

local NONE = colour("NONE", "NONE")

--- Colours that are the same in the light and the dark variant.
local common = {
  none = NONE,
  punctuation = colour("#888888", 244),
  unnecessary = colour("grey", 244),
  cursearch_bg = colour("#3388CC", 68),
  special_char = colour("#5555FF", 63),
  status_fg = colour("white", "white"),
  error = colour("#FF6666", 204),
  warn = colour("#FFDD66", 221),
  info = colour("#88DDFF", 117),
  hint = colour("#AAEEBB", 157),
}

--- @class Palette
--- @field none Colour Transparent: use the terminal default
--- @field string Colour
--- @field constant Colour
--- @field func Colour
--- @field keyword_control Colour `return` and `throw`
--- @field punctuation Colour
--- @field unnecessary Colour Code that the language server reports as unused
--- @field comment_fg Colour
--- @field comment_bg Colour
--- @field special_char Colour
--- @field float_bg Colour Floating windows, menus, and the cursor column
--- @field code_bg Colour Code blocks in rendered markdown
--- @field select_bg Colour Menu selection and search matches
--- @field cursearch_bg Colour The search match under the cursor
--- @field visual_bg Colour
--- @field cursorline_bg Colour
--- @field status_bg Colour Status line and tab line of the current window
--- @field status_fg Colour
--- @field status_nc_bg Colour Status line and tab line of the other windows
--- @field status_nc_fg Colour
--- @field scrollbar_bg Colour The scrollbar on the right edge of a window
--- @field error Colour
--- @field warn Colour
--- @field info Colour
--- @field hint Colour
--- @field diff_add Colour
--- @field diff_delete Colour
--- @field diff_change Colour
--- @field diff_text Colour

--- @type Palette
local light = vim.tbl_extend("error", common, {
  string = colour("#009944", "darkgreen"),
  constant = colour("#BB5500", 130),
  func = colour("#6600CC", 54),
  keyword_control = colour("#C64690", 205),
  comment_fg = colour("#444400", 58),
  comment_bg = colour("#FFFFEA", 230),
  float_bg = colour("#EEEEEE", 255),
  code_bg = colour("#EEEEEE", 255),
  select_bg = colour("#AADDFF", 153),
  visual_bg = colour("#FFFF00", 226),
  cursorline_bg = colour("#F2F2F2", "NONE"),
  status_bg = colour("#777777", 243),
  status_nc_bg = colour("#DDDDDD", 253),
  status_nc_fg = colour("#555555", 240),
  scrollbar_bg = colour("#CCCCCC", 252),
  diff_add = colour("#EAFFDC", 157),
  diff_delete = colour("#F9DDDD", 224),
  diff_change = colour("#EEEEFF", 189),
  diff_text = colour("#DDFCFA", "NONE"),
})

--- @type Palette
local dark = vim.tbl_extend("error", common, {
  string = colour("#66DD88", "lightgreen"),
  constant = colour("#FFAA66", 216),
  func = colour("#BB88FF", 141),
  keyword_control = colour("#FF66AA", 205),
  comment_fg = colour("#AAAA66", 143),
  comment_bg = colour("#222200", 234),
  float_bg = colour("#222222", 235),
  code_bg = colour("#333333", 236),
  select_bg = colour("#005588", 24),
  visual_bg = colour("#555500", 58),
  cursorline_bg = NONE,
  status_bg = colour("#666666", 242),
  status_nc_bg = colour("#444444", 238),
  status_nc_fg = colour("#AAAAAA", 248),
  scrollbar_bg = colour("#444444", 238),
  diff_add = colour("#223322", 22),
  diff_delete = colour("#442222", 52),
  diff_change = colour("#222244", 235),
  diff_text = colour("#224455", "NONE"),
})

--- The colour of the cursor itself. It does not change with the background.
local cursor = "#FF00EE"

return { light = light, dark = dark, cursor = cursor }
