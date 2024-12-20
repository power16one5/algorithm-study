import sys



class UnionFind():
    def __init__(self, n):
        self.parent = [-1] * n
        self.value = [0] * n
    
    def find(self, i):
        if self.parent[i] < 0:
            return i, self.value[i]
        
        self.parent[i], diff = self.find(self.parent[i])
        self.value[i] += diff

        return self.parent[i], self.value[i] 
    
    def union(self, a, b, v):
        (rap, rav), (rbp, rbv) = self.find(a), self.find(b)

        if rap == rbp: return

        self.parent[rbp] = rap
        self.value[rbp] += rav - rbv + v


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    
    while True:
        N, M = map(int, readline().split())

        if not N and not M: break

        uf = UnionFind(N + 1)

        for _ in range(M):
            op = readline().split()
            
            if op[0] == '!': uf.union(*map(int, op[1:]))
            
            else:
                a, b = uf.find(int(op[1])), uf.find(int(op[2]))

                if a[0] != b[0]: write('UNKNOWN\n')
                else: write(str(b[1] - a[1]) + '\n')
        

sys.setrecursionlimit(int(1e5) + 10)

main()
