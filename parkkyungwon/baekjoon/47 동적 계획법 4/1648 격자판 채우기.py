from collections import defaultdict



def sol(n, m):
    leng = n * m
    dp = [defaultdict(int) for _ in range(leng + 1)]
    dp[0][0] = 1

    h_mask = 0
    for i in range(m, (n + 1) * m, m):
        h_mask += 1 << i
    
    v_limit = leng - m

    for i in range(leng - 1):
        for j in dp[i]:
            # 가장 오른쪽 0 비트 위치
            bit = ~j & (j + 1)
            common = j | bit
            
            # 가로 블럭
            hbit = bit << 1
            if not((hbit & h_mask) or (j & hbit)):
                h = common | hbit
                next_i = (~h & (h + 1)).bit_length() - 1
                dp[next_i][h] = (dp[next_i][h] + dp[i][j]) % MOD

            # 세로 블럭
            if i < v_limit:
                vbit = bit << m
                v = common | vbit
                next_i = (~v & (v + 1)).bit_length() - 1
                dp[next_i][v] = (dp[next_i][v] + dp[i][j]) % MOD

    return dp[-1][(1 << leng) - 1]


MOD = 9901

N, M = map(int, input().split())

print(sol(N, M))
