import sys
from itertools import combinations as comb



def tarjan(edges):
    scc_indices = [None] * L
    parents = [None] * L
    stack = []
    index_count = 0
    scc_count = 0

    def dfs(i):
        nonlocal index_count, scc_count

        current = index_count
        parents[i] = index_count
        index_count += 1
        pos = len(stack)
        stack.append(i)

        for j in edges[i]:
            if scc_indices[j] is not None: continue
            if parents[j] is None: dfs(j)
            if parents[i] > parents[j]: parents[i] = parents[j]

        if parents[i] == current:
            for j in stack[pos:]: scc_indices[j] = scc_count

            scc_count += 1
            del stack[pos:]
    
    for i in range(1, L):
        if i > N: i = N - i
        if parents[i] is None:
            dfs(i)
    
    return scc_indices


def sat(scc_indices):
    answer = []

    for i in range(1, N+1):
        if scc_indices[i] == scc_indices[-i]: return
        
        answer.append('R' if scc_indices[i] < scc_indices[-i] else 'B')
            
    return answer


sys.setrecursionlimit(int(1e5))
write = sys.stdout.write
readline = sys.stdin.readline

N, M = map(int, readline().split())
L = (2*N + 1)

edges = [set() for _ in range(L)]
for _ in range(M):
    arr = readline().split()
    arr = [int(arr[i]) if arr[i+1] == 'R' else -int(arr[i]) for i in range(0, 5, 2)]
    
    for a, b in comb(arr, 2):
        edges[-a].add(b); edges[-b].add(a)

scc_indices = tarjan(edges)
answer = sat(scc_indices)

answer = ''.join(answer) + '\n' if answer else '-1\n'

write(answer)
