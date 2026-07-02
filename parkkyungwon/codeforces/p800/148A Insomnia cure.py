def gcd(a, b):
    while b:
        a, b = b, a % b
    
    return a


def inclu_exclu(arr, d):
    length = len(arr)
    total_dp = [0] * length

    def func(depth, i, w):
        next_depth = depth + 1

        for j in range(i, length):
            w2 = w * arr[j] // gcd(w, arr[j])
            total_dp[depth] += d // w2

            func(next_depth, j + 1, w2)
    
    func(0, 0, 1)

    total = 0
    for a in total_dp:
        total += a
        total = -total
    
    if total < 0: total = - total

    return total


def main():
    arr = list(map(int, open(0).read().split()))
    d = arr.pop()

    print(inclu_exclu(arr, d))


main()
