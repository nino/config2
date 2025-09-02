Hi!

- Use fd for finding files and rg for grepping. Calling rg with `--type ts` will
  also match tsx files. There is not such thing as `--type tsx`.
- ALWAYS use `??` instead of `||` for nullish-coalescing / fallback values. ONLY
  use `||` if you're actually trying to get the OR value of two booleans.
- Don't use `++` or `--`. Use `+= 1` or `-= 1`.
- Remove unused imports
- In new code, fully qualify React API names. So, write `import React from "react";` and `React.useState(...)`. You don't need to change existing imports unless asked to.
- I have comby installed, so you can use that for structured find & replace

Don't hesitate to create todo lists. The final item on your todo list should always be to fix any CLAUDE.md/AGENTS.md/etc guideline violations in code you added or edited. This is important because LLMs often forget to follow rules when they focus on a task, so you need to check for rule violations when you're done. It's basically a proofreading step, I need to do this too when I write code.
