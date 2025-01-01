import sys



class SegmentTree():
    __slots__ = ['tree', 'adj']

    def __init__(self, n):
        self.adj = 1 << n.bit_length()
        self.tree = [0] * (self.adj << 1)
    
    def query(self, s, e):
        total = 0
        s += self.adj; e += self.adj

        while s <= e:
            if s & 1:
                total += self.tree[s]
                s += 1
            
            if not(e & 1):
                total += self.tree[e]
                e -= 1

            s >>= 1; e >>= 1
        
        return total
    
    def update(self, i, w):
        i += self.adj

        while i:
            self.tree[i] += w
            i >>= 1


def euler_tour(n, edges):
    in_degree, out_degree = [None] * n, [None] * n
    degree = 1

    def dfs(u):
        nonlocal degree
        in_degree[u] = degree
        degree += 1

        for v in edges[u]:
            if in_degree[v] is None: dfs(v)
        
        out_degree[u] = degree
    
    dfs(1)

    return in_degree, out_degree


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M = map(int, readline().split())
    N += 1

    edges = [[] for _ in range(N)]
    edge_data = enumerate(map(int, readline().split()), 1)
    next(edge_data)
    for v, u in edge_data:
        edges[u].append(v)
    
    st = SegmentTree(N)
    in_degree, out_degree = euler_tour(N, edges)

    for _ in range(M):
        query = list(map(int, readline().split()))

        match query[0]:
            case 1:
                i, w = in_degree[query[1]], query[2]
                st.update(i, w)
            
            case _:
                s, e = in_degree[query[1]], out_degree[query[1]] - 1
                write(str(st.query(s, e)) + '\n')


sys.setrecursionlimit(int(1e6))

main()
