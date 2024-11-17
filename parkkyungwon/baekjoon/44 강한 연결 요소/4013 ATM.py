import sys



def tarjan(edges):
    indices = [None] * N
    parents = [None] * N
    on_stack = bytearray(N)
    stack = []
    sccs = []
    index_count = 0
    scc_count = 0

    def dfs(i):
        nonlocal index_count, scc_count

        indices[i] = index_count
        parents[i] = index_count
        index_count += 1
        stack.append(i)
        on_stack[i] = 1

        for j in edges[i]:
            if parents[j] is None: dfs(j)
            if on_stack[j] and parents[i] > parents[j]: parents[i] = parents[j]

        if parents[i] == indices[i]:
            scc = []

            while True:
                j = stack.pop()
                indices[j] = scc_count
                on_stack[j] = 0
                scc.append(j)

                if i == j: break
            
            sccs.append(scc)
            scc_count += 1
    
    for i in range(N):
        if parents[i] is None:
            dfs(i)

    return sccs, indices


def sol(sccs, scc_indices, money, edges, start, dests):
    scc_leng = len(sccs)

    # scc들 간의 간선, scc에 있는 총 현금
    scc_edges = [[] for _ in range(scc_leng)]
    scc_values = [0] * scc_leng

    for i in range(N):
        scc_values[scc_indices[i]] += money[i]

        for j in edges[i]:
            if scc_indices[i] == scc_indices[j]: continue
            
            scc_edges[scc_indices[i]].append(scc_indices[j])
    
    # 진입 차수
    scc_degree = [0] * scc_leng
    queue = [scc_indices[start]]
    visited = bytearray(scc_leng)
    visited[scc_indices[start]] = 1

    for i in queue:
        for j in scc_edges[i]:
            scc_degree[j] += 1

            if visited[j]: continue

            visited[j] = 1
            queue.append(j)
    
    # 진입 차수를 감소시키면서 현금 계산
    queue = [scc_indices[start]]
    scc_cum_values = [0] * scc_leng

    for i in queue:
        v = scc_cum_values[i] + scc_values[i]

        for j in scc_edges[i]:
            if scc_cum_values[j] < v:
                scc_cum_values[j] = v
            
            scc_degree[j] -= 1
            if not scc_degree[j]: queue.append(j)
        
    dests = {scc_indices[i] for i in dests}

    return max(scc_cum_values[i] + scc_values[i] for i in dests if visited[i])


sys.setrecursionlimit(int(1e6))
readline = sys.stdin.readline
int_m1 = lambda x: int(x) - 1
N, M = map(int, readline().split())

edges = [[] for _ in range(N)]
for a, b in (map(int_m1, readline().split()) for _ in range(M)):
    edges[a].append(b)

money = [int(readline()) for _ in range(N)]

sccs, scc_indices = tarjan(edges)

S = int_m1(readline().split()[0])
dests = tuple(map(int_m1, readline().split()))

sys.stdout.write(str(sol(sccs, scc_indices, money, edges, S, dests)) + '\n')
