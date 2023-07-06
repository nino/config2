use anyhow::anyhow;
use rust_tools::cmd_helpers::OutputExt;
use std::env;
use std::fs;
use std::io::Write;
use std::process::Command;
use termcolor::{Color, ColorChoice, ColorSpec, StandardStream, WriteColor};

trait LogErr {
    fn log_err(self, msg: String) -> Self;
}

impl<T, E: std::fmt::Debug> LogErr for Result<T, E> {
    fn log_err(self, msg: String) -> Self {
        if let Err(e) = &self {
            println!("{}: {:?}", msg, e);
        }
        self
    }
}

#[allow(dead_code)]
fn trunk_branch_name() -> Result<String, String> {
    let full_branch_name: String = Command::new("git")
        .args(&["symbolic-ref", "refs/remotes/origin/HEAD"])
        .output()
        .map_err(|_| {
            "Failed to get full branch name from `git symbolic-ref refs/remotes/origin/HEAD`"
        })?
        .stdout_as_string();

    match full_branch_name.split('/').last() {
        Some(x) => Ok(x.trim().to_string()),
        None => Err(
            "Unable to get branch name from `git symbolic-ref refs/remotes/origin/HEAD`"
                .to_string(),
        ),
    }
}

fn list_directories() -> Vec<String> {
    let current_dir = env::current_dir().unwrap();
    fs::read_dir(current_dir)
        .unwrap()
        .filter_map(|entry| {
            let entry = entry.unwrap();
            if entry.file_type().unwrap().is_dir() {
                Some(entry.file_name().into_string().unwrap())
            } else {
                None
            }
        })
        .collect()
}

fn fetch(path: &str) -> anyhow::Result<()> {
    println!("Fetching {}…", path);
    Command::new("git")
        .current_dir(path)
        .args(&["fetch"])
        .output()
        .map_err(|_| anyhow!("Failed to fetch {}", path))?;
    Ok(())
}

fn update(path: &str) -> anyhow::Result<()> {
    Command::new("git")
        .current_dir(path)
        .args(&["pull"])
        .output()
        .map_err(|_| anyhow!("Failed to fetch {}", path))?;
    Ok(())
}

struct ProcessResult {
    path: String,
    unclean: bool,
    current_branch: String,
}

fn process_repo(
    path: &str,
    unclean_repos: &mut Vec<String>,
    checked_out_branches: &mut Vec<(String, String)>,
) -> anyhow::Result<()> {
    let repo = git2::Repository::open(path)?;
    fetch(path).log_err(format!("Failed to fetch {}", path))?;

    let index = repo.index()?;
    if !index.is_empty() {
        unclean_repos.push(path.to_string());
    } else {
        update(path).log_err(format!("Failed to update {}", path))?;
    }

    match repo.head()?.name() {
        Some(branch) => checked_out_branches.push((
            path.to_string(),
            branch.replace("refs/heads/", "").to_string(),
        )),
        None => {}
    }
    Ok(())
}

fn main() {
    let mut unclean_repos = vec![];
    let mut checked_out_branches = vec![];

    for repo in list_directories() {
        let _ = process_repo(&repo, &mut unclean_repos, &mut checked_out_branches);
    }

    if !unclean_repos.is_empty() {
        println!("\nUnclean repos:");
        for repo in unclean_repos {
            println!("- {}", repo);
        }
    }

    println!("\nChecked-out branches:");
    let mut stdout = StandardStream::stdout(ColorChoice::Always);
    for (repo, branch) in checked_out_branches {
        if branch == "master" || branch == "develop" || branch == "main" {
            stdout.reset().unwrap();
            writeln!(&mut stdout, "- {}: {}", repo, branch).unwrap();
        } else {
            stdout
                .set_color(ColorSpec::new().set_fg(Some(Color::Red)))
                .unwrap();
            writeln!(&mut stdout, "- {}: {}", repo, branch).unwrap();
        }
    }
}
