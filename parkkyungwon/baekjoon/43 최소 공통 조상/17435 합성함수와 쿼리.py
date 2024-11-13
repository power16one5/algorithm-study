import sys



def sol(n, x):
    leng = n.bit_length()

    while leng > len(sparse):
        sparse.append([sparse[-1][a] for a in sparse[-1]])

    for i in range(leng):
        if (n >> i) & 1:
            x = sparse[i][x]

    return x


readline = sys.stdin.readline
M = int(readline())
sparse = [list(map(lambda x: int(x) - 1, readline().split()))]

for _ in range(int(readline())):
    n, x = map(int, readline().split())

    sys.stdout.write(str(sol(n, x-1) + 1) + '\n')
