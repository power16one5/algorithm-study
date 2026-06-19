def main():
    n = int(input("Enter a odd number: "))
    if not n & 1:
        print("Please enter an odd number.")
        return
    
    length = n ** 2 + 1
    dp = bytearray(length)

    for i in range(2, length):
        if dp[i]: continue

        for j in range(i * i, length, i):
            dp[j] = 1
    
    output = [[0] * n for _ in range(n)]
    x = y = (n >> 1) - 1
    i = 1; d = 1

    for j in range(2, n, 2):
        for _ in range(2):
            for _ in range(j):
                i += 1; x += d
                if not dp[i]: output[y][x] = i

            for _ in range(j):
                i += 1; y += d
                if not dp[i]: output[y][x] = i
                
            d = -d
        x -= 1; y -= 1
    
    for a in output:
        print(" ".join(str(x).ljust(4) for x in a))


main()
