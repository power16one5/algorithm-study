import sys



class Edge():
    __slots__ = ['to', 'rev', 'cap']

    def __init__(self, to, cap):
        self.to, self.cap = to, cap


class Dinic():
    __slots__ = ['graph', 'graph_len', 'selected_edge', 'work', 'level', 'size', 'source', 'sink']

    def __init__(self, n):
        self.size = n
        self.graph = [[] for _ in range(self.size)]
        self.graph_len = [0] * self.size
        self.selected_edge = []

    def add_edge(self, u, v, cap, rev_cap=0, is_selected=False):
        fw, bw = Edge(v, cap), Edge(u, rev_cap)
        fw.rev, bw.rev = bw, fw
        self.graph[u].append(fw), self.graph[v].append(bw)
        self.graph_len[u] += 1; self.graph_len[v] += 1

        if is_selected: self.selected_edge.append(fw)
    
    def set_cap(self, cap):
        for edge in self.selected_edge:
            edge.cap = cap

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
    readline = sys.stdin.readline
    write = sys.stdout.write

    N = int(readline())
    adj = N ** 2
    row = list(map(int, readline().split()))
    col = list(map(int, readline().split()))

    leng = (N + 1) ** 2 + 1
    mf = Dinic(leng)
    source, sink = leng - 2, leng - 1

    # 간선 추가
    for row_index, v in enumerate(row, adj):
        mf.add_edge(source, row_index, v)

    for col_index, v in enumerate(col, adj + N):
        mf.add_edge(col_index, sink, v)

    for row_index, i in enumerate(range(0, adj, N), adj):
        for j in range(i, i + N):
            mf.add_edge(row_index, j, INF, is_selected=True)

    for col_index, i in enumerate(range(N), adj + N):
        for j in range(i, adj, N):
            mf.add_edge(j, col_index, INF, is_selected=True)

    # 탐색
    target = sum(row)
    s, e = 0, target
    while s < e:
        m = (s + e) >> 1
        mf.set_cap(m)
        mf.max_flow(source, sink)
        ret = mf.max_flow(sink, source)
        
        if target > ret: s = m + 1
        else: e = m

    else:
        mf.set_cap(s)
        mf.max_flow(source, sink)

    # 출력
    write(str(s) + '\n')

    cap = [0] * adj
    for edge in mf.selected_edge:
        if edge.to < adj: cap[edge.to] = edge.rev.cap
    
    for i in range(0, adj, N):
        write(' '.join(map(str, cap[i:i+N])) + '\n')


INF = float('inf')

main()
