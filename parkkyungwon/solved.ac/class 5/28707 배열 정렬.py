from heapq import heappush, heappop
import sys



def sol(arr, swaps):
    answer = tuple(sorted(arr))
    visited = {}
    heap = [(0, tuple(arr))]

    while heap:
        cum_cost, case = heappop(heap)

        if cum_cost > visited.get(case, INF): continue
        if case == answer: return cum_cost
        case = list(case)

        for l, r, c in swaps:
            case[l], case[r] = case[r], case[l]
            next_case = tuple(case)

            if visited.get(next_case, INF) > (v := cum_cost + c):
                heappush(heap, (v, next_case))
                visited[next_case] = v

            case[l], case[r] = case[r], case[l]
    
    return -1


readline = sys.stdin.readline
INF = float('inf')

N = int(readline())
arr = list(map(int, readline().split()))
M = int(readline())

swaps = [0] * M
for i in range(M):
    l, r, c = map(int, readline().split())
    swaps[i] = (l-1, r-1, c)

print(sol(arr, swaps))