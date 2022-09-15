open Base
open OUnit2
open Stdint

let suite =
  "Wav"
  >::: [
         ( "read_wav_format" >:: fun _ ->
           let data = Bytes.create 4 in
           Uint32.to_bytes_little_endian (1 |> Uint32.of_int) data 0;
           assert_equal (Wav.read_wav_format data) PCM );
         ( "write_wav_format" >:: fun _ ->
           let data = Bytes.create 4 in
           Wav.write_wav_format PCM data;
           assert_equal (Wav.read_wav_format data) PCM );
       ]

let _ = run_test_tt_main suite
