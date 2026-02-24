import random



def sol(n):
    d = 2 * n + 1
    return d < 9 or miller_rabin(d)


def miller_rabin(n: int, k = 5):
    n1 = n - 1
    s = (n1 & -n1).bit_length()
    d = n1 >> (s - 1)

    for _ in range(k):
        x = pow(random.randint(2, n1), d, n)
        if x == 1 or x == n1: continue 

        for _ in range(s):
            x = x ** 2 % n
            if x == n1: break
        
        else: return False
    
    return True


def main():
    data = map(int, open(0).read().split())
    next(data)

    print(sum(map(sol, data)))


main()
