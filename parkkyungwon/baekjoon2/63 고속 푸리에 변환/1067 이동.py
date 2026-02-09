class NTT:
    def __init__(self, n):
        self.MOD = 998244353
        self.n = n
        self.n_inv = pow(n, self.MOD - 2, self.MOD)
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
        w = pow(3, (self.MOD - 1) // self.n, self.MOD)
        factors = [1] * self.n 

        for i in range(self.n - 1):
            factors[i + 1] = (factors[i] * w) % self.MOD

        return factors

    def transform(self, arr, inv=False):
        self.bit_reverse(arr)

        step, half_step, f_step = 2, 1, (self.n >> 1) * (-1 if inv else 1)
        while step <= self.n:
            for i in range(0, self.n, step):
                c = 0
                for a in range(i, i + half_step):
                    b = a + half_step

                    u, v = arr[a], (arr[b] * self.factors[c]) % self.MOD
                    arr[a], arr[b] = (u + v) % self.MOD, (u - v) % self.MOD
    
                    c += f_step

            step, half_step, f_step = step << 1, step, f_step >> 1

        if inv:
            for i in range(self.n):
                arr[i] = (arr[i] * self.n_inv) % self.MOD


def main():
    n = int(input())
    ntt_length = 1 << (2 * n).bit_length()

    A = list(map(int, input().split())) + [0] * (ntt_length - n)
    B = list(map(int, input().split()))[::-1] + [0] * (ntt_length - n)
    ntt = NTT(ntt_length)

    ntt.transform(A); ntt.transform(B)
    for i in range(ntt_length):
        A[i] = (A[i] * B[i]) % ntt.MOD
    ntt.transform(A, inv=True)

    print(max(A[i] + A[i + n] for i in range(n)))


main()
