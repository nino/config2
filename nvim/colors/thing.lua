local utils = require("utils")

utils.colorize("Identifier", { fg = utils.rgb(1, 4, 5) })
utils.colorize("Comment", { fg = utils.basic(7) })
utils.colorize("Constant", { fg = utils.rgb(3, 5, 4) })

utils.colorize("Normal", { fg = utils.basic(15) })

utils.colorize("DiffText", { bg = utils.rgb(0, 1, 3) })
utils.colorize("DiffAdd", { bg = utils.rgb(0, 1, 3) })
utils.colorize("DiffChange", { bg = utils.grey(4) })
utils.colorize("DiffDelete", { bg = utils.rgb(2, 0, 1) })
utils.colorize("Pmenu", { bg = utils.grey(4), fg = utils.grey(20) })

utils.colorize("DiagnosticUnderlineError", { bg = utils.rgb(1, 0, 0), decoration = "none" })
utils.colorize("DiagnosticUnderlineInfo", { bg = utils.grey(5), decoration = "none" })
utils.colorize("DiagnosticUnderlineHint", { bg = utils.grey(4), decoration = "none" })
utils.colorize("DiagnosticUnderlineWarn", { bg = utils.grey(5), decoration = "none" })

utils.colorize("CoqtailChecked", { bg = utils.grey(4), decoration = "none" })
