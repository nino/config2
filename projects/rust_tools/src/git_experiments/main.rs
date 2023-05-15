use rust_tools::git_helpers;

fn main() {
    if let Ok(is_clean) = git_helpers::is_clean(".") {
        println!("Is clean: {}", is_clean);
    } else {
        println!("Error checking if clean");
    }
}
