use anyhow::{Context, Result};
use rust_tools::cmd_helpers::OutputExt;
use std::{env, path::Path, process::Command};

#[derive(Debug, Default)]
struct LintStats {
    errors: usize,
    warnings: usize,
    hints: usize,
}

#[derive(Debug, Clone)]
struct CommitInfo {
    hash: String,
    short_hash: String,
    subject: String,
    timestamp: String, // ISO8601
}

#[derive(Debug)]
struct CommitResult {
    commit: CommitInfo,
    stats: Option<LintStats>,
    error: Option<String>,
}

fn get_merge_commits_by_date(
    repo_path: &Path,
    count: usize,
    skip_days: u32,
) -> Result<Vec<CommitInfo>> {
    let mut result = Vec::new();
    let mut before_date: Option<String> = None;

    for _ in 0..count {
        // Build git log command to find the most recent merge commit before a date
        let mut args = vec![
            "log".to_string(),
            "--format=%H|%h|%aI|%s".to_string(),
            "--grep=^Merge pull request".to_string(),
            "-n".to_string(),
            "1".to_string(),
        ];

        if let Some(ref date) = before_date {
            args.push(format!("--before={}", date));
        }

        let output = Command::new("git")
            .current_dir(repo_path)
            .args(&args)
            .output()
            .context("Failed to run git log")?;

        if !output.status.success() {
            break;
        }

        let stdout = output.stdout.iter().map(|&b| b as char).collect::<String>();
        let line = stdout.trim();

        if line.is_empty() {
            break; // No more commits
        }

        let parts: Vec<&str> = line.splitn(4, '|').collect();
        if parts.len() != 4 {
            break;
        }

        let commit = CommitInfo {
            hash: parts[0].to_string(),
            short_hash: parts[1].to_string(),
            timestamp: parts[2].to_string(),
            subject: parts[3].to_string(),
        };

        // Calculate the next "before" date: skip_days before this commit
        if let Ok(dt) = chrono::DateTime::parse_from_rfc3339(&commit.timestamp) {
            let next_date = dt - chrono::Duration::days(skip_days as i64);
            before_date = Some(next_date.format("%Y-%m-%d").to_string());
        }

        result.push(commit);
    }

    Ok(result)
}

fn checkout_commit(repo_path: &Path, hash: &str) -> Result<()> {
    let output = Command::new("git")
        .current_dir(repo_path)
        .args(["checkout", hash])
        .output()
        .context("Failed to run git checkout")?;

    if !output.status.success() {
        anyhow::bail!("git checkout failed: {}", output.stderr_as_string());
    }
    Ok(())
}

fn run_yarn_install(repo_path: &Path) -> Result<()> {
    let output = Command::new("yarn")
        .current_dir(repo_path)
        .arg("--frozen-lockfile")
        .output()
        .context("Failed to run yarn")?;

    if !output.status.success() {
        anyhow::bail!("yarn install failed: {}", output.stderr_as_string());
    }
    Ok(())
}

fn run_lint(repo_path: &Path, temp_file: &Path) -> Result<String> {
    // Redirect stderr to a file to avoid pipe buffering issues
    let file =
        std::fs::File::create(temp_file).context("Failed to create temp file for lint output")?;

    Command::new("yarn")
        .current_dir(repo_path)
        .args(["next", "lint"])
        .stdout(std::process::Stdio::null())
        .stderr(file)
        .status()
        .context("Failed to run yarn next lint")?;

    let output = std::fs::read_to_string(temp_file).context("Failed to read lint output file")?;

    Ok(output)
}

fn strip_ansi_codes(s: &str) -> String {
    // Remove ANSI escape sequences: \x1b[...m or \x1b[...;...m etc.
    let mut result = String::with_capacity(s.len());
    let mut chars = s.chars().peekable();

    while let Some(c) = chars.next() {
        if c == '\x1b' {
            // Skip until we hit 'm' (end of ANSI sequence)
            while let Some(&next) = chars.peek() {
                chars.next();
                if next == 'm' {
                    break;
                }
            }
        } else {
            result.push(c);
        }
    }

    result
}

fn parse_lint_output(output: &str) -> LintStats {
    let mut stats = LintStats::default();

    // Strip ANSI color codes first
    let clean_output = strip_ansi_codes(output);

    // Next.js lint output format (on stderr):
    // ./path/to/file.tsx
    // 1:1  Error: Message here  rule-name
    // 15:10  Warning: Another message  another-rule

    for line in clean_output.lines() {
        let words: Vec<&str> = line.split_whitespace().collect();

        for word in &words {
            let w = word.to_lowercase();
            // Match "error", "error:", "warning", "warning:", etc.
            if w == "error" || w == "error:" {
                stats.errors += 1;
                break;
            } else if w == "warning" || w == "warning:" {
                stats.warnings += 1;
                break;
            } else if w == "info" || w == "info:" || w == "hint" || w == "hint:" {
                stats.hints += 1;
                break;
            }
        }
    }

    stats
}

fn get_current_branch(repo_path: &Path) -> Result<String> {
    let output = Command::new("git")
        .current_dir(repo_path)
        .args(["rev-parse", "--abbrev-ref", "HEAD"])
        .output()
        .context("Failed to get current branch")?;

    Ok(output.stdout_as_string().trim().to_string())
}

fn main() -> Result<()> {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        eprintln!("Usage: lint_history <repo_path> [commit_count] [skip_days]");
        eprintln!("  repo_path:    Path to a Next.js repository");
        eprintln!("  commit_count: Max commits to scan (default: 10)");
        eprintln!("  skip_days:    Min days between tested commits (default: 0)");
        std::process::exit(1);
    }

    let repo_path = Path::new(&args[1]);
    let commit_count: usize = args.get(2).and_then(|s| s.parse().ok()).unwrap_or(10);
    let skip_days: u32 = args.get(3).and_then(|s| s.parse().ok()).unwrap_or(0);

    if !repo_path.exists() {
        anyhow::bail!("Repository path does not exist: {}", repo_path.display());
    }

    println!("Analyzing lint history for: {}", repo_path.display());
    println!(
        "Scanning up to {} commits, skipping {} days between tests\n",
        commit_count, skip_days
    );

    // Save current branch to restore later
    let original_branch = get_current_branch(repo_path)?;
    println!("Original branch: {}\n", original_branch);

    let commits = get_merge_commits_by_date(repo_path, commit_count, skip_days)?;

    println!("Testing {} commits:\n", commits.len());

    let mut results: Vec<CommitResult> = Vec::new();

    for commit in &commits {
        print!(
            "Processing {} ({}) - {}... ",
            commit.short_hash,
            &commit.timestamp[..10], // Just the date part
            truncate(&commit.subject, 30)
        );

        let result = process_commit(repo_path, commit);
        match &result.stats {
            Some(stats) => {
                println!("E:{} W:{} H:{}", stats.errors, stats.warnings, stats.hints);
            }
            None => {
                println!("FAILED: {}", result.error.as_deref().unwrap_or("Unknown"));
            }
        }
        results.push(result);
    }

    // Restore original branch
    println!("\nRestoring original branch: {}", original_branch);
    checkout_commit(repo_path, &original_branch)?;

    // Print summary
    print_summary(&results);

    Ok(())
}

fn process_commit(repo_path: &Path, commit: &CommitInfo) -> CommitResult {
    let mut result = CommitResult {
        commit: commit.clone(),
        stats: None,
        error: None,
    };

    if let Err(e) = checkout_commit(repo_path, &commit.hash) {
        result.error = Some(format!("Checkout failed: {}", e));
        return result;
    }

    if let Err(e) = run_yarn_install(repo_path) {
        result.error = Some(format!("Yarn install failed: {}", e));
        return result;
    }

    let temp_file = repo_path.join(".lint_output.tmp");

    match run_lint(repo_path, &temp_file) {
        Ok(output) => {
            result.stats = Some(parse_lint_output(&output));
        }
        Err(e) => {
            result.error = Some(format!("Lint failed: {}", e));
        }
    }

    // Clean up temp file
    let _ = std::fs::remove_file(&temp_file);

    result
}

fn truncate(s: &str, max_len: usize) -> String {
    if s.len() <= max_len {
        s.to_string()
    } else {
        format!("{}…", &s[..max_len - 1])
    }
}

fn print_summary(results: &[CommitResult]) {
    println!("\n{}", "=".repeat(90));
    println!("SUMMARY");
    println!("{}\n", "=".repeat(90));

    let successful: Vec<_> = results.iter().filter(|r| r.stats.is_some()).collect();
    let failed: Vec<_> = results.iter().filter(|r| r.stats.is_none()).collect();

    println!(
        "Processed: {} commits ({} successful, {} failed)\n",
        results.len(),
        successful.len(),
        failed.len()
    );

    if !successful.is_empty() {
        let total_errors: usize = successful
            .iter()
            .map(|r| r.stats.as_ref().unwrap().errors)
            .sum();
        let total_warnings: usize = successful
            .iter()
            .map(|r| r.stats.as_ref().unwrap().warnings)
            .sum();
        let total_hints: usize = successful
            .iter()
            .map(|r| r.stats.as_ref().unwrap().hints)
            .sum();

        println!("Totals across all commits:");
        println!("  Errors:   {}", total_errors);
        println!("  Warnings: {}", total_warnings);
        println!("  Hints:    {}", total_hints);

        // Find commits with most issues
        let mut by_errors: Vec<_> = successful.clone();
        by_errors.sort_by(|a, b| {
            b.stats
                .as_ref()
                .unwrap()
                .errors
                .cmp(&a.stats.as_ref().unwrap().errors)
        });

        if let Some(worst) = by_errors.first() {
            if worst.stats.as_ref().unwrap().errors > 0 {
                println!(
                    "\nMost errors: {} ({}) - {} errors",
                    worst.commit.short_hash,
                    truncate(&worst.commit.subject, 30),
                    worst.stats.as_ref().unwrap().errors
                );
            }
        }

        // Trend analysis (if commits are in chronological order, oldest first when reversed)
        if successful.len() >= 2 {
            let oldest = successful.last().unwrap();
            let newest = successful.first().unwrap();
            let first = oldest.stats.as_ref().unwrap();
            let last = newest.stats.as_ref().unwrap();

            let error_diff = last.errors as i64 - first.errors as i64;
            let warning_diff = last.warnings as i64 - first.warnings as i64;

            println!(
                "\nTrend ({} → {}):",
                &oldest.commit.timestamp[..10],
                &newest.commit.timestamp[..10]
            );
            println!(
                "  Errors:   {} → {} ({}{})",
                first.errors,
                last.errors,
                if error_diff >= 0 { "+" } else { "" },
                error_diff
            );
            println!(
                "  Warnings: {} → {} ({}{})",
                first.warnings,
                last.warnings,
                if warning_diff >= 0 { "+" } else { "" },
                warning_diff
            );
        }
    }

    if !failed.is_empty() {
        println!("\nFailed commits:");
        for result in failed {
            println!(
                "  {} - {}: {}",
                result.commit.short_hash,
                truncate(&result.commit.subject, 30),
                result.error.as_deref().unwrap_or("Unknown error")
            );
        }
    }

    // Print detailed table
    println!("\n{}", "-".repeat(90));
    println!(
        "{:<12} {:<12} {:>8} {:>8} {:>8}  {}",
        "Date", "Commit", "Errors", "Warnings", "Hints", "Subject"
    );
    println!("{}", "-".repeat(90));

    for result in results {
        let date = &result.commit.timestamp[..10];
        if let Some(stats) = &result.stats {
            println!(
                "{:<12} {:<12} {:>8} {:>8} {:>8}  {}",
                date,
                result.commit.short_hash,
                stats.errors,
                stats.warnings,
                stats.hints,
                truncate(&result.commit.subject, 30)
            );
        } else {
            println!(
                "{:<12} {:<12} {:>8} {:>8} {:>8}  {} (FAILED)",
                date,
                result.commit.short_hash,
                "-",
                "-",
                "-",
                truncate(&result.commit.subject, 22)
            );
        }
    }
}
