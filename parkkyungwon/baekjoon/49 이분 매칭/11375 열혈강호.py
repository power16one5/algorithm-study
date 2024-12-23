import sys



def bimat(n, m, edge):
    pair_u = [0] * (n + 1)
    pair_v = [0] * (m + 1)
    level = [0] * (n + 1)

    def bfs():
        queue = []

        # 매칭 되있으면 None, 아니면 0
        level[0] = None
        for u in range(1, n + 1):
            if not pair_u[u]:
                level[u] = 0
                queue.append(u)

            else:
                level[u] = None

        # 매칭되지않은 정점을 통해서 매칭된 정점에 도달하면 레벨 +
        for u in queue:
            for v in edge[u]:
                u2 = pair_v[v]

                if level[u2] is None:
                    level[u2] = level[u] + 1
                    queue.append(u2)

        # augmenting path 존재
        return level[0] is not None

    def dfs(u):
        for v in edge[u]:
            u2 = pair_v[v]

            # 매칭 성공
            if level[u2] == level[u] + 1 and (not u2 or dfs(u2)):
                pair_u[u] = v
                pair_v[v] = u
                return True

        # 매칭 실패
        level[u] = None
        return False
        
    matched = 0
    while bfs():
        for u in range(1, n + 1):
            if not pair_u[u] and dfs(u): matched += 1

    return matched


def main():
    readline = sys.stdin.readline

    N, M = map(int, readline().split())
    edge = tuple([] for _ in range(N + M + 1))

    for a in range(1, N + 1):
        for b in map(int, readline().split()[1:]):
            edge[a].append(b)
    
    print(bimat(N, M, edge))


sys.setrecursionlimit(int(1e4))

main()
