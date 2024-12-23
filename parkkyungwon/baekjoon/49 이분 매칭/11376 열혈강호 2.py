import sys



def bimat(n, m, edge):
    n += 1; m += 1
    pair_u = [0] * n
    pair_v = [0] * m
    level = [0] * n

    def bfs():
        queue = []

        level[0] = None
        for u in range(1, n):
            if not pair_u[u]: queue.append(u)
            else: level[u] = None
        
        for u in queue:
            for v in edge[u]:
                u2 = pair_v[v]

                if level[u2] is None:
                    level[u2] = level[u] + 1
                    queue.append(u2)
        
        return level[0] is not None
    
    def dfs(u):
        next_level = level[u] + 1

        for v in edge[u]:
            u2 = pair_v[v]

            if level[u2] == next_level and (not u2 or dfs(u2)):
                pair_u[u] = v; pair_v[v] = u
                return True
            
        return False
    
    matched = 0

    while bfs():
        for u in range(1, n):
            if not pair_u[u] and dfs(u): matched += 1
    
    return matched


def main():
    readline = sys.stdin.readline

    N, M = map(int, readline().split())
    edge = tuple([] for _ in range(2*N + 1))

    for a in range(1, N + 1):
        for b in map(int, readline().split()[1:]):
            edge[a].append(b)
            edge[a + N].append(b)
    
    print(bimat(2*N, M, edge))


sys.setrecursionlimit(int(1e4))

main()
