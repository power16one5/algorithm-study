import random



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


def main():
    n = int(input())
    if not n & 1: n += 1

    dp = [[None] * n for _ in range(n)]

    d = 1
    count = 1
    i = j = n // 2

    for limit in range(1, n):
        for _ in range(limit):
            dp[i][j] = 'x' if millar_rabin(count) else 'O'
            count += 1
            j += d
    
        for _ in range(limit):
            dp[i][j] = 'x' if millar_rabin(count) else 'O'
            count += 1
            i += d
        
        d = -d
    
    for _ in range(limit + 1):
        dp[i][j] = 'x' if millar_rabin(count) else 'O'
        count += 1
        j += d
    
    dp[n // 2][n // 2] = '-'

    print(*(i for i in range(n + 1)))
    for i, a in enumerate(dp, 1):
        print(f'{i:<2}', *a)


main()
