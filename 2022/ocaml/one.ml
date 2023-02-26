open Base

let lines = Stdio.In_channel.read_lines "../inputs/input1.txt"
let make_groups lst = 
  let rec aux group groups items =
    match items with
    []           -> groups
    | "" :: rest -> aux [] (group :: groups) rest
    | x :: rest  -> aux (x :: group) groups rest
  in aux [] [] lst

let get_sorted_elves lines = 
  lines
  |> make_groups
  |> List.map ~f: (fun group -> 
    List.fold_left group ~init:0 ~f:(fun acc x -> acc + Int.of_string x))
  |> List.sort ~compare: (fun x y -> if x < y then 1 else -1)

let sum = List.reduce_exn ~f:(+)

let () = 
  let sorted_elves = get_sorted_elves lines in
  printf "Part 1: %d \n" @@ List.hd_exn sorted_elves;
  printf "Part 2: %d \n" @@ sum @@ List.take sorted_elves 3