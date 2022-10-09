open Core

let timelapse_root_path = Sys_unix.home_directory () ^/ "Timelapse"
let sh cmd = match Sys_unix.command cmd with 0 -> Ok () | other -> Error other
let ls path = try Ok (Sys_unix.ls_dir path) with _ -> Error ()
let re str = Re.compile (Re.str str)

let create_day_dir_if_needed () =
  let today = Datetime.today () in
  let date_string = Date_unix.format today "%Y-%m-%d" in
  let day_dir = timelapse_root_path ^/ date_string in
  Core_unix.mkdir_p day_dir;
  day_dir

let next_filename day_dir =
  match ls day_dir with
  | Ok entries -> (
      let numbers =
        List.filter_map entries ~f:(fun entry ->
            try
              Some (Re.replace_string (re ".jpg") ~by:"" entry |> Int.of_string)
            with _ -> None)
      in
      match List.reduce ~f:Int.max numbers with
      | Some x -> Ok (Int.to_string (x + 1) ^ ".jpg")
      | None -> Error "cannot generate next filename")
  | Error _ -> Error "cannot generate next filename"

let screencapture path =
  print_endline @@ "Capturing screengrab at " ^ path;
  let quoted = Filename.quote path in
  match sh @@ "screencapture -x -t jpg -m " ^ quoted with
  | Ok () -> sh @@ "convert -scale 1200 " ^ quoted ^ " " ^ quoted
  | Error err -> Error err

let screenshot_loop () =
  while true do
    let day_dir = create_day_dir_if_needed () in
    match next_filename day_dir with
    | Error err -> print_endline ("Unable to create screenshot because " ^ err)
    | Ok filename -> (
        match screencapture (day_dir ^/ filename) with
        | Ok () -> Core_unix.sleep 4
        | Error _ -> Core_unix.sleep 60)
  done

let main () =
  print_endline "Starting up...\n";
  screenshot_loop ()

let () = main ()
