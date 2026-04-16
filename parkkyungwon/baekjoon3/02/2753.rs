use std::io::stdin;



fn main() {
    let mut input = String::new();
    let _ = stdin().read_line(&mut input);
    let year = input.trim().parse::<i32>().unwrap();

    if year % 400 == 0 || (year % 100 != 0 && year % 4 == 0) {
        println!("1");
    } else {
        println!("0");
    }
}
