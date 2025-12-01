use std::collections::HashMap;

#[path = "../aoc_utils.rs"]
mod aoc_utils;

fn acc_round_pt1(acc: i32, round: &Vec<char>) -> i32 {
    let pts = HashMap::from([('X', 1), ('Y', 2), ('Z', 3)]);
    let translate = HashMap::from([('X', 'A'), ('Y', 'B'), ('Z', 'C')]);

    acc + pts.get(&round[1]).unwrap() + match round.as_slice() {
        ['C', 'X'] => 6,
        ['A', 'Y'] => 6,
        ['B', 'Z'] => 6,
        [x, y] if x == translate.get(y).unwrap() => 3,
        _ => 0,
    }
}

fn acc_round_pt2(acc: i32, round: &Vec<char>) -> i32 {
    let pts = HashMap::from([('A', 1), ('B', 2), ('C', 3)]);
    let beats = HashMap::from([('A', 'C'), ('B', 'A'), ('C', 'B')]);
    let loses = HashMap::from([('A', 'B'), ('B', 'C'), ('C', 'A')]);

    let (outcome_pts, my_choice) = match round.as_slice() {
        [op, 'X'] => (0, beats.get(&op).unwrap()),
        [op, 'Z'] => (6, loses.get(&op).unwrap()),
        [op, 'Y'] => (3, op),
        _ => panic!("Unknown round!")
    };
    
    acc + outcome_pts + pts.get(&my_choice).unwrap()
}

fn main() {
    let rounds: Vec<Vec<char>> = aoc_utils::get_input_lines(2)
        .iter()
        .map(|s| s.chars().filter(|c| !c.is_whitespace()).collect())
        .collect();

    println!("Part1: {:?}", rounds.iter().fold(0, acc_round_pt1));
    println!("Part2: {:?}", rounds.iter().fold(0, acc_round_pt2));
}

