import sys



class SegmentTree():
    __slots__ = ['tree', 'lazy', 'adj', 's', 'e', 'v']

    def __init__(self, n):
        self.adj = 1 << n.bit_length()
        size = self.adj << 1
        self.tree = [0] * size
        self.lazy = [0] * size
    
    def _lazy_propagation(self, level, i, next_i1, next_i2):
        if self.lazy[i] == 1: self.tree[i] = level
        else: self.tree[i] = 0

        if i < self.adj:
            self.lazy[next_i1] = self.lazy[i]
            self.lazy[next_i2] = self.lazy[i]

        self.lazy[i] = 0
    
    def update(self, s, e, v):
        self.s, self.e, self.v = s, e, v
        self._update(self.adj, 1, 0, self.adj - 1)
    
    def _update(self, level, i, si, ei):
        next_i1 = i << 1
        next_i2 = next_i1 + 1
        next_level = level >> 1

        if si >= self.s and ei <= self.e:
            self.lazy[i] = self.v
            self._lazy_propagation(level, i, next_i1, next_i2)
            return
        
        if self.lazy[i]: self._lazy_propagation(level, i, next_i1, next_i2)
        if si > self.e or ei < self.s: return

        mid = (si + ei) >> 1
        self._update(next_level, next_i1, si, mid)
        self._update(next_level, next_i2, mid + 1, ei)
        self.tree[i] = self.tree[next_i1] + self.tree[next_i2]

    def query(self, s, e):
        self.s, self.e = s, e
        return self._query(self.adj, 1, 0, self.adj - 1)

    def _query(self, level, i, si, ei):
        next_i1 = i << 1
        next_i2 = next_i1 + 1
        next_level = level >> 1

        if si >= self.s and ei <= self.e:
            if self.lazy[i]: self._lazy_propagation(level, i, next_i1, next_i2)
            return self.tree[i]
        
        if self.lazy[i]: self._lazy_propagation(level, i, next_i1, next_i2)
        if si > self.e or ei < self.s: return 0 

        mid = (si + ei) >> 1
        left = self._query(next_level, next_i1, si, mid)
        right = self._query(next_level, next_i2, mid + 1, ei)
        return left + right


def euler_tour(n, start, edges):
    in_degree, out_degree = [None] * n, [None] * n
    degree = 0

    def dfs(u):
        nonlocal degree

        in_degree[u] = degree
        degree += 1

        for v in edges[u]:
            dfs(v)
        
        out_degree[u] = degree
    
    dfs(start)

    return in_degree, out_degree


def main():
    readline = sys.stdin.readline

    N = int(readline())
    arr = map(int, readline().split())
    next(arr)

    edges = [[] for _ in range(N + 1)]
    for i, v in enumerate(arr, 2):
        edges[v].append(i)
    
    in_degree, out_degree = euler_tour(N + 1, 1, edges)
    st = SegmentTree(N)
    st.update(0, N - 1, 1)

    M = int(readline())
    for _ in range(M):
        a, b = map(int, readline().split())
        b_in, b_out = in_degree[b] + 1, out_degree[b] - 1

        match a:
            case 1: st.update(b_in, b_out, 1)
            case 2: st.update(b_in, b_out, 2)
            case _: sys.stdout.write(str(st.query(b_in, b_out)) + '\n')


sys.setrecursionlimit(int(1e6))
main()
