use std::collections::HashSet;

#[path = "../aoc_utils.rs"]
mod aoc_utils;

fn get_commonc(v: &Vec<HashSet<char>>) -> u32 {
    let mut hs: HashSet<char> = v[0].clone();

    for i in 1..v.len() {
        hs = hs.intersection(&v[i]).cloned().collect();
    }
    
    let c = *hs.iter().next().unwrap();
    let cu = c as u32;
    
    if c.is_uppercase() {cu - 38} else {cu - 96}
}

fn main() {
    let inp = aoc_utils::get_input_lines(3);
    let splits: Vec<Vec<HashSet<char>>> = inp
        .iter()
        .map(|s| s.split_at(s.len() / 2))
        .map(|(a, b)| vec![HashSet::from_iter(a.to_string().chars()), 
            HashSet::from_iter(b.to_string().chars())])
        .collect();
    
        let commons: Vec<u32> = splits
        .iter()
        .map(get_commonc)
        .collect();
    
    println!("Part1: {:?}", commons.iter().sum::<u32>());
    
    let mut commons2: u32 = 0;
    for chunk in inp.as_slice().chunks(3) {
        let hs:Vec<HashSet<char>> = chunk.iter()
        .map(|c| HashSet::from_iter(c.to_string().chars()))
        .collect();

        commons2 += get_commonc(&hs);
    }
    println!("Part2: {:?}", commons2);
}

