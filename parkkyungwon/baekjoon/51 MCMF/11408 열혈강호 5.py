import sys
from heapq import heappop, heappush



class Edge():
    __slots__ = ['to', 'rev', 'cap', 'cost']

    def set_att(self, to, rev, cap, cost):
        self.to, self.rev, self.cap, self.cost = to, rev, cap, cost


class MCMF():
    __slots__ = ['edges', 'size', 'parent', 'parent_edge', 'source', 'sink']

    def __init__(self, n, source, sink):
        self.size = n
        self.source, self.sink = source, sink
        self.edges = [[] for _ in range(self.size)]

    def add_edge(self, u, v, cap, cost, rev_cap=0):
        fw, bw = Edge(), Edge()
        fw.set_att(v, bw, cap, cost); bw.set_att(u, fw, rev_cap, -cost)
        self.edges[u].append(fw), self.edges[v].append(bw)
    
    def dijkstra(self, potential):
        self.parent = [None] * self.size
        self.parent_edge = [None] * self.size
        dist = [INF] * self.size
        dist[self.source] = 0
        heap = [(0, self.source)]

        while heap:
            d, u = heappop(heap)
            if d > dist[u]: continue

            for e in self.edges[u]:
                v = e.to
                new_cost = d + e.cost + potential[u] - potential[v]

                if e.cap > 0 and dist[v] > new_cost:
                    dist[v] = new_cost
                    self.parent[v] = u
                    self.parent_edge[v] = e
                    heappush(heap, (new_cost, v))
        
        if dist[self.sink] is INF: return False

        for u in range(self.size):
            if dist[u] is not INF: potential[u] += dist[u]

        return True

    def max_flow(self):
        mini = INF

        u = self.sink
        while u != self.source:
            e = self.parent_edge[u]
            if mini > e.cap: mini = e.cap
            u = self.parent[u]
        
        u = self.sink
        while u != self.source:
            e = self.parent_edge[u]
            e.cap -= mini
            e.rev.cap += mini
            u = self.parent[u]

        return mini
        
    def min_cost_max_flow(self):
        total_flow = 0
        total_cost = 0
        potential = [0] * self.size

        while self.dijkstra(potential):
            flow = self.max_flow()
            total_flow += flow
            total_cost += flow * potential[self.sink]
        
        return total_flow, total_cost


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M = map(int, readline().split())

    leng = N + M + 2
    source, sink = leng - 2, leng - 1
    mcmf = MCMF(leng, source, sink)

    for i in range(N):
        mcmf.add_edge(source, i, 1, 0)
        arr = list(map(int, readline().split()))

        for j in range(1, len(arr), 2):
            mcmf.add_edge(i, arr[j] + N - 1, 1, arr[j + 1])
    
    for i in range(N, N + M):
        mcmf.add_edge(i, sink, 1, 0)
    
    write('\n'.join(map(str, mcmf.min_cost_max_flow())) + '\n')


INF = float('inf')

main()
