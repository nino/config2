import gleam/io
import gleam/otp/task
import gleam/string
import shellout
import simplifile
import path
import gleam/list

type ProcessResult {
  ProcessResult(name: String, is_clean: Bool, head_branch: String)
}

fn is_trunk(branch: String) -> Bool {
  let trunk_branches = ["master", "main", "trunk", "develop"]
  list.any(trunk_branches, fn(trunk) { trunk == branch })
}

fn get_directories(parent: String) -> List(String) {
  let assert Ok(entries) = simplifile.list_contents(parent)
  let full_paths =
    list.map(
      entries,
      fn(entry) {
        path.join(parent, entry)
        |> path.absname
      },
    )
  list.filter(full_paths, fn(path) { simplifile.is_directory(path) })
}

fn is_clean(path: String) -> Bool {
  let output =
    shellout.command(
      run: "git",
      with: ["status", "--porcelain"],
      in: path,
      opt: [],
    )
  case output {
    Ok(output) -> output == ""
    Error(_) -> False
  }
}

fn get_head_branch(path: String) -> String {
  let output =
    shellout.command(
      run: "git",
      with: ["rev-parse", "--abbrev-ref", "HEAD"],
      in: path,
      opt: [],
    )
  case output {
    Ok(output) -> output
    Error(_) -> ""
  }
}

fn update_repo(path: String) -> Nil {
  let _ = shellout.command(run: "git", with: ["pull"], in: path, opt: [])
  Nil
}

fn process_repo(path: String) -> ProcessResult {
  let clean = is_clean(path)
  case clean {
    True -> update_repo(path)
    _ -> Nil
  }
  let head_branch = string.trim(get_head_branch(path))
  io.print(".")
  ProcessResult(name: path, is_clean: clean, head_branch: head_branch)
}

pub fn main() {
  let entries = get_directories(".")
  let results =
    list.map(entries, fn(entry) { task.async(fn() { process_repo(entry) }) })
    |> list.map(task.await_forever)

  io.println("\n\nUnclean repos:")
  list.filter(results, fn(result) { !result.is_clean })
  |> list.each(fn(result) { io.println("- " <> path.basename(result.name)) })

  io.println("\n\nBranches:")
  list.each(
    results,
    fn(result) {
      let annotation = case is_trunk(result.head_branch) {
        True -> ""
        False -> "!!!"
      }
      io.println(
        "- " <> path.basename(result.name) <> ": " <> result.head_branch <> " " <> annotation,
      )
    },
  )
  Nil
}
