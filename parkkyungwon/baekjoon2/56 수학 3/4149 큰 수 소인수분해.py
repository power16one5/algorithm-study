import random
import sys



def get_gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a


def pollard_rho(n):
    if not n & 1: return 2

    c, gcd = 0, 1
    f = lambda x: (x * x + c) % n
    f_sq = lambda x: f(f(x))

    while True:
        c += 1
        t, h = 0, 0

        while gcd == 1:
            t, h = f(t), f_sq(h)
            if t == h: break
            gcd = get_gcd(t - h if t > h else h - t, n)
        
        else: return gcd
    


def millar_rabin(n, k=5):
    if n < 2: return False
    elif n < 4: return True
    
    n1 = n - 1
    s = (n1 & -n1).bit_length() - 1
    d = n1 >> s

    for _ in range(k):
        x = pow(random.randint(2, n1), d, n)
        if x == 1 or x == n1: continue

        for _ in range(s):
            x = x ** 2 % n
            if x == n1: break
        
        else: return False
    
    return True


def find_factor(n):
    divisor = [n]
    factor = []

    while divisor:
        d = divisor[-1]

        if d == 1: 
            divisor.pop()
            continue

        elif millar_rabin(d): 
            for i in range(len(divisor)):
                while not divisor[i] % d:
                    factor.append(d)
                    divisor[i] //= d

        else:
            d2 = pollard_rho(d)
            divisor[-1] //= d2
            divisor.append(d2)

    factor.sort()

    return factor


def main():
    global write
    write = sys.stdout.write
    n = int(input())

    print(*find_factor(n), sep='\n')


main()
