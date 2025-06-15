import sys



def main():
    readline = sys.stdin.readline()

    N = int(readline())
    N1 = N + 1
    dp = [None] * N1
    edge = [[] for _ in range(N1)]

    for _ in range(N - 1):
        u, v, d = map(int, readline().split())
        edge[u].append((v, d))
        edge[v].append((u, d))
    
    dp[u] = 
    