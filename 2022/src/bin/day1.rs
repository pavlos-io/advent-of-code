#[path = "../aoc_utils.rs"]
mod aoc_utils;

fn main() {
    // Part 1
    let mut elf_cals: Vec<i32> = aoc_utils::get_input_chunks(1)
        .iter()
        .map(|elf| elf.split("\n")
            .map(|cal| cal.parse::<i32>().unwrap())
            .sum()
        ).collect();
    
    println!("Part1: {:?}", elf_cals.iter().max().unwrap());

    // Part 2
    elf_cals.sort();
    elf_cals.reverse();
    
    println!("Part2: {:?}", elf_cals.iter().take(3).sum::<i32>());
}

