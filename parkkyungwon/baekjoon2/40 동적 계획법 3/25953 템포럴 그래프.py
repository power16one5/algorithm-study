import sys



def main():
    readline = sys.stdin.readline
    
    num_vertex, num_time, num_edge = map(int, readline().split())
    start, end = map(int, readline().split())
    INF = float('INF')
    dp1 = [INF] * num_vertex
    dp1[start] = 0

    for _ in range(num_time):
        dp2 = dp1.copy()

        for _ in range(num_edge):
            u, v, w = map(int, readline().split())

            value = dp1[u] + w
            if dp2[v] > value: dp2[v] = value
            value = dp1[v] + w
            if dp2[u] > value: dp2[u] = value
        
        dp1 = dp2

    print(dp1[end] if dp1[end] != INF else -1)
    

main()
