use std::io::stdin;



fn main() {
    let mut input = String::new();
    let _ = stdin().read_line(&mut input);

    let mut iter = input.split_whitespace()
        .map(|x| x.parse::<i32>().unwrap());

    let mut h = iter.next().unwrap();
    let mut m = iter.next().unwrap();

    if m < 45 { h = (h + 23) % 24; };
    m = (m + 15) % 60;

    println!("{} {}", h, m);
}
