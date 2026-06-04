def get_spf(n: int):
    length = n + 1
    dp = bytearray(0 for _ in range(length))

    for i in range(2, int(length ** 0.5)):
        if dp[i]: continue

        for j in range(i * i, length, i):
            if dp[j]: continue
            
            dp[j] = i
    
    return dp


def main():
    input()
    arr = list(map(int, input().split()))
    answer1, answer2 = [], []
    spf = get_spf(10000000)

    for a in arr:
        factor = spf[a]
        divisor = a
        while not divisor % factor:
            divisor //= factor

        if divisor == 1:
            answer1.append(-1)
            answer2.append(-1)

        else:
            answer1.append(factor)
            answer2.append(divisor)
    
    print(*answer1)
    print(*answer2)


main()
