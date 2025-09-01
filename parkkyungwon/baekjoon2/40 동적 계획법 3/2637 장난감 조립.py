import sys



def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N = int(readline())
    N1 = N + 1
    M = int(readline())

    graph = [[] for _ in range(N1)]
    in_degree = [0] * N1
    base_part = [True] * N1

    for _ in range(M):
        X, Y, K = map(int, readline().split())
        graph[X].append((Y, K))
        in_degree[Y] += 1
        base_part[X] = False
    
    queue = [N]
    for u in queue:
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    dp = [0] * N1
    dp[N] = 1
    for u in queue:
        a = dp[u]
        for v, k in graph[u]:
            dp[v] += a * k

    for i in range(1, N1):
        if base_part[i] and dp[i]:
            write(f'{i} {dp[i]}\n')


main()
