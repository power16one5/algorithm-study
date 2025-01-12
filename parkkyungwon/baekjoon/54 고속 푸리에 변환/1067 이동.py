from cmath import pi, exp



def reverse_bit(arr):
    leng = len(arr)
    j = 0

    for i in range(1, leng):
        bit = leng >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j: arr[i], arr[j] = arr[j], arr[i]


def fft(arr, inv=False):
    leng = len(arr)
    reverse_bit(arr)

    step, half_step = 2, 1
    two_pi = 2 * pi * (1 if inv else - 1)
    while step <= leng:
        z = exp(complex(0, two_pi / step))

        for i in range(0, leng, step):
            w = 1

            for j in range(i, i + half_step):
                k = j + half_step
                u, v = arr[j], arr[k] * w
                arr[j], arr[k] = u + v, u - v
                w *= z
        
        half_step, step = step, step << 1
    
    if inv: 
        for i, v in enumerate(arr): arr[i] /= leng
        
    return arr


def main():
    N = int(input())
    leng = 1 << (N << 1).bit_length()
    padding = [0] * (leng - N)
    A = list(map(int, input().split())) + padding
    B = list(map(int, input().split()))[::-1] + padding

    fft(A), fft(B)
    for i in range(leng):
        A[i] *= B[i]
    fft(A, True)

    amax = A[N-1].real
    for i in range(N - 1):
        v = A[i].real + A[N + i].real
        if amax < v: amax = v

    print(round(amax))


main()
