import random
import sys



def get_gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a


def pollard_rho(n):
    if not n & 1: return 2
    
    t, h, gcd = 0, 0, 1
    while True:
        c = random.randint(1, n - 1)

        while gcd == 1:
            t = (t * t + c) % n
            h = (h * h + c) % n
            h = (h * h + c) % n
            gcd = get_gcd(t - h if t > h else h - t, n)
        
        if gcd == n: gcd = 1
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
            factor.append(d)
            for i in range(len(divisor)):
                while not divisor[i] % d:
                    divisor[i] //= d

        else:
            d2 = pollard_rho(d)
            divisor[-1] //= d2
            divisor.append(d2)

    return factor


def main():
    global write
    write = sys.stdout.write
    n = int(input())

    total = n
    for f in find_factor(n):
        total //= f
        total *= f - 1

    print(total, sep='\n')


main()
