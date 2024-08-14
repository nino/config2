use anyhow::anyhow;
use rayon::prelude::*;
use rayon::ThreadPoolBuilder;
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

fn is_clean(path: &str) -> anyhow::Result<bool> {
    let output = Command::new("git")
        .current_dir(path)
        .args(&["status", "--porcelain=v1"])
        .output()
        .map_err(|_| anyhow!("Failed to get status for {}", path))?
        .stdout;
    Ok(output.len() == 0)
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
        .map_err(|_| anyhow!("Failed to update {}", path))?;
    Ok(())
}

struct ProcessResult {
    path: String,
    unclean: bool,
    current_branch: String,
}

fn process_repo(path: &str) -> anyhow::Result<ProcessResult> {
    let mut result = ProcessResult {
        path: String::from(path),
        unclean: false,
        current_branch: String::from("HEAD"),
    };
    let repo = git2::Repository::open(path)?;
    fetch(path).log_err(format!("Failed to fetch {}", path))?;

    if !is_clean(path)? {
        result.unclean = true;
    } else {
        update(path).log_err(format!("Failed to update {}", path))?;
    }

    match repo.head()?.name() {
        Some(branch) => result.current_branch = branch.replace("refs/heads/", "").to_string(),
        None => {}
    }
    Ok(result)
}

fn main() {
    // This doesn't actually seem to work, but 🤷
    ThreadPoolBuilder::new()
        .num_threads(48)
        .build_global()
        .expect("Failed to build thread pool");

    let mut unclean_repos = vec![];
    let mut checked_out_branches = vec![];
    let mut errors = vec![];

    let dirs = list_directories();
    let results: Vec<anyhow::Result<ProcessResult>> =
        dirs.par_iter().map(|path| process_repo(&path)).collect();

    for result in results.iter() {
        match result {
            Ok(res) => {
                if res.unclean {
                    unclean_repos.push(res.path.clone());
                }
                checked_out_branches.push((res.path.clone(), res.current_branch.clone()));
            }
            Err(err) => {
                errors.push(format!("{:?}", err));
            }
        }
    }

    if !errors.is_empty() {
        println!("\nErrors:");
        for error in errors {
            println!("- {}", error);
        }
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
        if branch == "master"
            || branch == "develop"
            || branch == "main"
            || branch == "environment/develop"
        {
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
