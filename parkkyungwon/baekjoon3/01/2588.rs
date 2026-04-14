use std::io::{self, Read};



fn main() {
    let mut input = String::new();
    let _ = io::stdin().read_to_string(&mut input);
    let nums = input.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();
    let (a, b) = (nums[0], nums[1]);

    for i in 0..3 {
        let b1 = (b / 10_i32.pow(i)) % 10 * a;

        println!("{}", b1);
    }
    println!("{}", a * b);
}
