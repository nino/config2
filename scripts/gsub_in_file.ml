#!/usr/bin/env ocaml
#use "topfind"

#require "base"

#require "stdio"

#require "re"

open Base

let gsub str a b =
  let regex = Re.Perl.compile_pat a in
  Re.replace ~all:true regex ~f:(fun _ -> b) str

let gsub_in_file filename a b =
  try
    let readchannel = Stdio.In_channel.create filename in
    let content = Stdio.In_channel.input_all readchannel in
    let new_content = gsub content a b in
    Stdio.In_channel.close readchannel;
    Stdio.Out_channel.write_all filename ~data:new_content;
    Ok ()
  with Sys_error err -> Error err

let main () =
  let args = Sys.get_argv () in
  if Array.length args <> 4 then failwith "3 args required"
  else
    let filename = Array.get args 1 in
    let a = Array.get args 2 in
    let b = Array.get args 3 in
    match gsub_in_file filename a b with
    | Ok () -> ()
    | Error err -> Stdio.eprintf "%s\n" err

let () = main ()
