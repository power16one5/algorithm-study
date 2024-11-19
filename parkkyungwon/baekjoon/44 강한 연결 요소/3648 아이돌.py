import sys


def tarjan(edges):
    parents = [None] * L
    on_stack = bytearray(L)
    stack = []
    index_count = 0

    def dfs(i):
        nonlocal index_count

        index = index_count
        parents[i] = index_count
        index_count += 1
        pos = len(stack)
        stack.append(i)
        on_stack[i] = 1

        for j in edges[i]:
            if parents[j] is None: dfs(j)
            if on_stack[j] and parents[i] > parents[j]: parents[i] = parents[j]

        if parents[i] == index:
            scc = set(stack[pos:])
            for i in scc:
                if -i in scc: return True

            for k in (stack[j] for j in range(pos, len(stack))):
                on_stack[k] = 0

            del stack[pos:]
    
    for i in range(1, L):
        if i > N: i = N - i
        if parents[i] is None:
            if dfs(i): return True
    
    return False


sys.setrecursionlimit(int(1e5))
write = sys.stdout.write
readline = sys.stdin.readline

while True:
    line = readline()
    if line == '': break

    N, M = map(int, line.split())
    L = (2*N + 1)

    edges = [set() for _ in range(L)]
    for a, b in (map(int, readline().split()) for _ in range(M)):
        edges[-a].add(b); edges[-b].add(a)
    
    edges[-1].add(1)

    write('no\n' if tarjan(edges) else 'yes\n')
