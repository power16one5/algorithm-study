class Dinic():
    __slots__ = ['fw_edge', 'bw_edge', 'edge_length', 'work', 'capacity', 'level', 'size', 'source', 'sink']

    def __init__(self, n):
        self.size = n
        self.edge_length = [0] * self.size
        self.fw_edge = [[] for _ in range(self.size)]
        self.bw_edge = [[] for _ in range(self.size)]
        self.capacity = [[0] * self.size for _ in range(self.size)]
    
    def add_edge(self, u, v, cap):
        self.fw_edge[u].append(v)
        self.bw_edge[v].append(u)
        self.capacity[u][v] += cap
        self.edge_length[u] += 1

    def bfs(self):
        fw_queue, bw_queue = [self.source], [self.sink]
        fw_queue2, bw_queue2 = [], []
        parent = [i for i in range(self.size)]
        in_queue = bytearray(self.size)
        q0, q1, q2, q3, q4 = [i * self.size for i in range(5)]

        self.level = [None] * self.size
        self.level[self.source] = q0
        self.level[self.sink] = q4 - 1

        # 투 포인터, bfs
        while fw_queue and bw_queue:
            # 정방향
            next_queue = []
            next_level = self.level[fw_queue[0]] + 1
            for u in fw_queue:
                for v in self.fw_edge[u]:
                    if self.capacity[u][v] > 0:
                        if self.level[v] is None:
                            self.level[v] = next_level
                            parent[v] = u
                            next_queue.append(v)

                        elif self.level[v] >= q3 and not in_queue[u]:
                            bw_queue2.append(u)
                            in_queue[u] = 1

            fw_queue = next_queue
            
            # 역방향
            next_queue = []
            next_level = self.level[bw_queue[0]] - 1
            for v in bw_queue:
                for u in self.bw_edge[v]:
                    if self.capacity[u][v] > 0:
                        if self.level[u] is None:
                            self.level[u] = next_level
                            parent[u] = v
                            next_queue.append(u)

                        elif self.level[u] < q1 and not in_queue[v]:
                            fw_queue2.append(v)
                            in_queue[v] = 1

            bw_queue = next_queue
        
        if not fw_queue2: return False

        # level 초기화
        q2_1 = q2 - 1
        for u in bw_queue2: self.level[u] = q2_1
        for u in fw_queue2: self.level[u] = q2

        # level 재할당
        # 정방향
        while bw_queue2:
            next_queue = []
            next_level = self.level[bw_queue2[0]] - 1
            for v in bw_queue2:
                u = parent[v]

                if self.level[u] < q1:
                    self.level[u] = next_level
                    next_queue.append(u)
            
            bw_queue2 = next_queue

        # 역방향
        while fw_queue2:
            next_queue = []
            next_level = self.level[fw_queue2[0]] + 1
            for u in fw_queue2:
                v = parent[u]

                if self.level[v] >= q3:
                    self.level[v] = next_level
                    next_queue.append(v)
            
            fw_queue2 = next_queue

        return True
    
    def dfs(self, u, upto):
        if u == self.sink: return upto
        cap = self.capacity[u]

        for i in range(self.work[u], self.edge_length[u]):
            v = self.fw_edge[u][i]

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
            for v in self.fw_edge[u]:
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
