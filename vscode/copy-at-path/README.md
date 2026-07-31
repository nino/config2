# Copy @path

Copies the path of the current file to the clipboard, with an `@` before it.
This is the same as the `<M-c>` keymap in the Neovim configuration.

## Keys

| Key             | Result                                                    |
| --------------- | --------------------------------------------------------- |
| `option`+`c`    | `@/path/to/file` — or `@/path/to/file:12` / `@/path/to/file:12-18` if text is selected |
| `shift`+`option`+`c` | Always adds the line number or the range               |

The command palette also has `Copy @path without line number`.

## Settings

- `copyAtPath.pathStyle` — `absolute` (default) or `workspaceRelative`.
- `copyAtPath.prefix` — the text before the path. The default is `@`.
- `copyAtPath.showNotification` — show a status bar message. The default is `true`.

## Installation

```bash
cd ~/.config/vscode/copy-at-path
npx --yes @vscode/vsce package --allow-missing-repository --skip-license
```

Then install the `.vsix` file:

```bash
cursor --install-extension ~/.config/vscode/copy-at-path/copy-at-path-0.0.1.vsix
```

Use `code` in the place of `cursor` for VS Code. You can also install it from the
UI: `Extensions` → `...` → `Install from VSIX...`.

## Development

Open this directory in VS Code or Cursor and press `F5` to start an
Extension Development Host window.
