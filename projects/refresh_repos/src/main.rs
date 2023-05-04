use std::env;
use std::fs;
use std::process::Command;

#[allow(dead_code)]
fn trunk_branch_name() -> Result<String, String> {
    let full_branch_name: String = Command::new("git")
        .args(&["symbolic-ref", "refs/remotes/origin/HEAD"])
        .output()
        .map_err(|_| {
            "Failed to get full branch name from `git symbolic-ref refs/remotes/origin/HEAD`"
        })?
        .stdout
        .iter()
        .map(|&byte| byte as char)
        .collect();

    match full_branch_name.split('/').last() {
        Some(x) => Ok(x.to_string()),
        None => Err(
            "Unable to get branch name from `git symbolic-ref refs/remotes/origin/HEAD`"
                .to_string(),
        ),
    }
}

fn cd(path: &str) {
    env::set_current_dir(path).unwrap();
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

fn is_git_working_tree_clean() -> bool {
    match Command::new("git")
        .args(&["status", "--porcelain"])
        .output()
    {
        Ok(output) => output.status.success() && output.stdout.is_empty(),
        Err(_) => false,
    }
}

fn main() {
    let mut unclean_repos = vec![];

    for repo in list_directories() {
        cd(&repo);
        println!("Entering {}...", repo);
        let _ = Command::new("git").arg("status").status().unwrap();

        if is_git_working_tree_clean() {
            println!("!!! {} is clean, pulling!", repo);
            let _ = Command::new("git").arg("pull").status().unwrap();
        } else {
            println!("!!! {} is not clean, skipping!", repo);
            unclean_repos.push(repo);
        }

        cd("..");
        println!("");
    }

    if !unclean_repos.is_empty() {
        println!("Unclean repos:");
        for repo in unclean_repos {
            println!("- {}", repo);
        }
    }
}
