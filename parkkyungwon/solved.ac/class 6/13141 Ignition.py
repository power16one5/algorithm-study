import sys



def floyd(dp):
    for k in range(N):
        for i in range(N):
            if i == k: continue

            for j in range(i + 1, N):
                v = dp[i][k] + dp[k][j]

                if dp[i][j] > v:
                    dp[i][j] = v; dp[j][i] = v


def sol(edge1, edge2):
    floyd(edge2)
    mini = INF

    for min_dp in edge2:
        maxi = 0

        for i in range(N):
            for j in edge1[i]:
                # 중복 제거
                if j < i: continue
                
                v = (min_dp[i] + min_dp[j] + edge1[i][j]) / 2

                if maxi < v: maxi = v
    
        if mini > maxi: mini = maxi

    return round(float(mini), 1)


readline = sys.stdin.readline
INF = float('inf')

N, M = map(int, readline().split())
edge1 = tuple({} for _ in range(N))
edge2 = tuple([INF] * N for _ in range(N))

for _ in range(M):
    a, b, c = map(int, readline().split())
    a -= 1; b -= 1

    if edge1[a].get(b, 0) < c:
        edge1[a][b] = c; edge1[b][a] = c

    if edge2[a][b] > c:
        edge2[a][b] = c; edge2[b][a] = c

for i in range(N):
    if edge2[i][i] == INF: edge2[i][i] = 0

print(sol(edge1, edge2))
