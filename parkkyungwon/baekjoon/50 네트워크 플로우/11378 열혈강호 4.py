import sys



class Edge():
    __slots__ = ['to', 'rev', 'cap']

    def __init__(self, to, cap):
        self.to = to
        self.cap = cap


class Dinic():
    __slots__ = ['graph', 'graph_iter', 'size', 'level', 'start', 'end', 'INF']

    def __init__(self, n):
        self.INF = float('inf')
        self.size = n
        self.graph = tuple([] for _ in range(n))
    
    def add_edge(self, u, v, cap):
        fw, bw = Edge(v, cap), Edge(u, 0)
        fw.rev, bw.rev = bw, fw
        self.graph[u].append(fw); self.graph[v].append(bw)
    
    def bfs(self):
        self.level = [-1] * self.size
        self.level[self.start] = 0
        queue = [self.start]

        for u in queue:
            next_level = self.level[u] + 1

            for edge in self.graph[u]:
                v = edge.to

                if edge.cap > 0 and self.level[v] < 0:
                    self.level[v] = next_level
                    queue.append(v)

                    if v == self.end: return True
        
        return False
    
    def dfs(self, u, cap):
        if u == self.end: return cap

        for edge in self.graph_iter[u]:
            v = edge.to

            if edge.cap > 0 and self.level[u] < self.level[v]:
                cost = self.dfs(v, cap if cap < edge.cap else edge.cap)

                if cost > 0:
                    edge.cap -= cost
                    edge.rev.cap += cost
                    return cost
        
        return 0
    
    def max_flow(self, start, end):
        flow = 0 
        self.start, self.end = start, end

        while self.bfs():
            self.graph_iter = [iter(self.graph[i]) for i in range(self.size)]

            while True:
                ret = self.dfs(self.start, self.INF)
                if not ret: break

                flow += ret
        
        return flow


def main():
    readline = sys.stdin.readline

    N, M, K = map(int, readline().split())
    u_size = N + 1
    total_size = N + M + 3
    start = 0
    end = total_size - 1
    extra = total_size - 2

    mf = Dinic(total_size)

    # 시작점과 직원 연결
    for i in range(1, u_size):
        mf.add_edge(0, i, 1)

    # 끝점과 일 연결
    for i in range(u_size, u_size + M):
        mf.add_edge(i, end, 1)

    # 직원과 일 연결
    for u in range(1, u_size):
        for v in map(int, readline().split()[1:]):
            mf.add_edge(u, v + N, 1)
    
    # 벌점 할당
    mf.add_edge(0, extra, K)
    for i in range(1, u_size):
        mf.add_edge(extra, i, K)

    print(mf.max_flow(start, end))


main()
