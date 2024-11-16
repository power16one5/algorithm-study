import sys



def get_scc(edges):
    leng = len(edges)
    indices = [None] * leng
    parents = [None] * leng
    scc_indices = [None] * leng
    on_stack = bytearray(leng)
    stack = []
    sccs = []
    scc_count = 0
    idx_count = 0

    def dfs(i):
        nonlocal idx_count, scc_count

        indices[i] = idx_count
        parents[i] = idx_count
        on_stack[i] = 1
        stack.append(i)
        idx_count += 1

        for j in edges[i]:
            if parents[j] is None: dfs(j)
            if on_stack[j] and parents[i] > parents[j]: parents[i] = parents[j]
        
        if parents[i] == indices[i]:
            scc = []

            while True:
                j = stack.pop()
                scc_indices[j] = scc_count
                on_stack[j] = 0
                scc.append(j)

                if j == i: break
            
            scc_count += 1
            sccs.append(scc)

    for i in range(1, leng):
        if parents[i] is None: dfs(i)
    
    return sccs, scc_indices
    

def get_degree(edges, sccs, scc_indices):
    leng = len(sccs)
    depended = bytearray(leng)
    
    for scc in sccs:
        for i in scc:
            for j in edges[i]:
                if scc_indices[i] != scc_indices[j]:
                    depended[scc_indices[j]] = 1
    
    return depended.count(0)


sys.setrecursionlimit(int(1e7))
readline = sys.stdin.readline
T = int(readline())

for n, m in (map(int, readline().split()) for _ in range(T)):
    edges = [[] for _ in range(n + 1)]

    for a, b in (map(int, readline().split()) for _ in range(m)):
        edges[a].append(b)
    
    sccs, scc_indices = get_scc(edges)
    answer = get_degree(edges, sccs, scc_indices)

    sys.stdout.write(str(answer) + '\n')
