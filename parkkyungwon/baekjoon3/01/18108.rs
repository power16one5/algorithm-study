use std::io;



fn main() {
    let mut input = String::new();
    
    let _ = io::stdin().read_line(&mut input);
    let year = input.trim().parse::<i32>().unwrap() - 543;

    println!("{}", year);
    
}
