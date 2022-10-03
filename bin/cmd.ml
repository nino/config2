open Stdio

let run cmd =
  let stdout = Unix.open_process_in cmd in
  let output = In_channel.input_lines stdout in
  In_channel.close stdout;
  output
