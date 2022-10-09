open Core

let time_zone = ref None

(* A safer version of Time.Zone.local, which defaults to UTC instead of throwing an exception if we
   cannot figure out local time. See https://github.com/janestreet/core/issues/96 for one example
   when this can happen *)
let get_time_zone () =
  match !time_zone with
  | Some zone -> zone
  | None ->
      let zone =
        try force Time_unix.Zone.local with _ -> Time_unix.Zone.utc
      in
      time_zone := Some zone;
      zone

let today () = Date.today ~zone:(get_time_zone ())
