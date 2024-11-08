from collections import defaultdict



def sol(n):
    if n == 1: return 0

    dp = [{1 << i: 1} for i in range(10)]

    for _ in range(n-1):
        new_dp = [defaultdict(int) for _ in range(10)]

        for mask in dp[0]:
            new_dp[1][mask | 2] += dp[0][mask]

        for i in range(1, 9):
            for mask in dp[i]:
                new_dp[i-1][mask | 1 << (i-1)] += dp[i][mask]
                new_dp[i+1][mask | 1 << (i+1)] += dp[i][mask]

        for mask in dp[9]:
            new_dp[8][mask | 256] += dp[9][mask]
        
        for a in new_dp:
            for b in a:
                a[b] %= MOD

        dp = new_dp
    
    return sum(a[1023] for a in dp[1:]) % MOD


N = int(input())
MOD = int(1e9)

print(sol(N))
