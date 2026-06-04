use std::io::stdin;



fn get_sf() -> Vec<u32> {
    const LENGTH: usize = 10000001;
    let mut dp = vec![0u32; LENGTH];

    for i in 2..LENGTH {
        if dp[i] != 0 { continue }
        
        dp[i] = i as u32;

        for j in (i * i..LENGTH).step_by(i) {
            if dp[j] != 0 { continue }

            dp[j] = i as u32;
        }
    }

    dp
}


fn main() {
    let mut input = String::new();
    let _ = stdin().read_line(&mut input);
    input.clear();

    let _ = stdin().read_line(&mut input);
    let arr = input.split_whitespace()
    .map(|x| x.parse::<u32>().unwrap())
    .collect::<Vec<u32>>();

    let mut answer1: Vec<i32> = Vec::new();
    let mut answer2: Vec<i32> = Vec::new();

    let dp  = get_sf();

    for a in arr {
        let factor = dp[a as usize];
        let mut divisor = a;
        while divisor % factor == 0 { divisor /= factor }

        if divisor == 1 {
            answer1.push(-1);
            answer2.push(-1);
        } else {
            answer1.push(factor as i32);
            answer2.push(divisor as i32);
        }
    }

    for avec in [answer1, answer2] {
        println!("{} ", avec.iter( )
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(" "));
    }
}
