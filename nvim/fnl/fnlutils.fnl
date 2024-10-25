(fn current-word [] (vim.fn.expand "<cword>"))
(fn current-WORD [] (vim.fn.expand "<cWORD>"))

(fn diagnostic-sign []
  (let [diagnostics (vim.diagnostic.get 0)
        total (length diagnostics)
        ;; Count errors (severity 1) using accumulator
        errors (accumulate [count 0
                            _ msg (pairs diagnostics)]
                           (if (= msg.severity 1)
                             (+ count 1)
                             count))]
    ;; Return appropriate symbol based on counts
    (if (= total 0)
      "♥︎"
      (if (= errors 0)
        "⊙"
        "×"))))

{:current-word    current-word
 :current-WORD    current-WORD
 :diagnostic-sign diagnostic-sign}
