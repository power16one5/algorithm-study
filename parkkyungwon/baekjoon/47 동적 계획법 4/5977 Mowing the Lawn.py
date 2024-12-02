from collections import deque
import sys



def sol(data):
    total = 0
    max_dq = deque([(-1, 0)])

    for i, v in enumerate(data):
        total += v
        v += max_dq[0][1]

        if max_dq[0][0] == i - K:
            max_dq.popleft()

        while max_dq and max_dq[-1][1] >= v:
            max_dq.pop()
        
        max_dq.append((i, v))
        
    return total - max_dq[0][1]


readline = sys.stdin.readline

N, K = map(int, readline().split())
data = (int(readline()) for _ in range(N))

print(sol(data))
