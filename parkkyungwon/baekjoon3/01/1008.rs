use std::io;



fn main() {
    let mut input = String::new();

    let _ = io::stdin().read_line(&mut input);
    let arr: Vec<i32> = input.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
    let answer = arr[0] as f64 / arr[1] as f64;

    println!("{}",  answer);
}
