def sol(arr):
    if not arr: return 0

    leng = len(arr)
    cost = [[3] * 5 for _ in range(5)]
    inf = float('inf')

    for i in range(1, 5): 
        cost[0][i] = 2
        cost[i][i] = 1
    cost[1][3], cost[3][1], cost[2][4], cost[4][2] = [4] * 4

    # n * 5 배열
    # dp[y][x] 는 한 발은 arr[y], 다른 한 발은 x
    dp = [[inf] * 5 for _ in range(leng)]
    dp[0][0] = 2
    
    for i in range(leng-1):
        for j in range(5):
            next_i = i + 1
            cur_step = arr[i]
            next_step = arr[next_i]

            # 바로 이전에 사용한 발을 이번에도 사용한 경우
            if (v := dp[i][j] + cost[cur_step][next_step]) < dp[next_i][j]:
                dp[next_i][j] = v

            # 바로 이전에 사용하지 않은 발을 사용한 경우
            if (v := dp[i][j] + cost[j][next_step]) < dp[next_i][cur_step]:
                dp[next_i][cur_step] = v

    return min(dp[-1])


arr = list(map(int, input().split()))
del arr[-1]

print(sol(arr))
