open Stdint

exception NotImplemented of string

type wav_format = PCM | Float | Unknown

let read_wav_format data =
  (* Not sure if it's a good idea to convert to uint32 and back, but I
     couldn't work out how to write uint32 literals to match with *)
  match Uint32.of_bytes_little_endian data 0 |> Uint32.to_int with
  | 0x0001 -> PCM
  | 0x0002 -> Float
  | _ -> Unknown

let write_wav_format format data =
  match format with
  | PCM -> Bytes.set_int32_le data 0 0x0001l
  | Float -> Bytes.set_int32_le data 0 0x0002l
  | Unknown -> raise (NotImplemented "Only PCM and Float are implemented.")

type wav_file = {
  file_size : int;
  format : wav_format;
  number_of_channels : int;
  samples_per_sec : int32;
  bytes_per_sec : int32;
}
