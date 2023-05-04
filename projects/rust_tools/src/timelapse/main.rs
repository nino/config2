use std::{path::PathBuf, process::Command};

trait OutputExt {
    fn stdout_as_string(&self) -> String;
    fn stderr_as_string(&self) -> String;
}

impl OutputExt for std::process::Output {
    fn stdout_as_string(&self) -> String {
        self.stdout
            .iter()
            .map(|&byte| byte as char)
            .collect::<String>()
    }

    fn stderr_as_string(&self) -> String {
        self.stderr
            .iter()
            .map(|&byte| byte as char)
            .collect::<String>()
    }
}

fn create_day_dir_if_needed(timelapse_root_path: &PathBuf) -> Result<PathBuf, String> {
    let today = chrono::Local::now().format("%Y-%m-%d").to_string();
    let day_dir = timelapse_root_path.join(&today);
    std::fs::create_dir_all(&day_dir).map_err(|_| format!("Unable to create day dir"))?;
    Ok(day_dir)
}

fn next_filename(day_dir: &PathBuf) -> Result<String, String> {
    let entries =
        std::fs::read_dir(day_dir).map_err(|_| "Unable to read entries of day dir".to_string())?;
    let files = entries
        .filter_map(|entry| entry.ok())
        .filter(|entry| {
            entry
                .file_type()
                .map(|file_type| file_type.is_file())
                .unwrap_or(false)
        })
        .filter_map(|entry| entry.file_name().to_str().map(|s| s.to_string()));

    let max = files
        .filter_map(|filename| filename.replace(".jpg", "").parse::<i32>().ok())
        .max()
        .unwrap_or(0);

    Ok(String::from(format!("{:05}.jpg", max + 1)))
}

fn capture_screenshot(screenshot_path: &str) -> Result<(), String> {
    let output = Command::new("screencapture")
        .args(&["-x", "-t", "jpg", "-m", &screenshot_path])
        .output()
        .map_err(|err| err.to_string())?;

    if output.status.success() {
        println!("Screenshot saved to {}", screenshot_path);
        Ok(())
    } else {
        println!("Unable to save screenshot");
        Err("Unable to save screenshot".to_string())
    }
}

fn resize_screenshot(file_path: &str) -> Result<(), String> {
    let output = Command::new("convert")
        .args(&["-scale", "1800x1124!", file_path, file_path])
        .output()
        .map_err(|err| err.to_string())?;

    if output.status.success() {
        Ok(())
    } else {
        Err(format!(
            "Unable to resize screenshot {} because {}",
            file_path,
            output.stderr_as_string()
        )
        .to_string())
    }
}

fn do_screenshot(timelapse_root_path: &PathBuf) -> Result<(), String> {
    let day_dir = create_day_dir_if_needed(timelapse_root_path)?;
    let screenshot_path = String::from(
        day_dir
            .join(next_filename(&day_dir)?)
            .to_str()
            .ok_or("Couldn't make string from screenshot path".to_string())?,
    );
    capture_screenshot(&screenshot_path)?;
    resize_screenshot(&screenshot_path)?;
    Ok(())
}

fn screenshoot_loop(timelapse_root_path: &PathBuf) {
    loop {
        match do_screenshot(timelapse_root_path) {
            Ok(()) => std::thread::sleep(std::time::Duration::from_secs(4)),
            Err(reason) => {
                println!("Error: {}", reason);
                std::thread::sleep(std::time::Duration::from_secs(60))
            }
        }
    }
}

fn main() {
    println!("Starting up...");

    let timelapse_root_path = dirs::home_dir()
        .expect("Unable to find home directory")
        .join("Timelapse2");

    screenshoot_loop(&timelapse_root_path);
}
