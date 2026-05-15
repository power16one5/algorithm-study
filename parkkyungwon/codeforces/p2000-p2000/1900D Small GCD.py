import sys
from collections import defaultdict
 
 
 
def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    
    return a
 
 
def millar_rabin(n: int):
    if n < 2: return False
    if n < 4: return True

    n1 = n - 1
    d = (n1 & -n1).bit_length() - 1
    s = n1 >> d
 
    for a in 2, 3, 5, 7, 11:
        a = pow(a, s, n)
 
        if a == 1 or a == n1: continue
 
        for _ in range(d):
            a = (a ** 2) % n
            if a == n1: break
        
        else: return False
    
    return True
 
 
def pollard_rho(n: int):
    t = h = 2
    factor = 1
    for c in range(1, n):
        while factor == 1:
            t = (t * t + c) % n
            h = (h * h + c) % n
            h = (h * h + c) % n
    
            factor = gcd(t - h, n)
    
        if factor == n: factor = 1
        else: break
    
    return factor
 
 
def get_divisors(n: int):
    divisors = set([1])
    while n > 1:
        factor = n
        while not millar_rabin(factor):
            factor = pollard_rho(factor)
        
        while not n % factor:
            n //= factor

            divisors = divisors.union([d * factor for d in divisors])

    return divisors


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
 
    t = int(readline())
    for _ in range(t):
        total = 0
        n = int(readline())
        n1 = n - 1

        arr = sorted(map(int, readline().split()))
        arr.pop()
        divisors = [get_divisors(a) for a in arr]
        
        dp = defaultdict(int)
        for divisor in divisors:
            for d in divisor:
                dp[d] += 1
        
        write(str(total) + '\n')
 
 
main()
