use rust_tools::cmd_helpers::OutputExt;

use std::{path::PathBuf, process::Command, thread::sleep, time::Duration};

struct Photographer {
    timelapse_root_path: PathBuf,
}

impl Photographer {
    fn new() -> Result<Photographer, String> {
        Ok(Photographer {
            timelapse_root_path: dirs::home_dir()
                .ok_or("Unable to find home directory".to_string())?
                .join("Timelapse2"),
        })
    }

    fn create_day_dir_if_needed(&self) -> Result<PathBuf, String> {
        let today = chrono::Local::now().format("%Y-%m-%d").to_string();
        let day_dir = self.timelapse_root_path.join(&today);
        std::fs::create_dir_all(&day_dir).map_err(|_| format!("Unable to create day dir"))?;
        Ok(day_dir)
    }

    fn screenshoot_loop(&self) {
        loop {
            match self.do_screenshot() {
                Ok(()) => sleep(Duration::from_secs(4)),
                Err(reason) => {
                    println!("Error: {}", reason);
                    sleep(Duration::from_secs(60))
                }
            }
        }
    }

    fn do_screenshot(&self) -> Result<(), String> {
        let day_dir = self.create_day_dir_if_needed()?;
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

fn main() {
    println!("Starting up...");
    let photographer = Photographer::new().expect("Unable to create photographer");
    photographer.screenshoot_loop();
}
