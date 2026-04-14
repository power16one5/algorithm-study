use std::io::stdin;



fn main() {
    let mut input = String::new();
    let _ = stdin().read_line(&mut input);
    
    let answer = input.split_whitespace().map(|x| x.parse::<i64>().unwrap())
        .sum::<i64>();

    println!("{}", answer);
}
