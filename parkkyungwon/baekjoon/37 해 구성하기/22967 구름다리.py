import sys



def gen_mst(except_nodes, s, e):
    dp = bytearray(e)

    for i in except_nodes: 
        dp[i] = 1

    for i in range(s, e):
        if not dp[i]: yield i


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N = int(readline())

    edges = [[i] for i in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, readline().split())
        edges[u].append(v)
        edges[v].append(u)
    
    if N < 5:
        need_edge = 0 if N == 2 else 1 if N == 3 else 3
        write(f"{need_edge}\n1\n")

        for u in range(1, N + 1):
            for v in gen_mst(edges[u], 1, N + 1):
                edges[u].append(v)
                edges[v].append(u)
                write(f'{u} {v}\n')
    
    else:
        most = 0
        most_node = 0
        for i in range(1, N + 1):
            leng = len(edges[i])
            if  leng > most:
                most = leng
                most_node = i
            
        write(f"{N - most}\n2\n")

        for v in gen_mst(edges[most_node], 1, N + 1):
            write(f'{most_node} {v}\n')


main()
