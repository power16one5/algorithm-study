import sys



def sol(edges):
    dp = [0] * L
    for edge in edges:
        for e in edge:
            dp[e] += 1

    answer = []
    queue = [i for i, v in enumerate(dp[1:], 1) if not v]

    while queue:
        queue_tmp = []

        for q in queue:
            answer.append(q)

            for e in edges[q]:
                dp[e] -= 1

                if not dp[e]: queue_tmp.append(e)
        
        queue = queue_tmp
    
    return answer if len(answer) == N else [0]


readline = sys.stdin.readline
N, M = map(int, readline().split())
L = N + 1

edges = [set() for _ in range(L)]

for _ in range(M):
    order = tuple(map(int, readline().split()))
    
    for i in range(1, order[0]):
        edges[order[i]].update(order[i+1:])

print(*sol(edges), sep='\n')
