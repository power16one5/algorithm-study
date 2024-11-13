import sys



def get_dps(edges):
    parent_min_max_dp, depth_dp = [None] * L, [None] * L
    depth_dp[0], depth_dp[1] = 0, 1
    parent_min_max_dp[0] = (0, INF, 0)
    parent_min_max_dp[1] = (1, INF, 0)
    depth = 0
    queue = [1]

    while queue:
        queue_tmp = []
        depth += 1

        for p in queue:
            gp = parent_min_max_dp[p][0]
            for c in edges[p]:
                if gp == c: continue
                
                v = edges[p][c]
                parent_min_max_dp[c] = (p, v, v)
                depth_dp[c] = depth
                queue_tmp.append(c)
                
        
        queue = queue_tmp
    
    return parent_min_max_dp, depth_dp, depth.bit_length()


def lca(a, b):
    mini, maxi = INF, 0

    # a, b의 depth를 맞춤
    if (ad := depth_dp[a]) != (bd := depth_dp[b]):
        # b가 더 깊으면 a와 b를 변경
        if ad < bd: a, b, ad, bd = b, a, bd, ad

        gap = ad - bd
    
        for i in range(gap.bit_length()):
            if (gap >> i) & 1:
                a, dmin, dmax = sparse_dp[i][a]

                if dmin < mini: mini = dmin
                if dmax > maxi: maxi = dmax
    
    while a != b:
        i = 0
        while sparse_dp[i+1][a][0] != sparse_dp[i+1][b][0]: i += 1

        a, a_min, a_max = sparse_dp[i][a]
        b, b_min, b_max = sparse_dp[i][b]

        mini = min(mini, a_min, b_min)
        maxi = max(maxi, a_max, b_max)
        
    return mini, maxi


readline = sys.stdin.readline
N = int(readline())
L = N + 1
INF = float('inf')

# 간선
edges = [{} for _ in range(L)]
for a, b, v in (map(int, readline().split()) for _ in range(N - 1)):
    edges[a][b] = v; edges[b][a] = v

# 깊이, 부모 dp 생성
parent_min_max_dp, depth_dp, max_depth = get_dps(edges)
del edges

# sparse dp
sparse_dp = [parent_min_max_dp]
for _ in range(max_depth):
    sparse = []

    for i in range(L):
        a, a_min, a_max = sparse_dp[-1][i]
        b, b_min, b_max = sparse_dp[-1][a]

        sparse.append((b, a_min if a_min < b_min else b_min, a_max if a_max > b_max else b_max))

    sparse_dp.append(sparse)

for _ in range(int(readline())):
    a, b = map(int, readline().split())

    sys.stdout.write(' '.join(map(str, lca(a, b))) + '\n')
