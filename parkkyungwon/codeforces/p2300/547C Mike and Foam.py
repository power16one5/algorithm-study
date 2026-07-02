import sys



def get_spf(length):
    spf = [0] * length

    for i in range(2, int(length ** (0.5)) + 1):
        for j in range(i * i, length, i):
            if spf[j]: continue

            spf[j] = i

    return spf


def get_factors(n, spf):
    factors = []

    while p := spf[n]:
        factors.append(p)
        while not n % p: n //= p

    if n > 1: factors.append(n)

    return factors


def get_inclusion_exclusion_divisors(factors):
    length = len(factors)
    odd, even = [], []

    def dfs(flag, i, w):
        next_flag = not flag

        for j in range(i, length):
            w2 = w * factors[j]
            if flag: even.append(w2)
            else: odd.append(w2)

            dfs(next_flag, j + 1, w2)
    
    dfs(False, 0, 1)

    return odd, even


def get_count(dp, odd, even):
    total = 0
    for a in odd: total += dp[a]
    for a in even: total -= dp[a]

    return total


def set_count(dp, odd, even, v):
    for a in odd: dp[a] += v
    for a in even: dp[a] += v


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    _, q = map(int, readline().split())
    arr = list(map(int, readline().split()))
    length = max(arr) + 1

    dp = [0] * length
    spf = get_spf(length)

    divisors_dp = {}
    for a in arr:
        if a in divisors_dp: continue
        divisors_dp[a] = get_inclusion_exclusion_divisors(get_factors(a, spf))
    
    mapping = [[]] + [divisors_dp[a] for a in arr]

    visited = bytearray(len(arr) + 1)
    in_the_shelf = 0
    count = 0

    for _ in range(q):
        i = int(readline())

        if visited[i]:
            set_count(dp, mapping[i][0], mapping[i][1], -1)
            in_the_shelf -= 1

            count -= in_the_shelf - get_count(dp, mapping[i][0], mapping[i][1])
        
        else:
            count += in_the_shelf - get_count(dp, mapping[i][0], mapping[i][1])

            set_count(dp, mapping[i][0], mapping[i][1], 1)
            in_the_shelf += 1

        visited[i] ^= 1
        write(str(count) + '\n')


main()
