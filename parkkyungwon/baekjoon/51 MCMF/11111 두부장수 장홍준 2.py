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
    
    def add_edge(self, u, v, cap, cost):
        fw, bw = Edge(), Edge()
        fw.set(v, bw, cap, cost), bw.set(u, fw, 0, -cost)
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
        
        if adj[self.sink] >= 0: return False, None, None
        
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
    file = open(0)
    cost_mat = [[10, 8, 7, 5, 1],
                [8, 6, 4, 3, 1],
                [7, 4, 3, 2, 1],
                [5, 3, 2, 2, 1],
                [1, 1, 1, 1, 0]]
    
    N, M = map(int, file.readline().split())
    trans = str.maketrans('ABCDF', '01234')
    arr = [list(map(int, line.translate(trans))) for line in file.read().splitlines()]

    leng = N * M
    source, sink = leng, leng + 1
    mcmf = MCMF(leng + 2, source, sink)

    i = 0
    for y in range(N):
        for x in range(M):
            if (y + x) & 1:
                mcmf.add_edge(source, i, 1, 0)
                
                if y:
                    cost = cost_mat[arr[y - 1][x]][arr[y][x]]
                    mcmf.add_edge(i, i - M, 1, -cost)
                
                if (y + 1) % N: 
                    cost = cost_mat[arr[y + 1][x]][arr[y][x]]
                    mcmf.add_edge(i, i + M, 1, -cost)
            
                if x:
                    cost = cost_mat[arr[y][x - 1]][arr[y][x]]
                    mcmf.add_edge(i, i - 1, 1, -cost)

                if (x + 1) % M: 
                    cost = cost_mat[arr[y][x + 1]][arr[y][x]]
                    mcmf.add_edge(i, i + 1, 1, -cost)

            else:
                mcmf.add_edge(i, sink, 1, 0)
            
            i += 1
    
    print(-mcmf.min_cost_max_flow())



INF = float('inf')

main()
