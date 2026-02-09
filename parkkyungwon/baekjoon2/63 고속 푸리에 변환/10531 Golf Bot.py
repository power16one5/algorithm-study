import cmath
import sys



class FFT:
    def __init__(self, n):
        self.n = n
        self.bit_reverse = self.make_bit_reverse()
        self.factors = self.make_factors()

    def make_bit_reverse(self):
        visited = bytearray(self.n)
        A, B = [], []

        b, start_bit = 0, self.n >> 1
        for a in range(1, self.n):
            bit = start_bit
            while b & bit:
                b ^= bit
                bit >>= 1
            b |= bit

            if visited[a] or a == b: continue
            visited[b] = 1
            A.append(a), B.append(b)

        def bit_reverse(arr):
            for a, b in zip(A, B):
                arr[a], arr[b] = arr[b], arr[a]

        return bit_reverse
    
    def make_factors(self):
        half, quad = self.n >> 1, self.n >> 2
        w = cmath.exp(1j * 2 * cmath.pi / self.n)

        factors = [1] * self.n
        factors[quad], factors[half], factors[-quad] = 1j, -1, -1j

        for i in range(1, quad):
            factors[i] = factors[i - 1] * w
            factors[-i] = factors[i].conjugate()
            factors[half - i] = -factors[-i]
            factors[half + i] = -factors[i]

        return factors

    def transform(self, arr, inv=False):
        self.bit_reverse(arr)

        step, half_step, f_step = 2, 1, (self.n >> 1) * (-1 if inv else 1)
        while step <= self.n:
            for i in range(0, self.n, step):
                c = 0
                for a in range(i, i + half_step):
                    b = a + half_step

                    u, v = arr[a], arr[b] * self.factors[c]
                    arr[a], arr[b] = u + v, u - v
    
                    c += f_step

            step, half_step, f_step = step << 1, step, f_step >> 1

        if inv:
            for i in range(self.n):
                arr[i] /= self.n


def main():
    readline = sys.stdin.readline
    
    n = int(readline())
    nums = [int(readline()) for _ in range(n)]
    fft_length = 1 << (2 * max(nums)).bit_length()
    fft = FFT(fft_length)

    arr = [0] * fft_length
    arr[0] = 1
    for i in nums:
        arr[i] = 1

    fft.transform(arr)
    for i in range(fft_length):
        arr[i] *= arr[i]
    fft.transform(arr, inv=True)
    
    m = int(readline())
    count = 0
    for _ in range(m):
        i = int(readline())
        if i < fft_length and int(arr[i].real + 0.5):
            count += 1

    print(count)


main()
