class Dinic():
    __slots__ = ['fw_graph', 'bw_graph', 'graph_length', 'work', 'capacity', 'level', 'size', 'source', 'sink']

    def __init__(self, n):
        self.size = n
        self.graph_length = [0] * self.size
        self.fw_graph = [[] for _ in range(self.size)]
        self.bw_graph = [[] for _ in range(self.size)]
        self.capacity = [[0] * self.size for _ in range(self.size)]
    
    def add_edge(self, u, v, cap):
        self.fw_graph[u].append(v)
        self.bw_graph[v].append(u)
        self.capacity[u][v] += cap
        self.graph_length[u] += 1

    def bfs(self):
        self.level = [None] * self.size
        self.level[self.source] = 0
        self.level[self.sink] = self.size
        fw_queue = [self.source]
        bw_queue = [self.sink]

        while fw_queue and bw_queue:
            # 정방향
            next_fw_queue = []
            next_level = self.level[fw_queue[0]] + 1
            for u in fw_queue:
                for v in self.fw_graph[u]:
                    if self.capacity[u][v] > 0:
                        if self.level[v] is None:
                            self.level[v] = next_level
                            next_fw_queue.append(v)

                        elif self.level[v] > next_level: return True

            fw_queue = next_fw_queue
            
            # 역방향
            next_bw_queue = []
            next_level = self.level[bw_queue[0]] - 1
            for v in bw_queue:
                for u in self.bw_graph[v]:
                    if self.capacity[u][v] > 0:
                        if self.level[u] is None:
                            self.level[u] = next_level
                            next_bw_queue.append(u)

                        elif self.level[u] < next_level: return True

            bw_queue = next_bw_queue

        return False
    
    def dfs(self, u, upto):
        if u == self.sink: return upto
        cap = self.capacity[u]

        for i in range(self.work[u], self.graph_length[u]):
            v = self.fw_graph[u][i]

            if cap[v] > 0 and (self.level[v] is not None) and self.level[u] < self.level[v]:
                cost = self.dfs(v, upto if upto < cap[v] else cap[v])

                if cost > 0:
                    self.capacity[u][v] -= cost
                    self.capacity[v][u] += cost
                    return cost
        
            self.work[u] += 1

        return 0

    def max_flow(self, source, sink):
        total = 0
        self.source, self.sink = source, sink

        while self.bfs():
            self.work = [0] * self.size

            while cost := self.dfs(self.source, INF):
                total += cost
        
        return total
    
    def cut(self, source):
        queue = [source]
        visit = bytearray(self.size)
        visit[source] = 1

        for u in queue:
            for v in self.fw_graph[u]:
                if not visit[v] and self.capacity[u][v]: 
                    queue.append(v)
                    visit[v] = 1
        
        left, right = [], []
        for i in range(1, self.size - 1):
            if visit[i]: left.append(i)
            else: right.append(i)

        return left, right


def main():
    file = open(0)

    N = int(file.readline())
    team = map(int, file.readline().split())
    mat = [[None]] + [[None] + list(map(int, a.split())) for a in file.read().splitlines()]

    mf = Dinic(N + 2)
    source, sink = 0, N + 1

    left_v, mid_v, right_v = [], [], []
    for i, det in enumerate(team, 1):
        if det == 1: 
            mf.add_edge(0, i, INF)
            left_v.append(i)

        elif det == 2: 
            mf.add_edge(i, sink, INF)
            right_v.append(i)
        
        else:
            mid_v.append(i)
    
    for u in left_v:
        for v in right_v:
            if mat[u][v]: mf.add_edge(u, v, mat[u][v])

    for u in left_v:
        for v in mid_v:
            if mat[u][v]: mf.add_edge(u, v, mat[u][v])

    for u in mid_v:
        for v in right_v:
            if mat[u][v]: mf.add_edge(u, v, mat[u][v])
    
    for i in range(len(mid_v)):
        u = mid_v[i]
        for j in range(i + 1, len(mid_v)):
            v = mid_v[j]
            if mat[u][v]: 
                mf.add_edge(u, v, mat[u][v])
                mf.add_edge(v, u, mat[u][v])

    print(mf.max_flow(source, sink))

    left, right = mf.cut(source)
    print(*left)
    print(*right)


INF = float('inf')

main()
