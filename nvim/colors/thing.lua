local utils = require("utils")

utils.colorize("Identifier", { fg = utils.rgb(1, 4, 5) })
utils.colorize("Comment", { fg = utils.basic(7) })

utils.colorize("Normal", { fg = utils.basic(15) })

utils.colorize("DiffText", { bg = utils.rgb(0, 1, 3) })
utils.colorize("DiffAdd", { bg = utils.rgb(0, 1, 3) })
utils.colorize("DiffChange", { bg = utils.grey(4) })
utils.colorize("DiffDelete", { bg = utils.rgb(2, 0, 1) })
utils.colorize("Pmenu", { bg = utils.grey(4), fg = utils.grey(20) })

utils.colorize("CoqtailChecked", { bg = utils.grey(4), decoration = "none" })
