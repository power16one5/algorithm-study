use std::io::{stdin, Read};



fn main() {
    let mut input = String::new();
    let _ = stdin().read_to_string(&mut input).unwrap();
    let nums = input.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    let answer = if nums[0] > 0 {
        if nums[1] > 0 {1} else {4}
    } else {
        if nums[1] > 0 {2} else {3}
    };

    println!("{}", answer);
}
