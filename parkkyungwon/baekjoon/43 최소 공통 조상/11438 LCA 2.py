import sys



def check_depth(edges):
    parent_dp, depth_dp = [0] * L, [0] * L
    queue = [1]
    depth = 1

    while queue:
        queue_tmp = []

        for p in queue:
            gp = parent_dp[p]

            for c in edges[p]:
                if gp == c: continue

                queue_tmp.append(c)
                parent_dp[c] = p
                depth_dp[c] = depth
        
        depth += 1
        queue = queue_tmp

    return parent_dp, depth_dp, (depth - 1).bit_length()


def lca(sparses, a, b):
    # a, b의 depth를 맞춤
    if (ad := depths[a]) != (bd := depths[b]):
        if ad > bd: deeper, gap = a, ad - bd
        else: deeper, gap = b, bd - ad
    
        for i in range(gap.bit_length()):
            if (gap >> i) & 1:
                deeper = sparses[i][deeper]

        if ad > bd: a = deeper
        else: b = deeper
    
    while a != b:
        i = 0
        while sparses[i+1][a] != sparses[i+1][b]: i += 1

        a, b = sparses[i][a], sparses[i][b]

    return a


readline = sys.stdin.readline
N = int(readline())
L = N + 1

# 간선
edges = [[] for _ in range(L)]
for _ in range(N-1):
    a, b = map(int, readline().split())

    edges[a].append(b)
    edges[b].append(a)

# 부모, 깊이 확인
parents, depths, max_sparse_leng = check_depth(edges)
del edges

# sparse 생성
sparses = [parents]
for _ in range(max_sparse_leng):
    sparses.append([sparses[-1][a] for a in sparses[-1]])

# 공통 조상 출력
for _ in range(int(readline())):
    a, b = map(int, readline().split())

    sys.stdout.write(str(lca(sparses, a, b)) + '\n')
