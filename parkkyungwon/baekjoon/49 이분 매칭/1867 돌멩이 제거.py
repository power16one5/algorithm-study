import sys



def hopcroft_karp(n, m, edge):
    pair_u = [None] * n
    pair_v = [None] * m
    level = [0] * n
    remained_u = {i for i in range(n)}
    matched = 0

    def bfs():
        queue = []
        flag = False

        for u in range(n):
            if pair_u[u] is None: queue.append(u)
            else: level[u] = None

        for u in queue:
            next_level = level[u] + 1

            for v in edge[u]:
                u2 = pair_v[v]
                if u2 is None:
                    flag = True
                
                elif level[u2] is None:
                    level[u2] = next_level
                    queue.append(u2)
        
        return flag
    
    def dfs(u):
        next_level = level[u] + 1

        for v in edge[u]:
            u2 = pair_v[v]

            if u2 is None or (level[u2] == next_level and dfs(u2)):
                pair_u[u] = v; pair_v[v] = u
                return True
        
        level[u] = 0
        return False

    while bfs():
        selected_u = set()

        for u in remained_u:
            if pair_u[u] is None and dfs(u): matched += 1
            
            if pair_u[u] is not None: selected_u.add(u)
        
        remained_u -= selected_u

    return matched


def main():
    readline = sys.stdin.readline

    N, K = map(int, readline().split())
    edge = tuple([] for _ in range(N))

    for _ in range(K):
        a, b = map(int, readline().split())
        edge[a - 1].append(b - 1)
    
    print(hopcroft_karp(N, N, edge))


main()
