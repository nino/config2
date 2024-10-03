(fn current-word [] (vim.fn.expand "<cword>"))
(fn current-WORD [] (vim.fn.expand "<cWORD>"))

{:current-word current-word
 :current-WORD current-WORD}
