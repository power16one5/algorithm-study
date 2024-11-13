import sys



def sol(parent, n, a, b):
    visited = bytearray(n + 1)

    while a:
        if visited[a]: return a

        visited[a] = 1
        a = parent[a]
        a, b = b, a

    while not visited[b]:
        b = parent[b]
    
    return b



readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    n = int(readline())

    parent = [0] * (n + 1)
    for a, b in (map(int, readline().split()) for _ in range(n - 1)):
        parent[b] = a
    
    a, b = map(int, readline().split())
    sys.stdout.write(str(sol(parent, n, a, b)) + '\n')
