import sys



class BIT():
    def __init__(self, n):
        self.leng = n
        self.dp = [0] * self.leng
    
    def update(self, i):
        while i < self.leng:
            self.dp[i] += 1
            i += i & -i
        
    def interval_sum(self, i):
        total = 0

        while i:
            total += self.dp[i]
            i ^= i & -i

        return total


def sol(coordin, n):
    total = 0
    tree = BIT(n + 1)

    for x, _ in coordin:
        total += tree.interval_sum(x)
        tree.update(x)
    
    return total


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    n = int(readline())

    coordin = [list(map(int, readline().split())) for _ in range(n)]
    compress = {i[0] for i in coordin}
    compress = {v: i for i, v in enumerate(sorted(compress, reverse=True), start=1)}
    
    for a in coordin:
        a[0] = compress[a[0]]

    coordin.sort(key=lambda x: (x[1], x[0]))

    sys.stdout.write(str(sol(coordin, n)) + '\n')
