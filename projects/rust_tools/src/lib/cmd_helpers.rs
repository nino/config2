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

#[cfg(all(test, unix))]
mod tests {
    use super::*;
    use std::os::unix::process::ExitStatusExt;
    use std::process::{ExitStatus, Output};

    fn make_output(stdout: &[u8], stderr: &[u8]) -> Output {
        Output {
            status: ExitStatus::from_raw(0),
            stdout: stdout.to_vec(),
            stderr: stderr.to_vec(),
        }
    }

    #[test]
    fn reads_stdout_as_string() {
        let output = make_output(b"hello world\n", b"");
        assert_eq!(output.stdout_as_string(), "hello world\n");
    }

    #[test]
    fn reads_stderr_as_string() {
        let output = make_output(b"", b"boom: it broke");
        assert_eq!(output.stderr_as_string(), "boom: it broke");
    }

    #[test]
    fn empty_buffers_produce_empty_strings() {
        let output = make_output(b"", b"");
        assert_eq!(output.stdout_as_string(), "");
        assert_eq!(output.stderr_as_string(), "");
    }

    #[test]
    fn decodes_one_codepoint_per_byte() {
        // The implementation maps `byte as char`, i.e. a Latin-1-style decode
        // (one codepoint per byte) rather than UTF-8, so 0xE9 becomes U+00E9.
        let output = make_output(&[0x68, 0x69, 0xE9], b"");
        assert_eq!(output.stdout_as_string(), "hié");
    }
}
