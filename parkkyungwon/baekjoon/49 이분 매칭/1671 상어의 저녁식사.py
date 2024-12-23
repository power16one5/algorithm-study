def hopcroft_karp(n, m, edge):
    pair_u = [None] * n
    pair_v = [None] * m
    level = [0] * n

    def bfs():
        queue = []
        flag = False

        for u in range(n):
            if pair_u[u] is None: queue.append(u)
            else: level[u] = None
        
        for u in queue:
            for v in edge[u]:
                u2 = pair_v[v]

                if u2 is None: 
                    flag = True

                elif level[u2] is None:
                    level[u2] = level[u] + 1
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
    
    matched = 0
    remained_u = {i for i in range(n)}

    while bfs():
        selected_u = set()

        for u in remained_u:
            if pair_u[u] is None and dfs(u): matched += 1

            if pair_u[u]: selected_u.add(u)
        
        remained_u -= selected_u
    
    return pair_v.count(None)


def compare(a, b):
    return a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2]


def main():
    arr = iter(open(0).read().splitlines())
    N = int(next(arr))
    edge = tuple([] for _ in range(2 * N))
    arr = tuple(tuple(map(int, a.split())) for a in arr)

    for i in range(N):
        for j in range(i + 1, N):
            if compare(arr[i], arr[j]):
                i2 = i << 1
                edge[i2].append(j)
                edge[i2 + 1].append(j)
            
            elif compare(arr[j], arr[i]):
                j2 = j << 1
                edge[j2].append(i)
                edge[j2 + 1].append(i)

    del arr

    print(hopcroft_karp(N << 1, N, edge))


main()
