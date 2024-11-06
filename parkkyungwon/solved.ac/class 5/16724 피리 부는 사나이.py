from itertools import chain



def sol(edges_dp, count_dp):
    zone_count = 0

    # 싸이클이 없는 곳 삭제
    queue = [i for i, v in enumerate(count_dp) if not v]

    for i in queue:
        while not count_dp[i]:
            i = edges_dp[i]
            count_dp[i] -= 1
    
    # 싸이클 하나씩 제거
    for i in range(L):
        if not count_dp[i]: continue

        zone_count += 1

        while count_dp[i]:
            count_dp[i] -= 1
            i = edges_dp[i]
    
    return zone_count


ss = open(0).read().splitlines()
N, M = map(int, ss[0].split())
L = N * M

edges_dp = [0] * L
count_dp = [0] * L
for i, direction in enumerate(chain(*ss[1:])):
    match direction:
        case 'D': t = i + M
        case 'U': t = i - M
        case 'L': t = i - 1
        case _:   t = i + 1

    edges_dp[i] = t
    count_dp[t] += 1

del ss

print(sol(edges_dp, count_dp))
