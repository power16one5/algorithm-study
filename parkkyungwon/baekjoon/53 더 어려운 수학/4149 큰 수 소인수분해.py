import math
import random



def miller_rabin(n, count):
    if n < 4: return True

    nm1 = n - 1
    odd = nm1
    ex = 0
    while not (odd & 1):
        ex += 1; odd >>= 1
    
    for _ in range(count):
        r = random.randint(2, n - 2)
        r = pow(r, odd, n)

        if r == 1: continue

        for _ in range(ex):
            if r == nm1: break
            r = (r * r) % n
        
        else: return False
    
    return True


def f(x): 
    return (x*x + 1)


def pollards_rho(n):
    if not (n & 1): return 2

    while True:
        a = random.randint(2, n - 1)
        b = a
        c = random.randint(1, n)
        g = 1

        while g == 1:
            a = (a * a + c) % n
            b = (b * b + c) % n
            b = (b * b + c) % n
            g = math.gcd(a - b if a > b else b - a, n)

        if g != n: return g


def main():
    N = int(input())
    answer = []

    while not miller_rabin(N, 5):
        factor = pollards_rho(N)
        while not miller_rabin(factor, 5):
            factor = pollards_rho(factor)

        while not (N % factor):
            answer.append(factor)
            N //= factor
        
    if N != 1: answer.append(N)
    answer.sort()

    print(*answer, sep='\n')


main()
