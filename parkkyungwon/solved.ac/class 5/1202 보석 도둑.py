import sys
from heapq import heappop, heappush



def sol(jewels, bags):
    total = 0
    heap = []
    leng = len(jewels)
    i = 0

    for bag in bags:
        while i < leng and jewels[i][0] <= bag: 
            heappush(heap, -jewels[i][1])
            i += 1

        if heap: total -= heappop(heap)

    return total


readline = sys.stdin.readline
N, K = map(int, readline().split())

jewels = sorted((tuple(map(int, readline().split())) for _ in range(N)), key=lambda x: x[0])
bags = sorted(int(readline()) for _ in range(K))

print(sol(jewels, bags))
