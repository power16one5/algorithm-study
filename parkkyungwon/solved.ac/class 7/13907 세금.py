from heapq import heappop, heappush
import sys



def dijkskra(n, s, e, edges):
    INF = float('inf')
    # 행은 노드, 열은 times
    dp = [[INF] * n for _ in range(n)]
    min_times = [n - 1] * n
    min_times[s] = 0
    heap = [(0, 0, s)]

    while heap:
        cost, times, u = heappop(heap)
        if dp[u][times] < cost or min_times[u] < times: continue

        new_times = times + 1
        for v, new_cost in edges[u]:
            new_cost += cost

            if dp[v][new_times] <= new_cost: continue
            if dp[v][min_times[v]] >= new_cost: min_times[v] = new_times
            dp[v][new_times] = new_cost
            if new_times > min_times[v]: continue
            heappush(heap, (new_cost, new_times, v))

    times, costs = [], []
    for i, v in enumerate(dp[e]):
        if v is INF: continue
        times.append(i)
        costs.append(v)

    return times, costs


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
            
    N, M, K = map(int, readline().split())
    S, D = map(int, readline().split())

    N += 1
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b, w = map(int, readline().split())
        edges[a].append((b, w)); edges[b].append((a, w))
    
    times, costs = dijkskra(N, S, D, edges)

    # 인상
    i = costs.index(min(costs)) + 1
    del costs[i:], times[i:]
    write(str(costs[-1]) + '\n')

    for _ in range(K):
        p = int(readline())

        for i in range(len(costs)): 
            costs[i] += times[i] * p

        i = costs.index(min(costs)) + 1
        del costs[i:], times[i:]
        write(str(costs[-1]) + '\n')


main()
