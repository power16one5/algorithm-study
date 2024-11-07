import sys




class DisjointSet():
    def __init__(self, n):
        self.dp = [None] * n

    def find(self, i):
        if self.dp[i] == None: return i

        r = self.find(self.dp[i])
        if self.dp[i] != r: self.dp[i] = r

        return self.dp[i]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        self.dp[rb] = ra


def sol(datas):
    ds = DisjointSet(G + 1)
    count = 0

    for data in datas:
        r = ds.find(data)

        if not r: break

        ds.union(r-1, r)

        count += 1
    
    return count


readline = sys.stdin.readline
G =int(readline())
P =int(readline())
datas = (int(readline()) for _ in range(P))

print(sol(datas))
