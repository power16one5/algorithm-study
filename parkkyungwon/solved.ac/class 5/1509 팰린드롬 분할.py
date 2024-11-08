# 모든 팰린드롬이 만들어지는 범위를 간선으로 표현
def sol(arr):
    leng = len(arr)
    edges = [[] for _ in range(leng + 1)]

    # 크기가 1인 팰린드롬 간선
    for i in range(1, leng + 1):
        edges[i-1].append(i)

    for i in range(leng):
        # 짝수 팰린드롬 간선
        for s, e in zip(range(i, -1, -1), range(i + 1, leng)):
            if arr[s] != arr[e]: break

            edges[s].append(e + 1)
        
        # 홀수 팰린드롬 간선
        for s, e in zip(range(i - 1, -1, -1), range(i + 1, leng)):
            if arr[s] != arr[e]: break

            edges[s].append(e + 1)
    
    # bfs
    def bfs():
        count = 0
        queue = [0]
        visited = [False] * (leng + 1)
        visited[0] = True

        while 1:
            count += 1
            queue_tmp = []

            for q in queue:
                for e in edges[q]:
                    if visited[e]: continue

                    if e == leng: return count

                    visited[e] = True
                    queue_tmp.append(e)
            
            queue = queue_tmp
    
    return bfs()


arr = input()

print(sol(arr))
