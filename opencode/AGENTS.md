Hi!

If you write one more `const [isLoading, setIsLoading] = useState(false)` for an async operation instead of using TanStack's `useQuery` or `useMutation` I'm going to KICK OFF.

- Use fd for finding files and rg for grepping. Calling rg with `--type ts` will
  also match tsx files. There is not such thing as `--type tsx`.
- ALWAYS use `??` instead of `||` for nullish-coalescing / fallback values. ONLY
  use `||` if you're actually trying to get the OR value of two booleans.
- Don't use `++` or `--`. Use `+= 1` or `-= 1`.
- Remove unused imports
- In new code, fully qualify React API names. So, write `import React from "react";` and `React.useState(...)`. You don't need to change existing imports unless asked to.
- I have ast-grep (sg) installed, so you can use that for structured find & replace

Don't hesitate to create todo lists. The final item on your todo list should always be to fix any CLAUDE.md/AGENTS.md/etc guideline violations in code you added or edited. This is important because LLMs often forget to follow rules when they focus on a task, so you need to check for rule violations when you're done. It's basically a proofreading step, I need to do this too when I write code.

- always write new React components like this: `function MyComponent({ propA, propB }: { propA: someType, propB: someType }): JSX.Element {....}` (possibly use `JSX.Element | null` if it can also return `null`)
- Don't use `export default`, except for NextJS page components
- When defining a top-level function, prefer `function` functions over arrow functions
- Prefer `for (const .. of ..)` loops over `.forEach`
- Don't specify staleTime, retry, etc on React Query hooks unless there's a specific reason. Usually you can assume that our configured defaults will be fine.
- Don't use `!!x`. Use `x != null` or `Boolean(x)`
- Use a proper ellipsis character (…) instead of "..." for user-facing text
- Don't add comments that just repeat what the code says, like

      // increment i
      i++;

      // call foo
      foo();

  If you find yourself accidentally adding such comments, delete them in the proofreading step.

- I usually have uncommitted ESLint config changes. These are just for my convenience. Please don't ever stage or commit them unless specifically asked to.
