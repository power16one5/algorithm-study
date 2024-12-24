import sys



def hopcroft_karp(n, edge):
    pair_u = [None] * n
    pair_v = [None] * n
    level = [0] * n
    remained_u = {i for i in range(n) if edge[i]}
    matching = 0

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
            if pair_u[u] is None and dfs(u):
                matching += 1

            if pair_u[u] is not None:
                selected_u.add(u)
        
        remained_u -= selected_u
    
    return matching


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    C = int(readline())
    for _ in range(C):
        N, M = map(int, readline().split())
        N += 2; M += 2
        leng = N * M

        arr = 'x' * M
        for _ in range(N - 2):
            arr += 'x' + readline().rstrip() + 'x'
        arr += 'x' * M
    
        arr_bool = bytearray(leng)
        for i in range(leng):
            if arr[i] == '.': arr_bool[i] = 1

        del arr
        num_vertex = arr_bool.count(1)

        edge = tuple([] for _ in range(leng))
        for s in range(1 + M, leng, M):
            for j in range(s, s + M - 1, 2):
                if arr_bool[j]:
                    edge[j].extend((k for k in (j-1, j+1, j-M+1, j-M-1, j+M+1, j+M-1) if arr_bool[k]))
        
        write(str(num_vertex - hopcroft_karp(leng, edge)) + '\n')


main()
