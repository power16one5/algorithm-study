from itertools import chain



def sol(source, target):
    # 현재 돌아간 위치
    dp = [INF] * 10
    dp[0] = 0

    for s, e in zip(source, target):
        dp_tmp = [0] * 10

        left = (e - s) % 10
        right = (10 - left) % 10

        # right
        for i, j in zip(range(10), chain(range(right, 10), range(0, right))):
            dp_tmp[i] = dp[i] + j
        
        # left
        for i, j in zip(range(10), chain(range(left, -1, -1), range(9, left, -1))):
            v = dp[i] + j
            k = (i + j) % 10

            if dp_tmp[k] > v: dp_tmp[k] = v
    
        dp = dp_tmp
    
    return min(dp)


INF = float('inf')

input()
source = map(int, input())
target = map(int, input())

print(sol(source, target))
