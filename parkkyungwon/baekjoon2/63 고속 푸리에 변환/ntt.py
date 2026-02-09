import sys



def ntt(arr, inv=False):
    def func(arr, factor):
        half = len(arr) // 2

        if not half:
            return arr

        next_factor = (factor ** 2) % MOD

        even, odd = arr[::2], arr[1::2]
        func(even, next_factor); func(odd, next_factor)

        w = 1
        for i in range(half):
            u, v = even[i], (odd[i] * w) % MOD
            arr[i] = (u + v) % MOD
            arr[i + half] = (u - v) % MOD
            w = (w * factor) % MOD

    n = len(arr)
    MOD = 998244353
    factor = pow(3, (MOD - 1) // n * (-1 if inv else 1), MOD)
    func(arr, factor)

    if inv:
        inv_n = pow(n, -1, MOD)
        for i in range(n):
            arr[i] = (arr[i] * inv_n) % MOD
    

def main():
    readline = sys.stdin.readline
    
    n = int(readline())
    nums = [int(readline()) for _ in range(n)]
    fft_length = 1 << (2 * max(nums)).bit_length()

    arr = [0] * fft_length
    arr[0] = 1
    for i in nums:
        arr[i] = 1

    ntt(arr)
    for i in range(fft_length):
        arr[i] *= arr[i]
    ntt(arr, inv=True)
    
    m = int(readline())
    count = 0
    for _ in range(m):
        i = int(readline())
        if i < fft_length and int(arr[i].real + 0.5):
            count += 1

    print(count)


main()
