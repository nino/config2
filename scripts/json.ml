(* WIP *)

#use "topfind"

#require "base"

#require "yojson"

open Base

type person = { name : string; age : int; animals : string list }

let read_person json =
  let result = Yojson.Basic.from_string
    {| { "name": "Nino", "age": 29, "animals": ["dog", "cat", "opossum"] } |} in
  match result with 
  | `Assoc assoc_list -> 
      let read_assoc_list person = function
        | ((`String "name"), name) -> { person with name = name }
        | ((`String "age"), age) -> { person with age = age }

