import sys



def main():
    readline = sys.stdin.readline
    
    N = int(readline())
    line = [bytearray(100) for _ in range(100)]
    dp = [[0] * 100 for _ in range(100)]
    for _ in range(N):
        a, b = map(lambda x: int(x) - 1, readline().split())
        if a > b: a, b = b, a
        line[a][b] = 1

    for size in range(1, 100):
        for s in range(100 - size):
            e = s + size

            for m in range(s + 1, e):
                v = dp[s][m] + dp[m][e]
                if dp[s][e] < v: dp[s][e] = v
            
            if line[s][e]: dp[s][e] += 1

    print(dp[0][-1])


main()
