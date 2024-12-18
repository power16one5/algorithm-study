import sys



def sol(edge, n):
    low, disc, parent = [[None] * n for _ in range(3)]
    bridge = []
    count = 0

    def tarjan(a):
        nonlocal count
        low[a] = disc[a] = count
        count += 1

        for b in edge[a]:
            if disc[b] is None: 
                parent[b] = a
                tarjan(b)
            
                if low[a] > low[b]: low[a] = low[b]
                if low[b] > disc[a]: bridge.append([a, b])
            
            if b != parent[a] and low[a] > disc[b]: low[a] = disc[b]
    
    tarjan(1)

    return bridge


def main():
    write = sys.stdout.write

    arr = list(map(int, open(0).read().split()))
    
    V, E = arr[0], arr[1]
    edge = tuple([] for _ in range(V + 1))
    for i in range(2, 2*E + 1, 2):
        a, b = arr[i], arr[i + 1]
        edge[a].append(b); edge[b].append(a)
    
    bridge = sol(edge, V + 1)
    
    write(str(len(bridge)) + '\n')
    
    for a in bridge:
        if a[0] > a[1]: a[0], a[1] = a[1], a[0]
    
    bridge.sort()

    for a in bridge:
        write(str(a[0]) + ' ' + str(a[1]) + '\n')


sys.setrecursionlimit(int(1e5) + 10)

main()
