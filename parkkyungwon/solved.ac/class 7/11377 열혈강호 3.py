import sys
import copy



def hopcroft_karp(edges, n, m, k):
    n2 = n << 1
    pair_u = [None] * n2
    pair_v = [None] * m
    level = [0] * n2
    edge_length = [len(edge) for edge in edges]
    remained_u = {i for i in range(n)}
    matching = 0

    def bfs(leng):
        queue = []

        for u in range(leng):
            if pair_u[u] is None: queue.append(u)
            else: level[u] = None

        flag = False

        for u in queue:
            next_level = level[u] + 1
            
            for v in edges[u]:
                u2 = pair_v[v]

                if u2 is None:
                    flag = True

                elif level[u2] is None:
                    level[u2] = next_level
                    queue.append(u2)
        
        return flag
        
    def dfs(u):
        next_level = level[u] + 1

        while work[u] < edge_length[u]:
            v = edges[u][work[u]]
            u2 = pair_v[v]

            if u2 is None or (level[u2] == next_level and dfs(u2)):
                pair_u[u] = v; pair_v[v] = u
                return True
            
            work[u] += 1
        
        level[u] = 0
        return False

    # 평범하게 사람과 일 1:1 매칭
    while bfs(n):
        work = [0] * n
        for u in list(remained_u):
            if pair_u[u] is None and dfs(u): 
                matching += 1
                remained_u.remove(u)

    # 사람 복사하고 매칭
    amax = matching + k
    edges += copy.deepcopy(edges)
    edge_length += edge_length
    remained_u.update(range(n, n2))

    while bfs(n2):
        work = [0] * n2
        for u in list(remained_u):
            if pair_u[u] is None and dfs(u): 
                matching += 1
                remained_u.remove(u)

    return matching if amax > matching else amax

        
def main():
    readline = sys.stdin.readline
    
    N, M, K = map(int, readline().split())
    edges = [list(map(int, readline().split()[1:])) for _ in range(N)]
    
    matching = hopcroft_karp(edges, N, M + 1, K)

    print(matching)


main()
