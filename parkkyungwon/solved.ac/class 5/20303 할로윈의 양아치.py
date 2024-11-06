import sys



class DisjointSet():
    def __init__(self, n, candy):
        self.root_dp = [-1] * n
        self.candy_dp = [0] + candy
    
    def find(self, i):
        if self.root_dp[i] < 0: return i

        if self.root_dp[i] != (r := self.find(self.root_dp[i])): 
            self.root_dp[i] = r
        
        return self.root_dp[i]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb: return

        if self.root_dp[ra] < self.root_dp[rb]:
            self.root_dp[ra] += self.root_dp[rb]
            self.candy_dp[ra] += self.candy_dp[rb]
            self.root_dp[rb] = ra
            self.candy_dp[rb] = 0
        else:
            self.root_dp[rb] += self.root_dp[ra]
            self.candy_dp[rb] += self.candy_dp[ra]
            self.root_dp[ra] = rb
            self.candy_dp[ra] = 0


def sol(friends, candies):
    dp = [-1] * K
    dp[0] = 0
    
    for f1, c1 in zip(friends, candies):
        for i in range(K - f1 - 1, -1, -1):
            if dp[i] < 0: continue
            
            f2 = f1 + i
            c2 = c1 + dp[i]

            if dp[f2] < c2: dp[f2] = c2
    
    return max(dp)


readline = sys.stdin.readline
N, M, K = map(int, readline().split())
arr = list(map(int, readline().split()))

ds = DisjointSet(N + 1, arr)
for _ in range(M):
    a, b = map(int, readline().split())
    ds.union(a, b)

friends = [-size for size in ds.root_dp[1:] if size < 0]
candies = [candy for candy in ds.candy_dp if candy]

print(sol(friends, candies))
