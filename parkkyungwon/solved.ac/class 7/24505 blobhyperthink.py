class BIT():
    __slots__ = ('size', 'tree')

    def __init__(self, n):
        self.size = n + 1
        self.tree = [0] * self.size

    def update(self, i, v):
        while i < self.size:
            self.tree[i] += v
            i += i & -i

    def query(self, i):
        total = 0
        while i:
            total += self.tree[i]
            i -= i & -i
        
        return total


def main():
    N = int(input())
    arr = list(map(int, input().split()))
    values = [1] * N
    leng = int(1e5)

    for _ in range(10):
        bit_tree = BIT(leng)

        for i, a in enumerate(arr):
            bit_tree.update(a, values[i])
            values[i] = bit_tree.query(a - 1) % MOD
    
    print(sum(values) % MOD)


MOD = int(1e9) + 7
main()
