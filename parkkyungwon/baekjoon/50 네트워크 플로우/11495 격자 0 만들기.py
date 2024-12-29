import sys



class Edge():
    __slots__ = ['to', 'rev', 'cap']

    def __init__(self, to, cap):
        self.to, self.cap = to, cap


class Dinic():
    __slots__ = ['graph', 'graph_len', 'work', 'level', 'size', 'source', 'sink']

    def __init__(self, n):
        self.size = n
        self.graph = [[] for _ in range(self.size)]
        self.graph_len = [0] * self.size

    def add_edge(self, u, v, cap, rev_cap=0):
        fw, bw = Edge(v, cap), Edge(u, rev_cap)
        fw.rev, bw.rev = bw, fw
        self.graph[u].append(fw), self.graph[v].append(bw)
        self.graph_len[u] += 1; self.graph_len[v] += 1
    
    def bfs(self):
        self.level = [-1] * self.size
        self.level[self.source] = 0
        queue = [self.source]
        next_level = 0

        while queue:
            next_queue = []
            next_level += 1
        
            for u in queue:
                for edge in self.graph[u]:
                    v = edge.to

                    if self.level[v] < 0 and edge.cap > 0:
                        self.level[v] = next_level
                        next_queue.append(v)
            
            queue = next_queue

        return self.level[self.sink] != -1
    
    def dfs(self, u, cap):
        if u == self.sink: return cap
        curr_level = self.level[u]

        for i in range(self.work[u], self.graph_len[u]):
            edge = self.graph[u][i]
            v = edge.to

            if edge.cap > 0 and curr_level < self.level[v]:
                mini = self.dfs(v, edge.cap if edge.cap < cap else cap)

                if mini > 0:
                    edge.cap -= mini
                    edge.rev.cap += mini
                    return mini
            
            self.work[u] += 1

        return 0

    def max_flow(self, source, sink):
        total = 0
        self.source, self.sink = source, sink

        while self.bfs():
            self.work = [0] * self.size

            while flow := self.dfs(source, INF):
                total += flow
        
        return total


def next_index(i):
    if (j := i - M) > -1:   yield j
    if (j := i + M) < area: yield j
    if i % M:               yield i - 1
    if (j := i + 1) % M:    yield j


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    global N, M, area

    T = int(readline())
    for _ in range(T):
        N, M = map(int, readline().split())
        arr = []
        for _ in range(N):
            arr += list(map(int, readline().split()))

        area = N * M
        leng = area + 2
        mf = Dinic(leng)
        source, sink = leng - 2, leng - 1

        # 정점간 연결
        i = 0
        for j in range(N):
            for k in range(M):
                if (j + k) & 1: 
                    mf.add_edge(source, i, arr[i])
                    for p in next_index(i):
                        mf.add_edge(i, p, INF)

                else: 
                    mf.add_edge(i, sink, arr[i])

                i += 1

        total = sum(arr)
        flow = mf.max_flow(source, sink)

        write(str(total - flow) + '\n')


INF = float('inf')

main()
