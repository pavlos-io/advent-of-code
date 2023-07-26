open Base

let lines = Stdio.In_channel.read_lines "../inputs/input2.txt"

let () = 
  lines
  |> List.map ~f: (fun line-> String.split line ' ')
  |> List.map ~f: (fun lst -> (List.nth_exn lst 0, List.nth_exn lst 1))
  |> List.iter ~f:(fun (a,b)-> Stdio.printf "%s %s\n" a b)
  |> List.fold_left ~f:score_round
  (* Printf.printf "Part 1: %d \n" 1 *)
  (* printf "Part 2: %d \n" @@ sum @@ List.take sorted_elves 3 *)