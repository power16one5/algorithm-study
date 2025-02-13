from heapq import heappush, heappop
import sys



class Edge():
    __slots__ = ('to', 'rev', 'cap', 'cost')

    def set(self, to, rev, cap, cost):
        self.to, self.rev, self.cap, self. cost = to, rev, cap, cost


class MCMF():
    __slots__ = ('edges', 'size', 'source', 'sink', 'INF')

    def __init__(self, size, source, sink):
        self.size, self.source, self.sink = size, source, sink
        self.edges = tuple([] for _ in range(self.size))
        self.INF = float('inf')

    def add_edge(self, u, v, cap, cost):
        fw, bw = Edge(), Edge()
        fw.set(v, bw, cap, cost), bw.set(u, fw, 0, -cost)
        self.edges[u].append(fw), self.edges[v].append(bw)
    
    def dijkstra(self, adj):
        parent = [None] * self.size
        parent_edge = [None] * self.size
        dist = [self.INF] * self.size
        dist[self.source] = 0
        heap = [(0, self.source)]

        while heap:
            cum_cost, u = heappop(heap)
            if cum_cost > dist[u]: continue

            for edge in self.edges[u]:
                v = edge.to
                new_cost = dist[u] + edge.cost + adj[u] - adj[v]

                if edge.cap > 0 and dist[v] > new_cost:
                    dist[v] = new_cost
                    parent[v] = u
                    parent_edge[v] = edge
                    heappush(heap, (new_cost, v))
        
        if dist[self.sink] is self.INF: return False, None, None

        for i in range(self.size):
            if dist[i] is not self.INF: adj[i] += dist[i]
        
        return True, parent, parent_edge

    def max_flow(self, parent, parent_edge):
        flow = self.INF

        u = self.sink
        while u != self.source:
            flow2 = parent_edge[u].cap
            if flow > flow2: flow = flow2
            u = parent[u]
        
        u = self.sink
        while u != self.source:
            edge = parent_edge[u]
            edge.cap -= flow
            edge.rev.cap += flow
            u = parent[u]

        return flow
            
    def min_cost_max_flow(self):
        cost = 0
        adj = [0] * self.size

        while True:
            boo, parent, parent_edge = self.dijkstra(adj)
            if not boo: break

            flow = self.max_flow(parent, parent_edge)
            cost += flow * adj[self.sink]
        
        return cost


def main():
    readline = lambda: map(int, sys.stdin.readline().split())

    N, M = readline()
    size = N + M + 2 
    source, sink = size - 2, size -1
    mcmf = MCMF(size, source, sink)

    for person, cap in enumerate(readline()): mcmf.add_edge(person, sink, cap, 0)
    for store, cap in enumerate(readline(), N): mcmf.add_edge(source, store, cap, 0)

    INF = float('inf')
    for store in range(N, N + M):
        for person, cost in enumerate(readline()):
            mcmf.add_edge(store, person, INF, cost)
    
    print(mcmf.min_cost_max_flow())


main()
