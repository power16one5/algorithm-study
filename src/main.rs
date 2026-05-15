use std::io::stdin;



fn pow(mut base: u64, mut exp: u64, m: u64) -> u64 {
    let mut total: u64= 1;

    while exp > 0 {
        if exp & 1 == 1 { total = total * base % m }
        exp >>= 1;
        base = base * base % m;
    }
    
    total
}

fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b > 0 { (a, b) = (b, a % b) }

    a
}


fn millar_rabin(n: u64) -> bool {
    if n < 2 { return false }
    if n < 4 { return true }

    let n1: u64 = n as u64 - 1;
    let d = n1.trailing_zeros();
    let s = n1 >> d;

    for mut a in [2_u64, 3, 5, 7, 11] {
        if a >= n { break }
        a = pow(a, s, n);

        if a == 1 || a == n1 { continue }

        let mut flag = true;
        for _ in 0..d {
            a = a * a % n;
            if a == n1 { 
                flag = false;
                break;
            }
        }

        if flag { return false }
    }

    true
}


fn pollard_rho(n: u64) -> u64{
    if n & 1 != 1 { return 2 }

    let (mut t, mut h) = (2, 2);
    let mut factor = 1;
    for c in 1..n {
        while factor == 1 {
            t = (t * t + c) % n;
            h = (h * h + c) % n;
            h = (h * h + c) % n;

            factor = gcd(if t > h { t - h } else {h - t}, n);
        }

        if factor == n { factor = 1 }
        else { break }
    }

    factor
}


fn get_divisors(mut n: u64) -> Vec<u64> {
    let mut divisors = vec![1u64];

    while n != 1 {
        let mut factor = n;
        while !millar_rabin(factor) { factor = pollard_rho(factor) }

        let mut count = 0;
        while n % factor == 0 {
            n /= factor;
            count += 1
        }
        
        let end: usize = divisors.len();
        let mut mul: u64 = 1;

        for _ in 0..count {
            mul *= factor;

            for i in 0..end {
                divisors.push(divisors[i] * mul);
            }
        }
    }

    divisors
}


struct TwoCombSum {
    arr: Vec<u64>,
    i: usize,
    j: usize,
    iend: usize,
}


impl TwoCombSum {
    fn new(arr: Vec<u64>, start: usize) -> Self {
        let iend = arr.len() - 1;

        Self {
            arr,
            i: start,
            j: start + 1,
            iend: iend,
        }
    }
}

impl Iterator for TwoCombSum {
    type Item = (u64, u64);

    fn next(&mut self) -> Option<Self::Item> {
        if self.i >= self.iend {
            return None;
        }

        let (a, b) = (self.arr[self.i], self.arr[self.j]);

        self.j += 1;
        if self.j == self.arr.len() {
            self.i += 1;
            self.j = self.i + 1;
        }


        Some((a, b))
    }
}


fn main() {
    let mut input = String::new();
    let _ = stdin().read_line(&mut input);
    input.clear();

    let _ = stdin().read_line(&mut input);
    let arr = input.split_whitespace()
    .map(|x| x.parse::<u64>().unwrap())
    .collect::<Vec<u64>>();

    let mut answer1: Vec<i64> = Vec::new();
    let mut answer2: Vec<i64> = Vec::new();

    for avec in arr.iter()
    .map(|x| get_divisors(*x)) {
        let n = avec[avec.len() - 1];
        let mut flag = true;
        for (a, b) in TwoCombSum::new(avec, 1) {
            if gcd(a + b, n) == 1 {
                answer1.push(a as i64); answer2.push(b as i64);
                flag = false;
                break; 
            }
        }

        if flag { answer1.push(-1); answer2.push(-1); }
    }

    for avec in [answer1, answer2] {
        println!("{} ", avec.iter( )
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(" "));
    }
}
