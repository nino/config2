const vscode = require("vscode");
const path = require("path");

/** Read the settings of this extension. */
function config() {
  return vscode.workspace.getConfiguration("copyAtPath");
}

/**
 * Make the path text for a document.
 * @param {vscode.TextDocument} document
 */
function pathFor(document) {
  const uri = document.uri;
  if (uri.scheme !== "file") {
    // Untitled buffers and virtual documents have no file path.
    return uri.toString();
  }
  if (config().get("pathStyle") === "workspaceRelative") {
    const folder = vscode.workspace.getWorkspaceFolder(uri);
    if (folder) {
      const relative = path.relative(folder.uri.fsPath, uri.fsPath);
      // Files outside the folder keep the full path.
      if (!relative.startsWith("..")) {
        return relative;
      }
    }
  }
  return uri.fsPath;
}

/**
 * Make the `:line` or `:start-end` suffix for a selection.
 * @param {vscode.Selection} selection
 */
function lineSuffix(selection) {
  const start = selection.start.line + 1;
  let end = selection.end.line + 1;
  // A selection that stops at column 0 does not include that line.
  if (end > start && selection.end.character === 0) {
    end -= 1;
  }
  return start === end ? `:${start}` : `:${start}-${end}`;
}

/**
 * Put the text on the clipboard and tell the user.
 * @param {string} text
 */
async function copy(text) {
  await vscode.env.clipboard.writeText(text);
  if (config().get("showNotification")) {
    vscode.window.setStatusBarMessage(`Copied ${text}`, 3000);
  }
}

/**
 * @param {"auto" | "always" | "never"} lineMode
 */
async function run(lineMode) {
  const editor = vscode.window.activeTextEditor;
  if (!editor) {
    vscode.window.showWarningMessage("Copy @path: no editor is open.");
    return;
  }
  const prefix = config().get("prefix");
  const filePath = pathFor(editor.document);
  const withLine =
    lineMode === "always" || (lineMode === "auto" && !editor.selection.isEmpty);
  const suffix = withLine ? lineSuffix(editor.selection) : "";
  await copy(`${prefix}${filePath}${suffix}`);
}

function activate(context) {
  context.subscriptions.push(
    vscode.commands.registerCommand("copyAtPath.copy", () => run("auto")),
    vscode.commands.registerCommand("copyAtPath.copyWithLine", () =>
      run("always"),
    ),
    vscode.commands.registerCommand("copyAtPath.copyPathOnly", () =>
      run("never"),
    ),
  );
}

function deactivate() {}

module.exports = { activate, deactivate };
