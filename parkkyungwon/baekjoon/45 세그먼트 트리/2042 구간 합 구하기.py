import sys



class Segment_Tree():
    def __init__(self, data):
        self.comp = len(data)
        self.segtree = ([0] * self.comp) + data

        for i in range(len(self.segtree) - 2, 0, -2):
            self.segtree[i >> 1] = self.segtree[i] + self.segtree[i+1]
        
    def update(self, i, v):
        j = self.comp + i
        d = v - self.segtree[j]
        self.segtree[j] = v

        while j:
            j //= 2
            self.segtree[j] += d
        
    def interval_sum(self, s, e):
        total = 0
        s += self.comp
        e += self.comp

        while s <= e:
            if s & 1:
                total += self.segtree[s]
                s += 1
            
            if not(e & 1):
                total += self.segtree[e]
                e -= 1
            
            s >>= 1; e >>= 1

        return total


readline = sys.stdin.readline
N, M, K = map(int, readline().split())

st = Segment_Tree([0] + [int(readline()) for _ in range(N)])

for _ in range(M + K):
    op, a, b = map(int, readline().split())

    if op == 1: st.update(a, b)
    else: sys.stdout.write(str(st.interval_sum(a, b)) + '\n')
