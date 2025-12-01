let input_file = "../input.txt"

type passport = string list

let read_whole_file (filename: string): string =
  let ch = open_in filename in
  let s = really_input_string ch (in_channel_length ch) in
  close_in ch;
  s


let get_input (filename: string): string list = 
  filename
  |> read_whole_file
  |> String.split_on_char '\n'


let assemble_passports (lines: string list): passport list =
  let rec f passports pass lns = 
    match lns with
    | [] -> pass :: passports
    | "" :: xs -> f (pass :: passports) [] xs
    | x :: xs -> f passports (List.append (String.split_on_char ' ' x) pass) xs
  in f [] [] lines

let is_pass_valid (p: passport): bool =
  p
  |> List.map (fun x -> List.hd (x |> String.split_on_char ':'))
  |> List.filter (fun x -> x <> "cid")
  |> List.length == 7

let part1 (passports: passport list): int = 
  passports
  |> List.map is_pass_valid
  |> List.filter (fun x -> x == true)
  |> List.length


let () = 
  input_file
  |> get_input
  |> assemble_passports
  |> part1
  |> print_int
  (* |> List.iter (fun p -> print_int (is_pass_valid p)) *)

  (* |> List.iter (fun p -> p |> List.iter print_endline) *)