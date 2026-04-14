use std::io::stdin;



fn main() {
    let mut input = String::new();
    
    let _ = stdin().read_line(&mut input);
    let nums = input.trim().split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();

    let a = (nums[0] + nums[1]) % nums[2];
    let b = (nums[0] * nums[1]) % nums[2];

    print!("{}\n{}\n{}\n{}\n", a, a, b, b);
}
