import sys



class BIT():
    def __init__(self, n, m):
        self.adj = n
        self.end = n + 1
        self.leng = n + m + 1
        self.pos = [None] + [n - i for i in range(n)]
        self.tree = [None] + ([1] * n) + ([0] * m)
        
        d = 1
        for _ in range(self.leng.bit_length()):
            for i in range(d, self.leng - d, d << 1):
                self.tree[i + d] += self.tree[i]
            
            d <<= 1
    
    def query(self, i):
        i = self.pos[i]
        total = 0

        while i:
            total += self.tree[i]
            i -= i & -i
        
        return self.adj - total 

    def update(self, i):
        j = self.pos[i]

        while j < self.leng:
            self.tree[j] -= 1
            j += j & -j
        
        j = self.pos[i] = self.end
        self.end += 1

        while j < self.leng:
            self.tree[j] += 1
            j += j & -j


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    T = int(readline())

    for _ in range(T):
        N, M = map(int, readline().split())
        bintree = BIT(N, M)
        answer = [None] * M

        for i, a in enumerate(map(int, readline().split())):
            answer[i] = str(bintree.query(a))
            bintree.update(a)
        
        write(' '.join(answer) + '\n')


main()
