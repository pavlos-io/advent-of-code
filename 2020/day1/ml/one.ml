let input_file = "../input.txt"

let read_whole_file (filename: string): string =
  let ch = open_in filename in
  let s = really_input_string ch (in_channel_length ch) in
  close_in ch;
  s


let get_input (filename: string): int list = 
  input_file
  |> read_whole_file
  |> String.split_on_char '\n'
  |> List.map int_of_string


let part_1 (nums: int list): int =
  List.fold_left (
    fun acc x -> 
    let combos = List.fold_left (fun acc2 y -> (x,y)::acc2) [] nums in
    List.append combos acc
  ) [] nums
  |> List.filter (fun (x,y) -> (x+y)=2020)
  |> List.map (fun (x,y) -> x*y)
  |> List.rev |> List.hd

let () = 
  let inp = get_input input_file in
  print_int (part_1 inp)