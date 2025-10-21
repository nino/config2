; Highlight 'as' type assertions
; extends

((as_expression
  "as" @keyword.cast)
 (#set! "priority" 101))

; Highlight TypeScript magic comments and TODO
((comment) @comment.magic
 (#match? @comment.magic "\\@ts-(expect-error|ignore|nocheck|check)|TODO|FIXME|XXX|HACK|NOTE")
 (#set! "priority" 101))
