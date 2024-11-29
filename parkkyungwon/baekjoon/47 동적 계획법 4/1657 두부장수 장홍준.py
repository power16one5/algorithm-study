import sys
from collections import defaultdict



def next_bit(i):
    return (~i & (i + 1)).bit_length() - 1

def sol(n, m, arr):
    leng = n * m
    dp = [defaultdict(int) for _ in range(leng + 1)]
    dp[0][0] = 0

    h_mask = 0
    for i in range(m - 1, n * m, m):
        h_mask |= (1 << i)
    
    v_limit = leng - m

    for i in range(leng):
        for j in dp[i]:
            # 가장 오른쪽 0 비트 위치
            common = ~j & (j + 1)
            bit = j | common

            # 버림
            next_i = next_bit(bit)
            if dp[next_i][bit] < dp[i][j]:
                dp[next_i][bit] = dp[i][j]
            
            # 가로 블럭
            h_bit = common << 1
            if not((common & h_mask) or (bit & h_bit)):
                hori = h_bit | bit
                next_i = next_bit(hori)
                value = dp[i][j] + V_MAT[arr[i]][arr[i+1]]

                if dp[next_i][hori] < value:
                    dp[next_i][hori] = value

            # 세로 블럭
            if i < v_limit:
                vert = (common << m) | bit
                next_i = next_bit(vert)
                value = dp[i][j] + V_MAT[arr[i]][arr[i+m]]

                if dp[next_i][vert] < value:
                    dp[next_i][vert] = value
        
        dp[i] = None

    return dp[-1][(1 << leng) - 1]


readline = sys.stdin.readline
read = sys.stdin.read

N, M = map(int, readline().split())

a_to_i = lambda x: v if (v := ord(x) - 65) < 5 else 4
arr = list(map(a_to_i, read().replace('\n', '')))

V_MAT = ((10, 8, 7, 5, 1),
         (8, 6, 4, 3, 1),
         (7, 4, 3, 2, 1),
         (5, 3, 2, 2, 1),
         (1, 1, 1, 1, 0))

print(sol(N, M, arr))
