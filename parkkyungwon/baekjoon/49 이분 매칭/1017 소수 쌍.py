def sieve(n):
    leng = n + 1
    dp = bytearray(leng)
    dp[0], dp[1] = 1, 1
    end = int(n ** (0.5)) + 1

    for i in range(2, end):
        if dp[i]: continue

        for j in range(i + i, leng, i):
            dp[j] = 1
    
    return dp


def bimat(n, edge, a, b):
    pair = [None] * n
    pair[a] = b; pair[b] = a
    level = [0] * n

    def bfs():
        queue = []
        flag = False

        for u in range(n):
            if pair[u] is None: queue.append(u)
            else: level[u] = None
        
        for u in queue:
            for v in edge[u]:
                u2 = pair[v]

                if u2 is None: 
                    flag = True

                elif level[u2] is None:
                    level[u2] = level[u] + 1
                    queue.append(u2)
        
        return flag
    
    def dfs(u):
        next_level = level[u] + 1

        for v in edge[u]:
            u2 = pair[v]

            if u2 is None or (level[u2] == next_level and dfs(u2)):
                pair[u] = v; pair[v] = u
                return True
        
        level[u] = 0
        return False
    
    matched = 0

    while bfs():
        for u in range(1, n):
            if pair[u] is None and dfs(u): matched += 1
    
    return matched


def main():
    N = int(input())

    # 홀수면 안됨
    if N & 1:
        print(-1)
        return

    arr = tuple(map(int, input().split()))
    edge = [[] for _ in range(N)]

    prime = sieve(2 * max(arr))

    for i in range(N):
        a = arr[i]
        for j in range(i + 1, N):
            b = a + arr[j]
            if prime[b]: continue

            edge[i].append(j); edge[j].append(i)
    
    tmp1 = edge[0]
    edge[0] = []
    match_num = (N >> 1) - 1
    answer = []
    
    for i in tmp1:
        tmp2 = edge[i]
        edge[i] = []
        
        if match_num == bimat(N, edge, 0, i):
            answer.append(arr[i])

        edge[i] = tmp2
    
    if answer:
        answer.sort()
        print(*answer, sep=' ')
    
    else:
        print(-1)


main()
