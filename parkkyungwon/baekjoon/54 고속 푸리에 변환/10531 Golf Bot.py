import sys
from cmath import pi, exp



def bit_reverse(arr):
    leng = len(arr)
    j = 0

    for i in range(1, leng):
        bit = leng >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j: arr[i], arr[j] = arr[j], arr[i]


def cooley_tukey_fft(arr, inv=False):
    leng = len(arr)
    bit_reverse(arr)

    size, half = 2, 1
    two_pi = 2 * pi * (1 if inv else -1)
    while size <= leng:
        z = exp(complex(0, two_pi / size))

        for i in range(0, leng, size):
            w = 1

            for j in range(i, i + half):
                u = arr[j]
                v = arr[j + half] * w
                arr[j] = u + v
                arr[j + half] = u - v
                w *= z
        
        half = size
        size <<= 1
    
    return [a / leng for a in arr] if inv else arr


def main():
    readline = sys.stdin.readline

    N = int(readline())
    # leng = (1 << 19)
    leng = (1 << 5)
    arr = [0] * leng
    
    arr[0] = 1
    for _ in range(N):
        arr[int(readline())] = 1

    arr = cooley_tukey_fft(arr)
    for i in range(leng):
        arr[i] *= arr[i]
    arr = cooley_tukey_fft(arr, True)

    count = 0
    M = int(readline())
    for _ in range(M):
        if round(arr[int(readline())].real): count += 1

    print(count)


main()
