import sys, cmath



def fft(arr, inv=False):
    def func(arr, factor):
        half = len(arr) // 2

        if not half:
            return arr

        next_factor = factor ** 2

        even, odd = arr[::2], arr[1::2]
        func(even, next_factor); func(odd, next_factor)

        w = 1
        for i in range(half):
            u, v = even[i], odd[i] * w
            arr[i] = u + v
            arr[i + half] = u - v
            w *= factor

    n = len(arr)
    factor = cmath.exp(1j * 2 * cmath.pi / n * (-1 if inv else 1))
    func(arr, factor)

    if inv:
        for i in range(n):
            arr[i] /= n
    

def main():
    readline = sys.stdin.readline
    
    n = int(readline())
    nums = [int(readline()) for _ in range(n)]
    fft_length = 1 << (2 * max(nums)).bit_length()

    arr = [0] * fft_length
    arr[0] = 1
    for i in nums:
        arr[i] = 1

    fft(arr)
    for i in range(fft_length):
        arr[i] *= arr[i]
    fft(arr, inv=True)
    
    m = int(readline())
    count = 0
    for _ in range(m):
        i = int(readline())
        if i < fft_length and int(arr[i].real + 0.5):
            count += 1

    print(count)


main()
