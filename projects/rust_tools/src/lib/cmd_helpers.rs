pub trait OutputExt {
    fn stdout_as_string(&self) -> String;
    fn stderr_as_string(&self) -> String;
}

impl OutputExt for std::process::Output {
    fn stdout_as_string(&self) -> String {
        self.stdout.iter().map(|&byte| byte as char).collect()
    }

    fn stderr_as_string(&self) -> String {
        self.stderr.iter().map(|&byte| byte as char).collect()
    }
}
