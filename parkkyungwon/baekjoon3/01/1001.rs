use std::io;



fn main() {
    let mut input = String::new();

    let _ = io::stdin().read_line(&mut input);
    let ret: Vec<i32> = input.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();

    println!("{}", ret[0] - ret[1]);
}
