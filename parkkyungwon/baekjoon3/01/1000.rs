use std::io;



fn main() {
    let mut input = String::new();

    let _ = io::stdin().read_line(&mut input);
    let ret = input.split_whitespace().map(|x| x.parse::<i32>().unwrap()).sum::<i32>();

    println!("{}", ret);
}
