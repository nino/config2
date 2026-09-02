Mannered prose substitutes metaphor and flourish for direct statement. Instead
of "a parameter worth varying," the mannered writer produces "a dial worth
turning." Instead of "this point still matters," they write "this point earns
its keep." The phrases exist to display the writer, not to convey the idea, and
readers can tell. That is why mannered prose irritates: it makes the reader work
harder so the writer can perform. It is also imprecise. Metaphors drag in
connotations the writer did not choose and cannot control. The fix is to say
what you mean. When a literal phrase is available, use it.

# Global notes

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

