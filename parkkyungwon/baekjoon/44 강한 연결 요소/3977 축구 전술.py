import sys



def kosaraju(forward, backward):
    leng = len(forward)
    visited = bytearray(leng)
    stack = []

    def forward_dfs(i):
        visited[i] = 1

        for j in forward[i]:
            if not visited[j]:
                forward_dfs(j)

        stack.append(i)

    for i in range(leng):
        if visited[i]: continue
        
        forward_dfs(i)

    visited = [None] * leng
    sccs = []
    scc_count = 0

    def backward_dfs(i):
        visited[i] = scc_count

        for j in backward[i]:
            if visited[j] is None:
                backward_dfs(j)

        scc.append(i)

    for i in reversed(stack):
        if visited[i] is not None: continue

        scc = []
        backward_dfs(i)
        sccs.append(scc)
        scc_count += 1
    
    return sccs, visited


def scc_degree(sccs, scc_indices, forward):
    degree = bytearray(len(sccs))

    for i in range(len(scc_indices)):
        for j in forward[i]:
            if scc_indices[i] != scc_indices[j]:
                degree[scc_indices[j]] = 1
    
    return degree.index(0) if degree.count(0) == 1 else None


sys.setrecursionlimit(int(1e7))
readline = sys.stdin.readline
write = sys.stdout.write

T = int(readline())

for i in range(T):
    if i: readline()
        
    n, m = map(int, readline().split())

    forward = [[] for _ in range(n)]
    backward = [[] for _ in range(n)]
    for a, b in (map(int, readline().split()) for _ in range(m)):
        forward[a].append(b)
        backward[b].append(a)

    sccs, scc_indices = kosaraju(forward, backward)
    answer = scc_degree(sccs, scc_indices, forward)

    answer = 'Confused' if answer == None else '\n'.join(map(str, sorted(sccs[answer])))

    write(answer + '\n\n')
