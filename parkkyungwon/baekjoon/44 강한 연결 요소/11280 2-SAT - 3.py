import sys



def tarjan(edges):
    indices = [None] * L
    parents = [None] * L
    on_stack = bytearray(L)
    stack = []
    sccs = []
    index_count = 0

    def dfs(i):
        nonlocal index_count

        indices[i] = index_count
        parents[i] = index_count
        index_count += 1
        pos = len(stack)
        stack.append(i)
        on_stack[i] = 1

        for j in edges[i]:
            if parents[j] is None: dfs(j)
            if on_stack[j] and parents[i] > parents[j]: parents[i] = parents[j]

        if parents[i] == indices[i]:
            sccs.append(set(stack[pos:]))

            for k in (stack[j] for j in range(pos, len(stack))):
                on_stack[k] = 0

            del stack[pos:]
    
    for i in range(1, L):
        if parents[i] is None:
            dfs(i)
    
    return sccs


def sat(sccs):
    for scc in sccs:
        for i in scc:
            if -i in scc: return 0

    return 1


sys.setrecursionlimit(int(1e5))
readline = sys.stdin.readline
N, M = map(int, readline().split())
L = (2*N + 1)

edges = [set() for _ in range(L)]
for a, b in (map(int, readline().split()) for _ in range(M)):
    edges[-a].add(b); edges[-b].add(a)

sccs = tarjan(edges)
sys.stdout.write(str(sat(sccs)) + '\n')
