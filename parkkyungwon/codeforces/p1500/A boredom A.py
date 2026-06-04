def main():
    _ = int(input())
    n = 100001
    dp = [0] * n
    dp2 = [0] * n

    for i in map(int, input().split()):
        dp[i] += i

    for i in range(n - 3):
        dp[i] += dp2[i]

        j = i + 2
        if dp[j] < dp[i]:
            dp[j] = dp[i]

        j = i + 3
        if dp[j] < dp[i]:
            dp[j] = dp[i]

    print(max(dp[-2], dp[-1]))


main()
