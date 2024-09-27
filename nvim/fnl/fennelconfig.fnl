(fn current-word [] (vim.fn.expand "<cword>"))

(fn exec [cmd]
  (let [handle (io.popen cmd)]
    (if handle
      (let [result (handle:read "*a")]
        (handle:close)
        result)
      "")))

(vim.keymap.set "n" "gu" (λ [] (exec (.. "open '" (current-word) "'"))))
