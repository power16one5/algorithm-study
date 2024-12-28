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

    def add_edge(self, u, v, cap, rev_cap):
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


def main():
    _, M = map(int, sys.stdin.readline().split())
    arr = sys.stdin.read()

    source = arr.index('K')
    sink = arr.index('H')

    tran = str.maketrans('KH', '..')
    arr = arr.translate(tran)
    leng = len(arr)
    width = M + 1

    if (diff := abs(source - sink)) == 1 or diff == width:
        print(-1)
        return

    mf = Dinic(2 * leng)

    for i in range(0, 2 * leng, 2): 
        mf.add_edge(i, i + 1, 1, 0)
    
    for i, char in enumerate(arr):
        if char != '.': continue
        u_in = 2*i
        u_out = u_in + 1

        for j in i + 1, i + width:
            if j < leng and arr[j] == '.': 
                v_in = 2*j
                v_out = v_in + 1
                mf.add_edge(u_out, v_in, 1, 0)
                mf.add_edge(v_out, u_in, 1, 0)

    print(mf.max_flow(2*source + 1, 2*sink))


sys.setrecursionlimit(int(1e5))
INF = float('inf')

main()
