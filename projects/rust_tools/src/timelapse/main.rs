use rust_tools::cmd_helpers::OutputExt;
use std::{path::PathBuf, process::Command, thread::sleep, time::Duration};
use thiserror::Error;

#[derive(Error, Debug)]
enum Error {
    #[error("Unable to find home dir")]
    UnableToFindHomeDir,

    #[error("Unable to create screenshot")]
    UnableToCreateScreenshot,

    #[error("Unable to resize screenshot {path} because: {reason}")]
    UnableToResizeScreenshot { path: String, reason: String },

    #[error("Unable convert screenshot path to string")]
    UnableToConvertScreenshotPathToString,

    #[error("IO Error")]
    IoError(#[from] std::io::Error),
}

struct Photographer {
    timelapse_root_path: PathBuf,
}

impl Photographer {
    fn new() -> Result<Photographer, Error> {
        Ok(Photographer {
            timelapse_root_path: dirs::home_dir()
                .ok_or(Error::UnableToFindHomeDir)?
                .join("Timelapse2"),
        })
    }

    fn create_day_dir_if_needed(&self) -> Result<PathBuf, Error> {
        let today = chrono::Local::now().format("%Y-%m-%d").to_string();
        let day_dir = self.timelapse_root_path.join(&today);
        std::fs::create_dir_all(&day_dir)?;
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

    fn do_screenshot(&self) -> Result<(), Error> {
        let day_dir = self.create_day_dir_if_needed()?;
        let screenshot_path = String::from(
            day_dir
                .join(next_filename(&day_dir)?)
                .to_str()
                .ok_or(Error::UnableToConvertScreenshotPathToString)?,
        );
        capture_screenshot(&screenshot_path)?;
        resize_screenshot(&screenshot_path)?;
        Ok(())
    }
}

fn next_filename(day_dir: &PathBuf) -> Result<String, Error> {
    let entries = std::fs::read_dir(day_dir)?;
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

fn capture_screenshot(screenshot_path: &str) -> Result<(), Error> {
    let output = Command::new("screencapture")
        .args(&["-x", "-t", "jpg", "-m", &screenshot_path])
        .output()?;

    if output.status.success() {
        println!("Screenshot saved to {}", screenshot_path);
        Ok(())
    } else {
        println!("Unable to save screenshot");
        Err(Error::UnableToCreateScreenshot)
    }
}

fn resize_screenshot(file_path: &str) -> Result<(), Error> {
    let output = Command::new("convert")
        .args(&["-scale", "1800x1124!", file_path, file_path])
        .output()?;

    if output.status.success() {
        Ok(())
    } else {
        Err(Error::UnableToResizeScreenshot {
            path: file_path.to_string(),
            reason: output.stderr_as_string(),
        })
    }
}

fn main() {
    println!("Starting up...");
    let photographer = Photographer::new().expect("Unable to create photographer");
    photographer.screenshoot_loop();
}
