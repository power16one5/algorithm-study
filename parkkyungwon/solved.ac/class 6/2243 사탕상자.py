import sys



class SegmentTree():
    def __init__(self):
        self.adj = 1 << int(1e6).bit_length()
        self.dp = [0] * (2*self.adj)

    def add(self, i, v):
        i += self.adj

        while i:
            self.dp[i] += v
            i >>= 1

    def sub(self, v):
        i = 1
        self.dp[1] -= 1

        while i < self.adj:
            i <<= 1

            if v > self.dp[i]:
                v -= self.dp[i]
                i += 1

            self.dp[i] -= 1

        return i - self.adj


readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
st = SegmentTree()

for _ in range(N):
    op = list(map(int, readline().split()))

    if op[0] == 1: write(str(st.sub(op[1])) + '\n')
    else: st.add(op[1], op[2])
