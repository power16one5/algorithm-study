import sys
from heapq import heappush, heappop



class Edge():
    __slots__ = ['to', 'rev', 'cap', 'cost']

    def set(self, to, rev, cap, cost):
        self.to, self.rev, self.cap, self. cost = to, rev, cap, cost


class MCMF():
    __slots__ = ['edge', 'size', 'source', 'sink']

    def __init__(self, size, source, sink):
        self.size, self.source, self.sink = size, source, sink
        self.edge = [[] for _ in range(self.size)]
    
    def add_edge(self, u, v, cap, cost, rev_cap=0, rev_cost=0):
        fw, bw = Edge(), Edge()
        fw.set(v, bw, cap, cost), bw.set(u, fw, rev_cap, rev_cost)
        self.edge[u].append(fw), self.edge[v].append(bw)
    
    def dijkstra(self, adj):
        parent = [None] * self.size
        parent_edge = [None] * self.size
        dist = [INF] * self.size
        dist[self.source] = 0
        heap = [(0, self.source)]

        while heap:
            cum_cost, u = heappop(heap)
            if cum_cost > dist[u]: continue

            for edge in self.edge[u]:
                v = edge.to
                new_cost = dist[u] + edge.cost + adj[u] - adj[v]

                if edge.cap > 0 and dist[v] > new_cost:
                    dist[v] = new_cost
                    parent[v] = u
                    parent_edge[v] = edge
                    heappush(heap, (new_cost, v))
        
        if dist[self.sink] is INF: return False, None, None

        for i in range(self.size):
            if dist[i] is not INF: adj[i] += dist[i]
        
        return True, parent, parent_edge

    def max_flow(self, parent, parent_edge):
        flow = INF

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
    readline = sys.stdin.readline
    write = sys.stdout.write

    T = int(readline())
    for _ in range(T):
        N, M = map(int, readline().split())

        source, sink = 0, N + 1
        mcmf = MCMF(N + 2, source, sink)

        for _ in range(M):
            u, v = map(int, readline().split())
            mcmf.add_edge(u, v, INF, 1, 0, -1)
            mcmf.add_edge(v, u, INF, 1, 0, -1)
        
        bit1, bit2 = [int(readline().rstrip().replace(' ', ''), base=2) for _ in range(2)]
        # 같은 색을 가지는 동전 개수가 적은 동전을 1로 선택
        if (N >> 1) + 1 < bit1.bit_count():
            mask = (1 << N) - 1
            bit1, bit2 = ~bit1 & mask, ~bit2 & mask
        
        while bit1:
            target_bit = bit1 & -bit1
            mcmf.add_edge(source, N - target_bit.bit_length() + 1, 1, 0)
            bit1 -= target_bit

        while bit2:
            target_bit = bit2 & -bit2
            mcmf.add_edge(N - target_bit.bit_length() + 1, sink, 1, 0)
            bit2 -= target_bit
        
        write(str(mcmf.min_cost_max_flow()) + '\n')



INF = float('inf')

main()
