# D = 최대 차이
# dp[i] = data[i] + max(dp[j] (i-D <= j < i), 0)
from collections import deque



def sol(data):
    max_dq = deque([(0, NINF)])
    maxi = NINF

    for i, v in enumerate(data):
        if max_dq[0][0] < i - D:
            max_dq.popleft()
        
        # 최대 값이 0 보다 작으면 i부터 시작
        if max_dq[0][1] > 0:
            v += max_dq[0][1]

        while max_dq and max_dq[-1][1] <= v:
            max_dq.pop()
      
        max_dq.append((i, v))

        if maxi < max_dq[0][1]:
            maxi = max_dq[0][1]

    return maxi


NINF = -float('inf')

N, D = map(int, input().split())
data = list(map(int, input().split()))

print(sol(data))
