class Edge():
    __slots__ = ['to', 'rev', 'cap']

    def __init__(self, to, cap):
        self.to = to
        self.cap = cap


class Dinic():
    __slots__ = ['size', 'graph', 'graph_iter', 'level', 'INF', 'start', 'end']

    def __init__(self, n):
        self.INF = float('inf')
        self.size = n
        self.graph = tuple([] for _ in range(self.size))

    def add_edge(self, fr, to, cap):
        forward = Edge(to, cap)
        backward = Edge(fr, 0)
        forward.rev = backward
        backward.rev = forward
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
    
    def bfs(self):
        queue = [self.start]
        self.level = [-1] * self.size
        self.level[self.start] = 0

        for u in queue:
            next_level = self.level[u] + 1

            for edge in self.graph[u]:
                v = edge.to

                if edge.cap > 0 and self.level[v] < 0:
                    self.level[v] = next_level
                    queue.append(v)
                    
                    if v == self.end: return True
        
        return False

    def dfs(self, u, upto):
        if u == self.end: return upto

        for edge in self.graph_iter[u]:
            v = edge.to

            if edge.cap > 0 and self.level[u] < self.level[v]:
                cost = self.dfs(v, upto if upto < edge.cap else edge.cap)

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
                ret = self.dfs(start, self.INF)
                if not ret: break

                flow += ret

        return flow
        

def main():
    arr = list(map(int, open(0).read().split()))
    N, P = arr[0], arr[1]
    mf = Dinic(N + 1)

    for i in range(2, 2*P + 2, 2):
        mf.add_edge(arr[i], arr[i + 1], 1)
    
    del arr
    
    print(mf.max_flow(1, 2))


main()
