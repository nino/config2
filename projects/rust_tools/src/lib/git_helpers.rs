use git2::Repository;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum Error {
    #[error("Git error: {0}")]
    Git(#[from] git2::Error),
}

pub fn is_clean(path: &str) -> Result<bool, Error> {
    let repo = Repository::open(path)?;
    let branches = repo.branches(None)?;
    for item in branches {
        let (branch, _) = item?;
        let name = branch.name()?;
        println!("Branch: {}", name.unwrap_or("No name"));
    }

    let statuses = repo.statuses(None)?;
    Ok(statuses.is_empty())
}
