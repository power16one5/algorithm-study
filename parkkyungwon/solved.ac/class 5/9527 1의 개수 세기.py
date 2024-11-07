def sol(a, b):
    leng = b.bit_length()
    dp = [0] * (leng + 1)
    dp[1] = 1

    for i in range(1, leng):
        dp[i+1] = 2*dp[i] + 2**i

    for i in range(leng + 1):
        dp[i] += 1

    def bit_count(i):
        leng = i.bit_length()
        total = 0
        count = 0

        for j in range(leng-1, -1, -1):
            if (i >> j) & 1:
                total += dp[j] + count * (1 << j)
                count += 1
        
        return total

    return bit_count(b) - bit_count(a-1)


A, B = map(int, input().split())

print(sol(A, B))
