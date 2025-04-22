import sys
from heapq import heappush, heappop



def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    T = int(readline())
    for _ in range(T):
        M = int(readline())

        # 원소
        data = (a for _ in range((M // 10) + 1) for a in map(int, readline().split()))
        # 출력하는 중앙값 개수
        write(str((M >> 1) + 1) + '\n')

        bheap, theap = [], [next(data)]
        # 첫 중앙값
        write(str(theap[0]) + ' ')

        for i, a in enumerate(data, 1):
            heappush(theap, int(a))

            if not(i & 1):
                heappush(bheap, -heappop(theap))

                if theap[0] < -bheap[0]:
                    heappush(theap, -heappop(bheap))
                    heappush(bheap, -heappop(theap))
                
                # 10n 번째 이후 마다 개행
                if i % 20 == 0: write('\n')

                write(str(theap[0]) + ' ')

        write('\n')


main()
