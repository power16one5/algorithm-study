import sys



def ex_euclid(a, b):
    c, d = 1, 0
    while b:
        a, b, c, d = b, a % b, d, c - d*(a//b)
    
    return a, c


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    amax = int(1e9)
    
    T = int(readline())
    for _ in range(T):
        K, C = map(int, readline().split())
        
        answer = 'IMPOSSIBLE\n'
        if C == 1:
            if K < amax:
                answer = str(K + 1) + '\n'
            
        elif K == 1: 
            answer = '1\n'

        else:
            gcd, inv = ex_euclid(C, K)

            if gcd == 1:
                answer = str(inv % K) + '\n'

        write(answer)


main()
