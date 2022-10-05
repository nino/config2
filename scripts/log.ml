#use "topfind"
#require "base"
#require "stdio"

#require "re"
open Base

type commit = { id: string; date: string; author: string; }

let print_commit { id; date; author } =
  Stdio.printf "Commit with ID %s made by %s on %s\n" id author date

let commit = Re.Perl.re ~opts:[`Multiline] "^commit (\\w+).*\n\
                                            ^Author:(.*)\n\
                                            (^Merge:.*\n)?\
                                            Date:(.*)\n" |> Re.compile

let matches = Re.all commit (Stdio.In_channel.input_all Stdio.stdin)

let () = List.iter matches ~f:(
  fun group ->
    let captures = (Re.Group.all group) in
    print_commit {
      id = String.strip (captures.(1));
      author = String.strip captures.(2);
      date = String.strip captures.(4);
    }
)
