-- RGB: { red, green, blue }
local function rgb_diff(a, b)
  return math.sqrt((a.red - b.red) ^ 2 + (a.green - b.green) ^ 2 +
    (a.blue - b.blue) ^ 2)
end

local function hex_to_rgb(hex)
  local red = tonumber(string.sub(hex, 2, 3), 16)
  local green = tonumber(string.sub(hex, 4, 5), 16)
  local blue = tonumber(string.sub(hex, 6, 7), 16)

  return { red = red, green = green, blue = blue }
end

local function hex_diff(a, b) return rgb_diff(hex_to_rgb(a), hex_to_rgb(b)) end

local tailwind_colors = {
  ["Slate-50"] = "#f8fafc",
  ["Slate-100"] = "#f1f5f9",
  ["Slate-200"] = "#e2e8f0",
  ["Slate-300"] = "#cbd5e1",
  ["Slate-400"] = "#94a3b8",
  ["Slate-500"] = "#64748b",
  ["Slate-600"] = "#475569",
  ["Slate-700"] = "#334155",
  ["Slate-800"] = "#1e293b",
  ["Slate-900"] = "#0f172a",
  ["Gray-50"] = "#f9fafb",
  ["Gray-100"] = "#f3f4f6",
  ["Gray-200"] = "#e5e7eb",
  ["Gray-300"] = "#d1d5db",
  ["Gray-400"] = "#9ca3af",
  ["Gray-500"] = "#6b7280",
  ["Gray-600"] = "#4b5563",
  ["Gray-700"] = "#374151",
  ["Gray-800"] = "#1f2937",
  ["Gray-900"] = "#111827",
  ["Zinc-50"] = "#fafafa",
  ["Zinc-100"] = "#f4f4f5",
  ["Zinc-200"] = "#e4e4e7",
  ["Zinc-300"] = "#d4d4d8",
  ["Zinc-400"] = "#a1a1aa",
  ["Zinc-500"] = "#71717a",
  ["Zinc-600"] = "#52525b",
  ["Zinc-700"] = "#3f3f46",
  ["Zinc-800"] = "#27272a",
  ["Zinc-900"] = "#18181b",
  ["Neutral-50"] = "#fafafa",
  ["Neutral-100"] = "#f5f5f5",
  ["Neutral-200"] = "#e5e5e5",
  ["Neutral-300"] = "#d4d4d4",
  ["Neutral-400"] = "#a3a3a3",
  ["Neutral-500"] = "#737373",
  ["Neutral-600"] = "#525252",
  ["Neutral-700"] = "#404040",
  ["Neutral-800"] = "#262626",
  ["Neutral-900"] = "#171717",
  ["Stone-50"] = "#fafaf9",
  ["Stone-100"] = "#f5f5f4",
  ["Stone-200"] = "#e7e5e4",
  ["Stone-300"] = "#d6d3d1",
  ["Stone-400"] = "#a8a29e",
  ["Stone-500"] = "#78716c",
  ["Stone-600"] = "#57534e",
  ["Stone-700"] = "#44403c",
  ["Stone-800"] = "#292524",
  ["Stone-900"] = "#1c1917",
  ["Red-50"] = "#fef2f2",
  ["Red-100"] = "#fee2e2",
  ["Red-200"] = "#fecaca",
  ["Red-300"] = "#fca5a5",
  ["Red-400"] = "#f87171",
  ["Red-500"] = "#ef4444",
  ["Red-600"] = "#dc2626",
  ["Red-700"] = "#b91c1c",
  ["Red-800"] = "#991b1b",
  ["Red-900"] = "#7f1d1d",
  ["Orange-50"] = "#fff7ed",
  ["Orange-100"] = "#ffedd5",
  ["Orange-200"] = "#fed7aa",
  ["Orange-300"] = "#fdba74",
  ["Orange-400"] = "#fb923c",
  ["Orange-500"] = "#f97316",
  ["Orange-600"] = "#ea580c",
  ["Orange-700"] = "#c2410c",
  ["Orange-800"] = "#9a3412",
  ["Orange-900"] = "#7c2d12",
  ["Amber-50"] = "#fffbeb",
  ["Amber-100"] = "#fef3c7",
  ["Amber-200"] = "#fde68a",
  ["Amber-300"] = "#fcd34d",
  ["Amber-400"] = "#fbbf24",
  ["Amber-500"] = "#f59e0b",
  ["Amber-600"] = "#d97706",
  ["Amber-700"] = "#b45309",
  ["Amber-800"] = "#92400e",
  ["Amber-900"] = "#78350f",
  ["Yellow-50"] = "#fefce8",
  ["Yellow-100"] = "#fef9c3",
  ["Yellow-200"] = "#fef08a",
  ["Yellow-300"] = "#fde047",
  ["Yellow-400"] = "#facc15",
  ["Yellow-500"] = "#eab308",
  ["Yellow-600"] = "#ca8a04",
  ["Yellow-700"] = "#a16207",
  ["Yellow-800"] = "#854d0e",
  ["Yellow-900"] = "#713f12",
  ["Lime-50"] = "#f7fee7",
  ["Lime-100"] = "#ecfccb",
  ["Lime-200"] = "#d9f99d",
  ["Lime-300"] = "#bef264",
  ["Lime-400"] = "#a3e635",
  ["Lime-500"] = "#84cc16",
  ["Lime-600"] = "#65a30d",
  ["Lime-700"] = "#4d7c0f",
  ["Lime-800"] = "#3f6212",
  ["Lime-900"] = "#365314",
  ["Green-50"] = "#f0fdf4",
  ["Green-100"] = "#dcfce7",
  ["Green-200"] = "#bbf7d0",
  ["Green-300"] = "#86efac",
  ["Green-400"] = "#4ade80",
  ["Green-500"] = "#22c55e",
  ["Green-600"] = "#16a34a",
  ["Green-700"] = "#15803d",
  ["Green-800"] = "#166534",
  ["Green-900"] = "#14532d",
  ["Emerald-50"] = "#ecfdf5",
  ["Emerald-100"] = "#d1fae5",
  ["Emerald-200"] = "#a7f3d0",
  ["Emerald-300"] = "#6ee7b7",
  ["Emerald-400"] = "#34d399",
  ["Emerald-500"] = "#10b981",
  ["Emerald-600"] = "#059669",
  ["Emerald-700"] = "#047857",
  ["Emerald-800"] = "#065f46",
  ["Emerald-900"] = "#064e3b",
  ["Teal-50"] = "#f0fdfa",
  ["Teal-100"] = "#ccfbf1",
  ["Teal-200"] = "#99f6e4",
  ["Teal-300"] = "#5eead4",
  ["Teal-400"] = "#2dd4bf",
  ["Teal-500"] = "#14b8a6",
  ["Teal-600"] = "#0d9488",
  ["Teal-700"] = "#0f766e",
  ["Teal-800"] = "#115e59",
  ["Teal-900"] = "#134e4a",
  ["Cyan-50"] = "#ecfeff",
  ["Cyan-100"] = "#cffafe",
  ["Cyan-200"] = "#a5f3fc",
  ["Cyan-300"] = "#67e8f9",
  ["Cyan-400"] = "#22d3ee",
  ["Cyan-500"] = "#06b6d4",
  ["Cyan-600"] = "#0891b2",
  ["Cyan-700"] = "#0e7490",
  ["Cyan-800"] = "#155e75",
  ["Cyan-900"] = "#164e63",
  ["Sky-50"] = "#f0f9ff",
  ["Sky-100"] = "#e0f2fe",
  ["Sky-200"] = "#bae6fd",
  ["Sky-300"] = "#7dd3fc",
  ["Sky-400"] = "#38bdf8",
  ["Sky-500"] = "#0ea5e9",
  ["Sky-600"] = "#0284c7",
  ["Sky-700"] = "#0369a1",
  ["Sky-800"] = "#075985",
  ["Sky-900"] = "#0c4a6e",
  ["Blue-50"] = "#eff6ff",
  ["Blue-100"] = "#dbeafe",
  ["Blue-200"] = "#bfdbfe",
  ["Blue-300"] = "#93c5fd",
  ["Blue-400"] = "#60a5fa",
  ["Blue-500"] = "#3b82f6",
  ["Blue-600"] = "#2563eb",
  ["Blue-700"] = "#1d4ed8",
  ["Blue-800"] = "#1e40af",
  ["Blue-900"] = "#1e3a8a",
  ["Indigo-50"] = "#eef2ff",
  ["Indigo-100"] = "#e0e7ff",
  ["Indigo-200"] = "#c7d2fe",
  ["Indigo-300"] = "#a5b4fc",
  ["Indigo-400"] = "#818cf8",
  ["Indigo-500"] = "#6366f1",
  ["Indigo-600"] = "#4f46e5",
  ["Indigo-700"] = "#4338ca",
  ["Indigo-800"] = "#3730a3",
  ["Indigo-900"] = "#312e81",
  ["Violet-50"] = "#f5f3ff",
  ["Violet-100"] = "#ede9fe",
  ["Violet-200"] = "#ddd6fe",
  ["Violet-300"] = "#c4b5fd",
  ["Violet-400"] = "#a78bfa",
  ["Violet-500"] = "#8b5cf6",
  ["Violet-600"] = "#7c3aed",
  ["Violet-700"] = "#6d28d9",
  ["Violet-800"] = "#5b21b6",
  ["Violet-900"] = "#4c1d95",
  ["Purple-50"] = "#faf5ff",
  ["Purple-100"] = "#f3e8ff",
  ["Purple-200"] = "#e9d5ff",
  ["Purple-300"] = "#d8b4fe",
  ["Purple-400"] = "#c084fc",
  ["Purple-500"] = "#a855f7",
  ["Purple-600"] = "#9333ea",
  ["Purple-700"] = "#7e22ce",
  ["Purple-800"] = "#6b21a8",
  ["Purple-900"] = "#581c87",
  ["Fuchsia-50"] = "#fdf4ff",
  ["Fuchsia-100"] = "#fae8ff",
  ["Fuchsia-200"] = "#f5d0fe",
  ["Fuchsia-300"] = "#f0abfc",
  ["Fuchsia-400"] = "#e879f9",
  ["Fuchsia-500"] = "#d946ef",
  ["Fuchsia-600"] = "#c026d3",
  ["Fuchsia-700"] = "#a21caf",
  ["Fuchsia-800"] = "#86198f",
  ["Fuchsia-900"] = "#701a75",
  ["Pink-50"] = "#fdf2f8",
  ["Pink-100"] = "#fce7f3",
  ["Pink-200"] = "#fbcfe8",
  ["Pink-300"] = "#f9a8d4",
  ["Pink-400"] = "#f472b6",
  ["Pink-500"] = "#ec4899",
  ["Pink-600"] = "#db2777",
  ["Pink-700"] = "#be185d",
  ["Pink-800"] = "#9d174d",
  ["Pink-900"] = "#831843",
  ["Rose-50"] = "#fff1f2",
  ["Rose-100"] = "#ffe4e6",
  ["Rose-200"] = "#fecdd3",
  ["Rose-300"] = "#fda4af",
  ["Rose-400"] = "#fb7185",
  ["Rose-500"] = "#f43f5e",
  ["Rose-600"] = "#e11d48",
  ["Rose-700"] = "#be123c",
  ["Rose-800"] = "#9f1239",
  ["Rose-900"] = "#881337",
  White = "#FFFFFF",
  Black = "#000000"
}

local term_colors = {
  ["0"] = "#000000",
  ["1"] = "#800000",
  ["2"] = "#008000",
  ["3"] = "#808000",
  ["4"] = "#000080",
  ["5"] = "#800080",
  ["6"] = "#008080",
  ["7"] = "#c0c0c0",
  ["8"] = "#808080",
  ["9"] = "#ff0000",
  ["10"] = "#00ff00",
  ["11"] = "#ffff00",
  ["12"] = "#0000ff",
  ["13"] = "#ff00ff",
  ["14"] = "#00ffff",
  ["15"] = "#ffffff",
  ["16"] = "#000000",
  ["17"] = "#00005f",
  ["18"] = "#000087",
  ["19"] = "#0000af",
  ["20"] = "#0000d7",
  ["21"] = "#0000ff",
  ["22"] = "#005f00",
  ["23"] = "#005f5f",
  ["24"] = "#005f87",
  ["25"] = "#005faf",
  ["26"] = "#005fd7",
  ["27"] = "#005fff",
  ["28"] = "#008700",
  ["29"] = "#00875f",
  ["30"] = "#008787",
  ["31"] = "#0087af",
  ["32"] = "#0087d7",
  ["33"] = "#0087ff",
  ["34"] = "#00af00",
  ["35"] = "#00af5f",
  ["36"] = "#00af87",
  ["37"] = "#00afaf",
  ["38"] = "#00afd7",
  ["39"] = "#00afff",
  ["40"] = "#00d700",
  ["41"] = "#00d75f",
  ["42"] = "#00d787",
  ["43"] = "#00d7af",
  ["44"] = "#00d7d7",
  ["45"] = "#00d7ff",
  ["46"] = "#00ff00",
  ["47"] = "#00ff5f",
  ["48"] = "#00ff87",
  ["49"] = "#00ffaf",
  ["50"] = "#00ffd7",
  ["51"] = "#00ffff",
  ["52"] = "#5f0000",
  ["53"] = "#5f005f",
  ["54"] = "#5f0087",
  ["55"] = "#5f00af",
  ["56"] = "#5f00d7",
  ["57"] = "#5f00ff",
  ["58"] = "#5f5f00",
  ["59"] = "#5f5f5f",
  ["60"] = "#5f5f87",
  ["61"] = "#5f5faf",
  ["62"] = "#5f5fd7",
  ["63"] = "#5f5fff",
  ["64"] = "#5f8700",
  ["65"] = "#5f875f",
  ["66"] = "#5f8787",
  ["67"] = "#5f87af",
  ["68"] = "#5f87d7",
  ["69"] = "#5f87ff",
  ["70"] = "#5faf00",
  ["71"] = "#5faf5f",
  ["72"] = "#5faf87",
  ["73"] = "#5fafaf",
  ["74"] = "#5fafd7",
  ["75"] = "#5fafff",
  ["76"] = "#5fd700",
  ["77"] = "#5fd75f",
  ["78"] = "#5fd787",
  ["79"] = "#5fd7af",
  ["80"] = "#5fd7d7",
  ["81"] = "#5fd7ff",
  ["82"] = "#5fff00",
  ["83"] = "#5fff5f",
  ["84"] = "#5fff87",
  ["85"] = "#5fffaf",
  ["86"] = "#5fffd7",
  ["87"] = "#5fffff",
  ["88"] = "#870000",
  ["89"] = "#87005f",
  ["90"] = "#870087",
  ["91"] = "#8700af",
  ["92"] = "#8700d7",
  ["93"] = "#8700ff",
  ["94"] = "#875f00",
  ["95"] = "#875f5f",
  ["96"] = "#875f87",
  ["97"] = "#875faf",
  ["98"] = "#875fd7",
  ["99"] = "#875fff",
  ["100"] = "#878700",
  ["101"] = "#87875f",
  ["102"] = "#878787",
  ["103"] = "#8787af",
  ["104"] = "#8787d7",
  ["105"] = "#8787ff",
  ["106"] = "#87af00",
  ["107"] = "#87af5f",
  ["108"] = "#87af87",
  ["109"] = "#87afaf",
  ["110"] = "#87afd7",
  ["111"] = "#87afff",
  ["112"] = "#87d700",
  ["113"] = "#87d75f",
  ["114"] = "#87d787",
  ["115"] = "#87d7af",
  ["116"] = "#87d7d7",
  ["117"] = "#87d7ff",
  ["118"] = "#87ff00",
  ["119"] = "#87ff5f",
  ["120"] = "#87ff87",
  ["121"] = "#87ffaf",
  ["122"] = "#87ffd7",
  ["123"] = "#87ffff",
  ["124"] = "#af0000",
  ["125"] = "#af005f",
  ["126"] = "#af0087",
  ["127"] = "#af00af",
  ["128"] = "#af00d7",
  ["129"] = "#af00ff",
  ["130"] = "#af5f00",
  ["131"] = "#af5f5f",
  ["132"] = "#af5f87",
  ["133"] = "#af5faf",
  ["134"] = "#af5fd7",
  ["135"] = "#af5fff",
  ["136"] = "#af8700",
  ["137"] = "#af875f",
  ["138"] = "#af8787",
  ["139"] = "#af87af",
  ["140"] = "#af87d7",
  ["141"] = "#af87ff",
  ["142"] = "#afaf00",
  ["143"] = "#afaf5f",
  ["144"] = "#afaf87",
  ["145"] = "#afafaf",
  ["146"] = "#afafd7",
  ["147"] = "#afafff",
  ["148"] = "#afd700",
  ["149"] = "#afd75f",
  ["150"] = "#afd787",
  ["151"] = "#afd7af",
  ["152"] = "#afd7d7",
  ["153"] = "#afd7ff",
  ["154"] = "#afff00",
  ["155"] = "#afff5f",
  ["156"] = "#afff87",
  ["157"] = "#afffaf",
  ["158"] = "#afffd7",
  ["159"] = "#afffff",
  ["160"] = "#d70000",
  ["161"] = "#d7005f",
  ["162"] = "#d70087",
  ["163"] = "#d700af",
  ["164"] = "#d700d7",
  ["165"] = "#d700ff",
  ["166"] = "#d75f00",
  ["167"] = "#d75f5f",
  ["168"] = "#d75f87",
  ["169"] = "#d75faf",
  ["170"] = "#d75fd7",
  ["171"] = "#d75fff",
  ["172"] = "#d78700",
  ["173"] = "#d7875f",
  ["174"] = "#d78787",
  ["175"] = "#d787af",
  ["176"] = "#d787d7",
  ["177"] = "#d787ff",
  ["178"] = "#d7af00",
  ["179"] = "#d7af5f",
  ["180"] = "#d7af87",
  ["181"] = "#d7afaf",
  ["182"] = "#d7afd7",
  ["183"] = "#d7afff",
  ["184"] = "#d7d700",
  ["185"] = "#d7d75f",
  ["186"] = "#d7d787",
  ["187"] = "#d7d7af",
  ["188"] = "#d7d7d7",
  ["189"] = "#d7d7ff",
  ["190"] = "#d7ff00",
  ["191"] = "#d7ff5f",
  ["192"] = "#d7ff87",
  ["193"] = "#d7ffaf",
  ["194"] = "#d7ffd7",
  ["195"] = "#d7ffff",
  ["196"] = "#ff0000",
  ["197"] = "#ff005f",
  ["198"] = "#ff0087",
  ["199"] = "#ff00af",
  ["200"] = "#ff00d7",
  ["201"] = "#ff00ff",
  ["202"] = "#ff5f00",
  ["203"] = "#ff5f5f",
  ["204"] = "#ff5f87",
  ["205"] = "#ff5faf",
  ["206"] = "#ff5fd7",
  ["207"] = "#ff5fff",
  ["208"] = "#ff8700",
  ["209"] = "#ff875f",
  ["210"] = "#ff8787",
  ["211"] = "#ff87af",
  ["212"] = "#ff87d7",
  ["213"] = "#ff87ff",
  ["214"] = "#ffaf00",
  ["215"] = "#ffaf5f",
  ["216"] = "#ffaf87",
  ["217"] = "#ffafaf",
  ["218"] = "#ffafd7",
  ["219"] = "#ffafff",
  ["220"] = "#ffd700",
  ["221"] = "#ffd75f",
  ["222"] = "#ffd787",
  ["223"] = "#ffd7af",
  ["224"] = "#ffd7d7",
  ["225"] = "#ffd7ff",
  ["226"] = "#ffff00",
  ["227"] = "#ffff5f",
  ["228"] = "#ffff87",
  ["229"] = "#ffffaf",
  ["230"] = "#ffffd7",
  ["231"] = "#ffffff",
  ["232"] = "#080808",
  ["233"] = "#121212",
  ["234"] = "#1c1c1c",
  ["235"] = "#262626",
  ["236"] = "#303030",
  ["237"] = "#3a3a3a",
  ["238"] = "#444444",
  ["239"] = "#4e4e4e",
  ["240"] = "#585858",
  ["241"] = "#626262",
  ["242"] = "#6c6c6c",
  ["243"] = "#767676",
  ["244"] = "#808080",
  ["245"] = "#8a8a8a",
  ["246"] = "#949494",
  ["247"] = "#9e9e9e",
  ["248"] = "#a8a8a8",
  ["249"] = "#b2b2b2",
  ["250"] = "#bcbcbc",
  ["251"] = "#c6c6c6",
  ["252"] = "#d0d0d0",
  ["253"] = "#dadada",
  ["254"] = "#e4e4e4",
  ["255"] = "#eeeeee"
}

local function hex_color_to_term_color(hex_color)
  local closest = { color = "0", distance = 100000 }
  for termkey, termhex in pairs(term_colors) do
    local diff = hex_diff(termhex, hex_color)
    if diff <= closest.distance then
      closest.distance = diff
      closest.color = termkey
    end
  end

  return closest.color
end

local function tailwind_color_to_term_color(tw_color_name)
  local tw_color = tailwind_colors[tw_color_name]
  return hex_color_to_term_color(tw_color)
end

local function colorize(group, attrs)
  local cmd = "highlight " .. group
  if attrs.bg == "none" then
    cmd = cmd .. " ctermbg=none guibg=none"
  elseif attrs.bg then
    local ctermbg = tailwind_color_to_term_color(attrs.bg)
    local guibg = tailwind_colors[attrs.bg]
    cmd = cmd .. " ctermbg=" .. ctermbg .. " guibg=" .. guibg
  end

  if attrs.fg == "none" then
    cmd = cmd .. " ctermfg=none guifg=none"
  elseif attrs.fg then
    local ctermfg = tailwind_color_to_term_color(attrs.fg)
    local guifg = tailwind_colors[attrs.fg]
    cmd = cmd .. " ctermfg=" .. ctermfg .. " guifg=" .. guifg
  end

  if attrs.decoration then
    cmd = cmd .. " cterm=" .. attrs.decoration .. " gui=" ..
        attrs.decoration
  end

  vim.api.nvim_command(cmd)
end

colorize("Normal", { fg = "White" })

function rgb(r, g, b)
  return 16 + b + 6 * g + 36 * r
end

function gui_rgb(r, g, b)
  local r_hex = string.format("%x", math.floor(r / 6 * 256))
  local g_hex = string.format("%x", math.floor(g / 6 * 256))
  local b_hex = string.format("%x", math.floor(b / 6 * 256))
  return "#" .. r_hex .. g_hex .. b_hex
end

function grey(level)
  return 232 + level
end

-- vim.api.nvim_command("highlight Normal ctermbg=" .. rgb(1,0,0))

colorize("Cursor", { bg = "Pink-400" })
colorize("Visual", { bg = "Gray-700" })
colorize("ScrollBar", { bg = "Gray-800" })
colorize("ScrollBarHandle", { bg = "Gray-600" })
colorize("ScrollBarError", { bg = "Red-500", fg = "Red-500" })
colorize("ScrollBarErrorHandle", { bg = "Red-500", fg = "Red-500" })
-- colorize("LineNr", { fg = "Slate-600" })
colorize("NonText", { fg = "Slate-700" })

colorize("TabLineFill", { bg = "Gray-700", decoration = "none" })
colorize("TabLineSel", { bg = "Sky-800", fg = "White" })
colorize("TabLine", { bg = "Gray-600", fg = "Gray-200", decoration = "none" })

colorize("SpellBad", { bg = "Red-800", decoration = "none" })
colorize("SpellCap", { bg = "Orange-800" })

colorize("DiffText", { bg = "Emerald-900" })
colorize("DiffAdd", { bg = "Emerald-900" })
colorize("DiffChange", { bg = "Green-900" })
colorize("DiffDelete", { bg = "Rose-900" })

colorize("StatusLine", { bg = "Gray-600", fg = "White", decoration = "none" })
colorize("StatusLineNC", { fg = "Gray-600", bg = "Gray-200", decoration = "none" })
colorize('Pmenu', { bg = 'Pink-900', fg = "Gray-50" })
colorize('DiagnosticError', { fg = 'Red-300' })
colorize('DiagnosticVirtualTextError', { fg = 'Red-800' })
colorize('DiagnosticVirtualTextWarn', { fg = 'Yellow-600' })
colorize('DiagnosticVirtualTextHint', { fg = 'Gray-500' })

colorize("ColorColumn", { bg = "Gray-700" })
colorize("VertSplit", { bg = "none", fg = "Gray-600", decoration = "none" })
colorize("SignColumn", { bg = "Gray-700" })
colorize("CursorLine", { bg = "Gray-700" })

colorize("Statement", { fg = "Yellow-400", decoration = "none" })
colorize("Comment", { fg = "Lime-50", decoration = "bold" })
colorize("Special", { fg = "Green-200" }) -- Delimiters and special characters
colorize("Folded", { fg = "Sky-100", bg = "Slate-700" })
colorize("Identifier", { fg = "Pink-100" })
colorize("ocamlLabel", { fg = "Pink-400" })
colorize("typescriptParens", { fg = "Gray-200" })
colorize("DiagnosticUnderlineError", { bg = "Gray-700", decoration = "none" })
colorize("DiagnosticUnderlineHint", { bg = "Gray-500", decoration = "none" })
colorize("DiagnosticUnderlineWarn", { bg = "Gray-700", decoration = "none" })

colorize("CoqtailChecked", { bg = "Gray-800", decoration = "none" })
