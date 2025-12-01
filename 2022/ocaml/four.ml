open Base

let lines = Stdio.In_channel.read_lines "../inputs/input4.txt"

type rng_pair = {
  a: (int * int);
  b: (int * int);
}

let is_contained {a = (x1, y1); b = (x2, y2)} =
  (x1 >= x2 && y1 <= y2) || (x2 >= x1 && y2 <= y1)

let has_overlap {a; b} =
  let overlap (x1, y1) (x2, y2) = (x2 <= x1 && x1 <= y2) || (x2 <= y1 && y1 <= y2) in
  overlap a b || overlap b a

let parse_line ln =
  let rngs = 
    String.split ln ~on:','
    |> List.map ~f: (fun rng -> String.split rng ~on:'-' |> List.map ~f: Int.of_string) in
  match rngs with
    [[x1 ; y1]; [x2 ; y2]] -> {a = (x1, y1); b = (x2, y2)}
    | _ -> assert false

let () =
  let rng_pairs = lines |> List.map ~f: parse_line in
  let p1 = rng_pairs |> List.filter ~f: is_contained
  and p2 = rng_pairs |> List.filter ~f: has_overlap in
  printf "Part 1: %d \n" @@ List.length p1;
  printf "Part 2: %d \n" @@ List.length p2