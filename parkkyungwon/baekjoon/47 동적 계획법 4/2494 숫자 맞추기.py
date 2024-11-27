import sys


def sol(source, target):
    # 현재 돌아간 위치
    dp = [INF] * 10
    pathes = [[None] * 10 for _ in range(N)]
    dp[0] = 0

    for s, e, path in zip(source, target, pathes):
        dp_tmp = [0] * 10

        left = (e - s) % 10
        right = (10 - left) % 10

        # right
        for i, j in zip(range(10), range(10)):
            j = (right + j) % 10
            dp_tmp[i] = dp[i] + j
            path[i] = -j
        
        # left
        for i, j in zip(range(10), range(10)):
            j = (left - j) % 10
            v = dp[i] + j
            k = (i + j) % 10

            if dp_tmp[k] > v: 
                dp_tmp[k] = v
                path[k] = j
    
        dp = dp_tmp
    
    mini = min(dp)
    i = dp.index(mini)
    shortest = []
    
    for path in reversed(pathes):
        shortest.append(path[i])

        if path[i] > 0:
            i = (i - path[i]) % 10

    return mini, reversed(shortest)


INF = float('inf')
write = sys.stdout.write

N = int(input())
source = map(int, input())
target = map(int, input())

mini, path = sol(source, target)

write(str(mini) + '\n')
for i, v in zip(range(1, N + 1), path):
    write(str(i) + ' ' + str(v) + '\n')
