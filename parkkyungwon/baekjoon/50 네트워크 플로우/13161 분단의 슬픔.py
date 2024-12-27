class Dinic():
    __slots__ = ['graph', 'work', 'capacity', 'level', 'size', 'source', 'sink']

    def __init__(self, n):
        self.size = n
        self.graph = [[] for _ in range(self.size)]
        self.capacity = [[0] * self.size for _ in range(self.size)]
    
    def add_edge(self, u, v, cap):
        self.graph[u].append(v)
        self.capacity[u][v] += cap

    def bfs(self):
        self.level = [-1] * self.size
        self.level[self.source] = 0
        queue = [self.source]

        for u in queue:
            next_level = self.level[u] + 1
            cap = self.capacity[u]

            for v in self.graph[u]:
                if cap[v] > 0 and self.level[v] < 0:
                    self.level[v] = next_level
                    queue.append(v)

        return self.level[self.sink] > -1
    
    def dfs(self, u, upto):
        if u == self.sink: return upto
        cap = self.capacity[u]
        next_level = self.level[u] + 1    

        for i in range(self.work[u], len(self.graph[u])):
            v = self.graph[u][i]

            if cap[v] > 0 and next_level == self.level[v]:
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
            for v in self.graph[u]:
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
