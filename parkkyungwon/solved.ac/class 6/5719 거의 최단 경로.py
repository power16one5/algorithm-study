import sys
from heapq import heappop, heappush



def dijkstra(n, edge, start, end):
    heap = [[0, start]]
    dp = [None] * n
    
    while heap:
        w, s = heappop(heap)

        if dp[s] is not None: continue
        dp[s] = w

        if s == end: break

        for d in edge[s]:
            if dp[d] is not None: continue
            
            heappush(heap, [w + edge[s][d], d])

    return dp


def remove(n, edge, edge_rev, dp, end):
    queue = [end]
    visit = bytearray(n)
    visit[end] = 1

    for q in queue:
        for e in edge_rev[q]:
            if dp[e] is not None and (dp[q] - edge_rev[q][e]) == dp[e]:
                del edge[e][q]
                
                if visit[e]: continue
                visit[e] = 1
                queue.append(e)


def sol(n, edge, edge_rev, start, end):
    dp = dijkstra(n, edge, start, end)
    remove(n, edge, edge_rev, dp, end)

    return dijkstra(n, edge, start, end)[end]


readline = sys.stdin.readline

while True:
    n, m = map(int, readline().split())

    if not n and not m: break

    s, d = map(int, readline().split())

    edge = [{} for _ in range(n)]
    edge_rev = [{} for _ in range(n)]

    for _ in range(m):
        a, b, w = map(int, readline().split())
        edge[a][b] = w
        edge_rev[b][a] = w

    answer = sol(n, edge, edge_rev, s, d)
    if answer is None: answer = -1

    sys.stdout.write(str(answer) + '\n')
