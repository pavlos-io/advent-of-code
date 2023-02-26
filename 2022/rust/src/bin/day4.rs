#[path = "../aoc_utils.rs"]
mod aoc_utils;

#[derive(Debug)]
struct Range {
    start: i32,
    end: i32,
}

fn main() {
    let inp = aoc_utils::get_input_lines(4);
    let splits: Vec<_> = inp
        .iter()
        .map(|s| s.split(",")
            .map(|r| r.split("-")
                .map(|i| i.parse().unwrap())
                .collect::<Vec<i32>>()
            ).map(|v| Range{start:v[0], end:v[1]})
            .collect::<Vec<Range>>()
        )
        .collect();
    
    let mut cnt = 0;
    for elf in splits.as_slice() {
        match elf.as_slice() {
            [Range{start: a, end: b}, Range{start: c, end: d}] 
                if (a <= c && d <= b) ||
                    (c <= a && b <= d) => cnt += 1,
            _ => println!("no")
        }
    }
    
    println!("Part1: {:?}", cnt);
    cnt = 0;
    for elf in splits.as_slice() {
        match elf.as_slice() {
            [Range{start: a, end: b}, Range{start: c, end: d}] 
                if (a <= c && c <= b) || (a <= d && d <= b) 
                    || (c <= a && a <= d) || (c <= b && b <= d) => cnt += 1,
            _ => println!("no")
        }
    }

    println!("Part2: {:?}", cnt);
}

