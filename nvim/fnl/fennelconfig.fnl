(local util (require :fnlutils))

; (set vim.g.conjure_filetypes ["fennel" "clojure"])
(set vim.g.conjure#filetype#fennel "conjure.client.fennel.nfnl")

(fn exec [cmd]
  (let [handle (io.popen cmd)]
    (if handle
      (let [result (handle:read "*a")]
        (handle:close)
        result)
      "")))

(vim.keymap.set "n" "gu" (λ [] (vim.cmd (.. "!open " (util.current-WORD)))))

(local cpp-indent
       (let [env (os.getenv "CPP_INDENT")]
         (if env (tonumber env)
                 4)))

(vim.api.nvim_create_autocmd "FileType"
  {:pattern  "cpp"
   :callback (fn []
               (set vim.bo.tabstop cpp-indent)
               (set vim.bo.softtabstop cpp-indent)
               (set vim.bo.shiftwidth cpp-indent)
               (set vim.bo.expandtab true))})

(vim.api.nvim_create_autocmd "FileType"
  {:pattern  "markdown"
   :callback (fn []
               (set vim.o.breakindentopt "shift:0")
               (set vim.bo.smartindent false)
               (set vim.bo.cindent false))})

(vim.api.nvim_create_autocmd "FileType"
  {:pattern  "gitcommit"
   :callback (fn []
               (set vim.o.breakindentopt "shift:0")
               (set vim.bo.smartindent false)
               (set vim.bo.cindent false))})

(vim.api.nvim_create_autocmd "FileType"
  {:pattern  "gdscript"
   :callback (fn []
               (set vim.bo.tabstop 4)
               (set vim.bo.shiftwidth 4)
               (set vim.bo.expandtab false))})

{}
