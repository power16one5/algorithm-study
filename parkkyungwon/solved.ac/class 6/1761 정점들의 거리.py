import sys



class LCA():
    def __init__(self, edge):
        leng = len(edge)
        self.depth, self.sparse, self.weight = [[0] * leng for _ in range(3)]
        self.depth[1], self.sparse[1] = 1, 1

        count = 2
        queue = [1]

        while queue:
            queue_tmp = []

            for q in queue:
                for e in edge[q]:
                    if self.depth[e]: continue

                    self.depth[e] = count
                    self.sparse[e] = q
                    self.weight[e] = edge[q][e]
                    queue_tmp.append(e)

            count += 1
            queue = queue_tmp

        self.sparse = [tuple(self.sparse)]
        self.weight = [tuple(self.weight)]

        for _ in range(count.bit_length() - 1):
            s, w = self.sparse[-1], self.weight[-1]
            self.weight.append(tuple(w[a] + b for a, b in zip(s, w)))
            self.sparse.append(tuple(s[a] for a in s))
        
    def find(self, a, b):
        total_weight = 0

        # a 와 b의 depth 맞춤
        if self.depth[a] != self.depth[b]:
            if self.depth[a] < self.depth[b]: a, b = b, a
            c = self.depth[a] - self.depth[b]

            while c:
                bit = (c & -c)
                bit_leng = bit.bit_length() - 1
                total_weight += self.weight[bit_leng][a]
                a = self.sparse[bit_leng][a]
                c -= bit
        
        if a != b:
            for asparse, aweight in zip(reversed(self.sparse), reversed(self.weight)):
                if asparse[a] != asparse[b]:
                    total_weight += aweight[a]
                    total_weight += aweight[b]
                    a, b = asparse[a], asparse[b]
        
            total_weight += self.weight[0][a]
            total_weight += self.weight[0][b]
            a, b = self.sparse[0][a], self.sparse[0][b]
        
        return total_weight


readline = sys.stdin.readline
N = int(readline())

edge = [{} for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, w = map(int, readline().split())
    edge[a][b] = w
    edge[b][a] = w

lca = LCA(edge)

M = int(readline())

for _ in range(M):
    a, b = map(int, readline().split())
    sys.stdout.write(str(lca.find(a, b)) + '\n')
