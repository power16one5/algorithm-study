import sys



def find_scc():
    indices = [None] * L
    parents = [None] * L
    on_stack = bytearray(L)
    stack = []
    scc = []
    count = 0

    def dfs(i):
        nonlocal count

        indices[i] = count
        parents[i] = count
        count += 1
        stack.append(i)
        on_stack[i] = 1

        for j in edges[i]:
            if parents[j] is None: dfs(j)
            if on_stack[j] and parents[i] > parents[j]: parents[i] = parents[j]

        if indices[i] == parents[i]:
            scci = []

            while True:
                j = stack.pop()
                on_stack[j] = 0
                scci.append(j)
            
                if i == j: break

            scci.sort()
            scc.append(scci)
    
    for i in range(1, L):
        if not indices[i]:
            dfs(i)

    scc.sort(key=lambda x: x[0])

    return scc


sys.setrecursionlimit(int(1e7))
readline = sys.stdin.readline
write = sys.stdout.write

V, E = map(int, readline().split())
L = V + 1

edges = [[] for _ in range(L)]
for a, b in (map(int, readline().split()) for _ in range(E)):
    edges[a].append(b)

scc = find_scc()

write(str(len(scc)) + '\n')
for a in scc:
    write(' '.join(map(str, a)) + ' -1\n')
