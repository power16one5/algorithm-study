import sys



def sol(edge, n):
    low, disc, parent = [[None] * n for _ in range(3)]
    ap = bytearray(n)
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
                if low[b] >= disc[a]: ap[a] = 1
            
            if b != parent[a] and low[a] > disc[b]: low[a] = disc[b]
    
    for a in range(1, n):
        # 루트노드 탐색
        if disc[a] is None:
            tarjan(a)

            children = 0
            for b in edge[a]:
                if parent[b] == a:
                    children += 1
            
                    if children > 1: 
                        ap[a] = 1
                        break

            else: ap[a] = 0

    return [i for i in range(1, n) if ap[i]]


def main():
    arr = list(map(int, open(0).read().split()))
    
    V, E = arr[0], arr[1]
    edge = [[] for _ in range(V + 1)]
    for i in range(2, 2*E + 1, 2):
        a, b = arr[i], arr[i + 1]
        edge[a].append(b); edge[b].append(a)
    
    points = sol(edge, V + 1)
    
    print(len(points))
    print(*points)


sys.setrecursionlimit(int(1e5) + 10)

main()
