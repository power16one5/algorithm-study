import sys



def tarjan(edges):
    scc_indices = [None] * L
    parents = [None] * L
    stack = []
    sccs = []
    index_count = 0
    scc_count = 0

    def dfs(i):
        nonlocal index_count, scc_count

        index = index_count
        parents[i] = index_count
        index_count += 1
        pos = len(stack)
        stack.append(i)

        for j in edges[i]:
            if scc_indices[j] is not None: continue
            if parents[j] is None: dfs(j)
            if parents[i] > parents[j]: parents[i] = parents[j]

        if parents[i] == index:
            sccs.append(set(stack[pos:]))

            for k in (stack[j] for j in range(pos, len(stack))):
                scc_indices[k] = scc_count

            scc_count += 1
            del stack[pos:]
    
    for i in range(1, L):
        if i > N: i = N - i
        if parents[i] is None:
            dfs(i)
    
    return sccs, scc_indices


def sat(sccs, scc_indices):
    # x, ~x가 동시에 존재하는지 확인
    for scc in sccs:
        for i in scc:
            if -i in scc: return

    return [1 if scc_indices[i] < scc_indices[-i] else 0 for i in range(1, N+1)]


sys.setrecursionlimit(int(1e5))
write = sys.stdout.write
readline = sys.stdin.readline

N, M = map(int, readline().split())
L = (2*N + 1)

edges = [set() for _ in range(L)]
for a, b in (map(int, readline().split()) for _ in range(M)):
    edges[-a].add(b); edges[-b].add(a)

sccs, scc_indices = tarjan(edges)
answer = sat(sccs, scc_indices)

answer = '1\n' + str(' '.join(map(str, answer))) + '\n' if answer else '0\n'

write(answer)
