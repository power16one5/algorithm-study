class Edge():
    __slots__ = ['to', 'rev', 'cap']

    def __init__(self, to, cap):
        self.to, self.cap = to, cap


class Dinic():
    __slots__ = ['graph', 'graph_iter', 'level', 'size', 'source', 'sink']

    def __init__(self, n):
        self.size = n
        self.graph = tuple([] for _ in range(self.size))
    
    def add_edge(self, u, v):
        fw, bw = Edge(v, 1), Edge(u, 0)
        fw.rev, bw.rev = bw, fw
        self.graph[u].append(fw); self.graph[v].append(bw)

    def bfs(self):
        self.level = [-1] * self.size
        self.level[self.source] = 0
        queue = [self.source]

        for u in queue:
            next_level = self.level[u] + 1

            for edge in self.graph[u]:
                v = edge.to

                if edge.cap > 0 and self.level[v] < 0:
                    self.level[v] = next_level
                    queue.append(v)

                    if v == self.sink: return True
        
        return False
    
    def dfs(self, u, cap):
        if u == self.sink: return cap

        for edge in self.graph_iter[u]:
            v = edge.to

            if edge.cap > 0 and self.level[u] < self.level[v]:
                cost = self.dfs(v, cap if cap < edge.cap else edge.cap)

                if cost > 0:
                    edge.cap -= cost
                    edge.rev.cap += cost
                    return cost
        
        return 0
    
    def max_flow(self, source, sink):
        total = 0
        self.source, self.sink = source, sink

        while self.bfs():
            self.graph_iter = tuple(iter(self.graph[i]) for i in range(self.size))

            while True:
                cost = self.dfs(self.source, self.sink)
                if not cost: break

                total += cost
        
        return total


def main():
    arr = list(map(int, open(0).read().split()))
    N, P = arr[0], arr[1]
    mf = Dinic(2*(N + 1))
    source, sink = 2*1 + 1, 2*2

    for i in range(2, 2*N + 2, 2):
        mf.add_edge(i, i + 1)
    
    for i in range(2, 2*P + 2, 2):
        mf.add_edge(2*arr[i] + 1, 2*arr[i + 1])
        mf.add_edge(2*arr[i + 1] + 1, 2*arr[i])
    
    del arr

    print(mf.max_flow(source, sink))


main()
