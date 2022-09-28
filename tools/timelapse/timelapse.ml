open Core

let timelapse_root_path = Sys.home_directory () ^/ "Timelapse"

let create_day_dir_if_needed () =
  let today = Datetime.today () in
  let date_string = Date.format today "%Y-%m-%d" in
  let day_dir = timelapse_root_path ^/ date_string in
  Unix.mkdir_p day_dir;
  day_dir

let postprocess_image fname = ignore fname

let next_filename day_dir =
  ignore day_dir;
  "001.jpg"

let screencapture path =
  ignore path;
  ignore (postprocess_image path);
  Ok ()

let screenshot_loop () =
  while true do
    let day_dir = create_day_dir_if_needed () in
    match screencapture (day_dir ^/ next_filename day_dir) with
    | Ok () -> Unix.sleep 4
    | Error () -> Unix.sleep 60
  done

let main () =
  print_endline "Starting up...\n";
  screenshot_loop ()

let () = main ()
