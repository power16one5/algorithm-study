import sys



def sol(edge, edge_rev, indegree, start, end):
    weight = [0] * L

    queue = [start]
    # 탐색
    for q in queue:
        for e in edge[q]:
            v = weight[q] + edge[q][e]

            if weight[e] < v:
                weight[e] = v
            
            indegree[e] -= 1
            if not indegree[e]:
                queue.append(e)
    
    queue = [end]
    visit = bytearray(L)
    count = 0
    # 역추적
    for q in queue:
        for e in edge_rev[q]:
            if weight[q] - edge_rev[q][e] == weight[e]:
                count += 1

                if visit[e]: continue
                visit[e] = 1

                queue.append(e)

    return weight[end], count


readline = sys.stdin.readline
N = int(readline())
M = int(readline())
L = N + 1

indegree = [0] * L
edge = [{} for _ in range(L)]
edge_rev = [{} for _ in range(L)]
for _ in range(M):
    a, b, c = map(int, readline().split())
    edge[a][b] = c
    edge_rev[b][a] = c
    indegree[b] += 1

start, end = map(int, readline().split())

print(*sol(edge, edge_rev, indegree, start, end), sep='\n')
