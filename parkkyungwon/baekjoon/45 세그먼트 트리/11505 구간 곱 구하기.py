import sys



class SegmentTree():
    def __init__(self, data):
        self.comp = len(data) 
        self.dp = ([0] * self.comp) + data

        for i in range(len(self.dp) - 1, 0, -2):
            self.dp[i >> 1] = self.dp[i] * self.dp[i-1] % MOD

    def update(self, i, v):
        i += self.comp

        if self.dp[i]:
            inv = pow(self.dp[i], -1, MOD)
            self.dp[i] = v
            d = v * inv % MOD

            while i:
                i >>= 1
                self.dp[i] = self.dp[i] * d % MOD

        else:
            self.dp[i] = v

            while i:
                i >>= 1; j = i << 1
                self.dp[i] = self.dp[j] * self.dp[j+1] % MOD

    def interval_sum(self, s, e):
        total = 1
        s += self.comp; e+= self.comp

        while s <= e:
            if s & 1:
                total = total * self.dp[s] % MOD
                s += 1
            
            if not(e & 1):
                total = total * self.dp[e] % MOD
                e -= 1
            
            s >>= 1; e >>= 1
        
        return total


readline = sys.stdin.readline
MOD = int(1e9) + 7

N, M, K = map(int, readline().split())

st = SegmentTree([1] + [int(readline()) for _ in range(N)])

for _ in range(M + K):
    op, a, b = map(int, readline().split())

    if op == 1: st.update(a, b)
    else: sys.stdout.write(str(st.interval_sum(a, b)) + '\n')
