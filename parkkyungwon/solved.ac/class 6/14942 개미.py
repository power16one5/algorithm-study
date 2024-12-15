import sys



class SparseTable():
    def __init__(self, n, edge):
        self.sparse = [None] * n
        self.sparse[0], self.sparse[1] = 0, 1
        self.weight = [0] * n
        queue = [1]
        count = 0

        while queue:
            count += 1
            queue_tmp = []

            for a in queue:
                for b in edge[a]:
                    if self.sparse[b] is not None: continue

                    self.sparse[b] = a
                    self.weight[b] = edge[a][b]
                    queue_tmp.append(b)
            
            queue = queue_tmp

        self.sparse = [tuple(self.sparse)]
        self.weight = [tuple(self.weight)]

        for _ in range(count.bit_length()):
            si, wi = self.sparse[-1], self.weight[-1]
            self.sparse.append(tuple(si[a] for a in si))
            self.weight.append(tuple(wi[a] + b for a, b in zip(si, wi)))
    
    def move(self, start, rest):
        for si, wi in zip(reversed(self.sparse), reversed(self.weight)):
            if wi[start] <= rest:
                rest -= wi[start]
                start = si[start]
        
        return start


def sol(edge, arr):
    st = SparseTable(N + 1, edge)

    return (st.move(i, w) for i, w in enumerate(arr, 1))


readline = sys.stdin.readline
N = int(readline())

arr = [int(readline()) for _ in range(N)]

edge = tuple({} for _ in range(N + 1))
for _ in range(N - 1):
    a, b, c = map(int, readline().split())
    edge[a][b] = c; edge[b][a] = c

print(*sol(edge, arr), sep='\n')
