use std::io::stdin;



fn main() {
    let mut input = String::new();
    let _ = stdin().read_line(&mut input);

    let nums = input.split_whitespace()
    .map(|x| x.parse::<i32>().unwrap())
    .collect::<Vec<i32>>();

    let answer;
    if nums[0] > nums[1] {
        answer = ">".to_string();
    } else if nums[0] < nums[1] {
        answer = "<".to_string();
    } else {
        answer = "==".to_string();
    }

    println!("{}", answer);
}
