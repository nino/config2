// fn output_bytes(bytes: Vec<u8>) {
//     let s = String::from_utf8(bytes).expect("Can't make a string from a UTF8 vector??");
//     println!("The file is this: {}", s);
// }

fn main() {
    // match std::fs::read("readfile.rs") {
    //     Ok(bytes) => output_bytes(bytes),
    //     Err(_) => println!("Unable to read file"),
    // }

    loop {
        let mut buf = String::new();
        let stdin = std::io::stdin();
        match stdin.read_line(&mut buf) {
            Ok(0) => break,
            Ok(_) => print!("{}", buf),
            Err(_) => {
                println!("Error");
                break;
            }
        }
    }
}
