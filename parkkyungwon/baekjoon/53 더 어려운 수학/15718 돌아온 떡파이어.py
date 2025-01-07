import sys
from math import log, factorial



def lucas(n, m, mod):
    digit = mod ** int(log(n, mod))
    total = 1

    def fac(n):
        return factorial(n) % mod

    def inv(n):
        return pow(factorial(n) % mod, -1, mod)

    while digit:
        numer = n // digit
        denom = m // digit

        if numer < denom: return 0


        total = (total * fac(numer) * inv(denom) * inv(numer - denom)) % mod
        
        n -= numer * digit
        m -= denom * digit
        digit //= mod
    
    return total
    

def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    T = int(readline())
    for _ in range(T):
        N, M = map(int, readline().split())

        if (N - M + 1) < 0 or (M == 1 and N):
            write('0\n')

        elif N > 1 and M > 2:
            N -= 1; M -= 2
            mod1, mod2 = 97, 1031
            a1 = lucas(N, M, mod1)
            a2 = lucas(N, M, mod2)

            k = (a2 - a1) * pow(mod1, -1, mod2)
            c = (mod1 * k + a1) % (mod1 * mod2)

            write(str(c) + '\n')
        
        else:
            write('1\n')


main()
