def sol(arr):
    end = len(arr)
    dp = tuple([0] * end for _ in range(end))

    for i in range(end):
        dp[i][i] = 1

    for i in range(end - 1):
        j = i + 1
        dp[i][j] = 3 if arr[i] == arr[j] else 2

    for leng in range(2, end):
        for i in range(end - leng):
            j = i + leng

            if arr[i] == arr[j]:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] + 1) % MOD

            else:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
    
    return dp[0][-1]


MOD = int(1e4) + 7
arr = input().rstrip()

print(sol(arr))
