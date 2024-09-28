(fn current-word [] (vim.fn.expand "<cword>"))

(fn exec [cmd]
  (let [handle (io.popen cmd)]
    (if handle
      (let [result (handle:read "*a")]
        (handle:close)
        result)
      "")))

(vim.keymap.set "n" "gu" (λ [] (exec (.. "open '" (current-word) "'"))))


(vim.api.nvim_create_autocmd "FileType"
  {:pattern "cpp"
   :callback (fn []
               (set vim.bo.tabstop 4)
               (set vim.bo.softtabstop 4)
               (set vim.bo.shiftwidth 4)
               (set vim.bo.expandtab true))})
