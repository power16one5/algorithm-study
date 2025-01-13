from cmath import exp, pi



def reverse_bit(leng):
    reverse_arr = [i for i in range(leng)]
    half, j = leng >> 1, 0

    for i in range(1, leng):
        bit = half
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j: reverse_arr[i], reverse_arr[j] = reverse_arr[j], reverse_arr[i]
    
    def func(arr):
        for i, j in enumerate(reverse_arr):
            if i < j: arr[i], arr[j] = arr[j], arr[i]
    
    return func
            

def fft(arr, rev_func, inv=False):
    leng = len(arr)
    rev_func(arr)
    size, half = 2, 1
    two_pi = 2 * pi * (1 if inv else -1)

    while size <= leng:
        w = exp(complex(0, two_pi / size))

        for i in range(0, leng, size):
            pow_w = 1

            for j in range(i, i + half):
                k = j + half
                a, b = arr[j], arr[k] * pow_w
                arr[j] = a + b
                arr[k] = a - b
                pow_w *= w
        
        half, size = size, size << 1
    
    if inv: 
        for i in range(leng): arr[i] /= leng


def barrier(leng): 
    input()
    arr = [0] * leng

    for i in map(int, input().split()): 
        arr[i + 30000] = 1

    return arr


def main():
    leng = 1 << (120001).bit_length()
    rev_func = reverse_bit(leng)

    A = barrier(leng)
    B  = barrier(leng)
    C = barrier(leng)

    fft(A, rev_func); fft(C, rev_func)
    for i in range(leng): A[i] *= C[i]
    fft(A, rev_func, True)

    count = 0
    for i in range(60001): 
        if B[i]: count += A[i << 1].real
    
    print(round(count))


main()
