use std::fs::File;
use std::io::{BufReader, Read};

pub fn get_input_str(day: u8) -> String {
    let input = match File::open(format!("inputs/input{}.txt", day)) {
        Ok(res) => res,
        Err(e) => panic!("Can't open input! {}", e)
    };

    let mut buff = BufReader::new(input);
    let mut input_str = String::new();
    buff.read_to_string(&mut input_str).expect("err");
    input_str
}

// pub fn get_input_lines(day: u8) -> Vec<String> {
//     get_input_str(day).split("\n").map(str::to_string).collect()
// }

// pub fn get_input_chunks(day: u8) -> Vec<String> {
//     get_input_str(day).split("\n\n").map(str::to_string).collect()
// }

pub fn get_input_2d_ivec(day: u8) -> Vec<Vec<i32>> {
    get_input_str(day)
        .split("\n\n")
        .map(|chunk| 
            chunk.split("\n")
            .map(|s| s.parse::<i32>().unwrap())
            .collect()
        )
        .collect()
}