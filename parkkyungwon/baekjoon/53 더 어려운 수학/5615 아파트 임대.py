import sys
import random



def miller_rabin(n, k):
    nm1 = n - 1
    d = nm1
    ex = 0 

    while not(d & 1):
        d >>= 1; ex += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        r = pow(a, d, n)

        if r == 1: continue

        for _ in range(ex):
            if r == nm1: break

            r = pow(r, 2, n)
        
        else: return False
    
    return True


def main():
    readline = sys.stdin.readline

    N = int(readline())
    impossible_count = 0

    for _ in range(N):
        a = 2*int(readline()) + 1

        if miller_rabin(a, 5): impossible_count += 1

    print(impossible_count)


main()
