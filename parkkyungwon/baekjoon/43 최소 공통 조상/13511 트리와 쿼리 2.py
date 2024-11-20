import sys



def get_dps():
    # 1을 루트 노드로 정하고 depth와 1번째 sparse를 제작
    sparse_dp, depth_dp = [None] * L, [None] * L
    sparse_dp[0], sparse_dp[1] = (0, 0), (1, 0)
    depth_dp[1] = 0
    queue, depth = [1], 0

    while queue:
        queue_tmp = []
        depth += 1

        for p in queue:
            gp = sparse_dp[p][0]

            for c in edges[p]:
                if gp == c: continue

                depth_dp[c] = depth
                sparse_dp[c] = (p, edges[p][c])
                queue_tmp.append(c)

        queue = queue_tmp
    
    sparse_dp = [tuple(sparse_dp)]
    for _ in range(depth.bit_length()):
        sparse_dp.append(tuple((sparse_dp[-1][a][0], sparse_dp[-1][a][1] + v) for a, v in sparse_dp[-1]))
    
    return sparse_dp, depth_dp


def move(a, distance):
    while distance:
        bit = distance & -distance
        a = sparse_dp[bit.bit_length() - 1][a][0]
        distance ^= bit

    return a


def query1(a, b):
    total = 0

    if (ad := depth_dp[a]) != (bd := depth_dp[b]):
        if ad < bd: a, b, ad, bd = b, a, bd, ad
        gap = ad - bd

        while gap:
            bit = gap & -gap
            i = bit.bit_length() - 1
            total += sparse_dp[i][a][1]
            a = sparse_dp[i][a][0]
            gap ^= bit

    if a != b:    
        for i in range(SPARSE_LENG-1, -1, -1):
            if sparse_dp[i][a][0] != sparse_dp[i][b][0]:
                total += sparse_dp[i][a][1] + sparse_dp[i][b][1]
                a, b = sparse_dp[i][a][0], sparse_dp[i][b][0]

        total += sparse_dp[0][a][1] + sparse_dp[0][b][1]
        a, b = sparse_dp[0][a][0], sparse_dp[0][b][0]

    return total


def query2(a, b, k):
    ai, bi = a, b
    is_gap_exist = False

    if (ad := depth_dp[ai]) != (bd := depth_dp[bi]):
        is_gap_exist = True
        
        if ad > bd:
            gap = ad - bd
            ai = move(ai, gap)
            is_gap_left = True
            
        else: 
            gap = bd - ad
            bi = move(bi, gap)
            is_gap_left = False

    distance = 1
    
    if ai != bi:    
        for i in range(SPARSE_LENG-1, -1, -1):
            if sparse_dp[i][ai][0] != sparse_dp[i][bi][0]:
                distance += 2 << i
                ai, bi = sparse_dp[i][ai][0], sparse_dp[i][bi][0]

        distance += 2
        ai, bi = sparse_dp[0][ai][0], sparse_dp[0][bi][0]

    lca_rel_idx = distance // 2

    if is_gap_exist:
        if is_gap_left: lca_rel_idx += gap
        
        distance += gap
        
    return move(a, k - 1) if k <= lca_rel_idx else move(b, distance - k)


readline = sys.stdin.readline
N = int(readline())
L = N + 1

edges = [{} for _ in range(L)]
for _ in range(N - 1):
    a, b, v = map(int, readline().split())
    edges[a][b] = v; edges[b][a] = v

sparse_dp, depth_dp = get_dps()
SPARSE_LENG = len(sparse_dp)
del edges

M = int(readline())
for _ in range(M):
    quary = list(map(int, readline().split()))

    match quary[0]:
        case 1: answer = query1(quary[1], quary[2])
        case _: answer = query2(*quary[1:])
    
    sys.stdout.write(str(answer) + '\n')
