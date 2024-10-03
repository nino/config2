(local util (require :fnlutils))

(fn exec [cmd]
  (let [handle (io.popen cmd)]
    (if handle
      (let [result (handle:read "*a")]
        (handle:close)
        result)
      "")))

(vim.keymap.set "n" "gu" (λ [] (vim.cmd (.. "!open " (util.current-WORD)))))

(vim.keymap.set "n" "<C-j>" vim.diagnostic.goto_next)
(vim.keymap.set "n" "<C-k>" vim.diagnostic.goto_prev)

(vim.api.nvim_create_autocmd "FileType"
  {:pattern  "cpp"
   :callback (fn []
               (set vim.bo.tabstop 4)
               (set vim.bo.softtabstop 4)
               (set vim.bo.shiftwidth 4)
               (set vim.bo.expandtab true))})

(vim.api.nvim_create_autocmd "FileType"
  {:pattern  "markdown"
   :callback (fn []
               (set vim.o.breakindentopt "shift:0"))})

{}
