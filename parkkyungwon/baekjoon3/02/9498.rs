use std::io::stdin;



fn main() {
    let mut input = String::new();
    let _ = stdin().read_line(&mut input);

    let score = input.trim().parse::<i32>().unwrap();
    let grade = if score >= 90 {
        "A"
    } else if score >= 80 {
        "B"
    } else if score >= 70 {
        "C"
    } else if score >= 60 {
        "D"
    } else {
        "F"
    };

    println!("{}", grade);
}
