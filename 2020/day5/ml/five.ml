let read_whole_file (filename: string): string =
  let ch = open_in filename in
  let s = really_input_string ch (in_channel_length ch) in
  close_in ch;
  s

let explode s =
  let rec exp i l =
   if i < 0 then l else exp (i - 1) (s.[i] :: l) in
  exp (String.length s - 1) [];;

let midpt (x: int) (y: int): float = (Float.of_int x +. Float.of_int y) /. 2.

let rd_up n = n |> Float.ceil |> Float.to_int
let rd_dn n = n |> Float.floor |> Float.to_int

let get_seat_id(pass: string): int =
  let rec run chars row col =
  let lrow, hrow = row and lcol, rcol = col in
  let row_midpt = (midpt lrow hrow) and col_midpt = (midpt lcol rcol) in
  match chars with
  | []            -> lrow * 8 + lcol
  | ('F' :: rest) -> run rest (lrow, rd_dn row_midpt) col
  | ('B' :: rest) -> run rest (rd_up row_midpt, hrow) col
  | ('L' :: rest) -> run rest row (lcol, rd_dn col_midpt)
  | ('R' :: rest) -> run rest row (rd_up col_midpt, rcol)
  | _             -> raise (Failure "Invalid character!") in
  run (explode pass) (0, 127) (0, 7)

let() =
  let ids = 
  "../input.txt"
  |> read_whole_file
  |> String.split_on_char '\n'
  |> List.map get_seat_id in
  
  ids |> List.fold_left max min_int |> print_int |> print_newline;
  
  let sorted = List.sort compare ids in
  List.iter2 (fun a b -> if b - a = 2 then print_int (b - 1)) sorted (List.tl sorted)
  |> print_newline