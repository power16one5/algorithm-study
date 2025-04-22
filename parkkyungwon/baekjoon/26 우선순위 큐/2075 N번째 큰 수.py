from heapq import heapify, heappushpop
import sys



def main():
    readline = sys.stdin.readline
    N = int(readline())
    heap = list(map(int, readline().split()))
    heapify(heap)
    
    for _ in range(N - 1):
        for a in map(int, readline().split()):
            heappushpop(heap, a)

    print(heap[0])


main()
