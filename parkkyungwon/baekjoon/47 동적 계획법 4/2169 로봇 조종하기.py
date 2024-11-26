import sys



def sol(data):
    # 라인을 거칠 때마다 최대값을 저장하는 dp
    # 초기 시작은 0, 0에서 시작하기 때문에 0 인덱스 외에 나머지는 -inf
    dp = [-INF] * M
    dp[0] = 0

    for line in data:
        for i, v in enumerate(line):
            dp[i] += v

        from_left = dp.copy()
        for i in range(1, M):
            v = line[i] + from_left[i-1]
            if from_left[i] < v: from_left[i] = v

        from_right = dp.copy()
        for i in range(M-2, -1, -1):
            v = line[i] + from_right[i+1]
            if from_right[i] < v: from_right[i] = v
        
        for i, arr in enumerate(zip(dp, from_left, from_right)):
            v = max(arr)
            if dp[i] < v: dp[i] =v
    
    return dp[-1]


readline = sys.stdin.readline
INF = float('inf')

N, M = map(int, readline().split())
data = (tuple(map(int, readline().split())) for _ in range(N))

print(sol(data))
