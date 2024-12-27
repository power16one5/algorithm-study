import time

# 데이터 준비
N = 500
graph = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        graph[i].append(j)

# 방식 1: 정수 인덱스 사용
start_time = time.time()
for _ in range(100):
    it = [0] * N
    for v in range(N):
        while it[v] < len(graph[v]):
            edge = graph[v][it[v]]
            it[v] += 1
end_time = time.time()
print("정수 인덱스 방식 소요 시간:", end_time - start_time)

# 방식 2: 반복자 사용
start_time = time.time()
for _ in range(100):
    graph_iter = tuple(iter(graph[i]) for i in range(N))
    for v in range(N):
        for edge in graph_iter[v]:
            pass
end_time = time.time()
print("반복자 방식 소요 시간:", end_time - start_time)