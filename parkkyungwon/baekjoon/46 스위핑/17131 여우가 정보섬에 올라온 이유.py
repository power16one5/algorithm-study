import sys
from collections import defaultdict



class BIT():
    def __init__(self, n):
        self.lim = n
        self.tree = [0] * self.lim
        self.count = [0] * self.lim
    
    def update(self, i):
        self.count[i] += 1

        while i < self.lim:
            self.tree[i] += 1
            i += i & -i
    
    def interval_sum(self, i):
        total = 0

        while i:
            total += self.tree[i]
            i -= i & -i

        return total
    
    def get_count(self, i):
        return self.count[i]


def sol(data):
    tree = BIT(L)
    star_count = 0
    num_of_V = 0

    keys = sorted(data.keys(), reverse=True)
    for key in keys:
        for x in data[key]:
            left = tree.interval_sum(x - 1)
            right = star_count - tree.get_count(x) - left

            num_of_V = (left * right + num_of_V) % MOD

        for x in data[key]:
            tree.update(x)
            
        star_count += len(data[key])
    
    return num_of_V


readline = sys.stdin.readline
L = int(4e5) + 2
ADJ = int(2e5) + 1
MOD = int(1e9) + 7

N = int(readline())

data = defaultdict(list)
for _ in range(N):
    x, y = map(int, readline().split())
    data[y].append(x + ADJ)

print(sol(data))
