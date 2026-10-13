# Global notes

## H1 for final report

When you're ready to present what you've done after an extended bit of work,
start with an H1 heading, so I can clearly see where you finish narrating your
progress and start reporting the final results.

## My shell is zsh, not bash — unquoted `$var` does NOT word-split

The interactive/tooling shell here is **zsh**. The recurring gotcha: unlike
bash, zsh does **not** perform word-splitting on unquoted parameter
expansions. So building a space-joined string and expanding it unquoted
passes the whole thing as a SINGLE argument.

```zsh
files="a.ts b.ts"
prettier --write $files   # bash: two args | zsh: ONE arg "a.ts b.ts" -> "no files matching pattern"
```

Do this instead:

- **Inline the arguments** or use a **glob** (`prettier --write app/**/*.ts`) — preferred.
- Use a real **array**: `files=(a.ts b.ts); prettier --write $files` (arrays expand to separate words in zsh).
- Or force splitting: `prettier --write ${=files}` (or `${(z)files}`).

Don't assume bash word-splitting when passing a list of files through a variable.

# Committing

Only commit when I explicitly ask you to.

# Reviewing PRs

When I'm reviewing code changes, annotate all statements about existing
functionality with 🧱 and statements about changed/new functionality with ✨.
This makes it easier to see at a glance where I should consider making changes
vs just having to deal with pre-existing architecture.
