class DisjointSet():
    def __init__(self, n):
        self.dp = [-1] * n

    def find(self, i):
        if self.dp[i] < 0: return i

        if self.dp[i] != (r := self.find(self.dp[i])):
            self.dp[i] = r
        
        return self.dp[i]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        if ra == rb: return False

        if self.dp[ra] > self.dp[rb]:
            self.dp[rb] += self.dp[ra]
            self.dp[ra] = rb
        
        else:
            self.dp[ra] += self.dp[rb]
            self.dp[rb] = ra
        
        return True


def sol(coor):
    ds = DisjointSet(N)
    sort_func = lambda x: x[0]
    
    for i in range(3): coor[i].sort(key=sort_func)

    queue = [(co[next_i := i + 1][0] - co[i][0], co[i][1], co[next_i][1]) for co in coor for i in range(N - 1)]
    queue.sort(key=sort_func)
    
    total = 0
    count = N - 1
    for v, a ,b in queue:
        if ds.union(a, b):
            total += v
            count -= 1
    
    return total


arr = open(0).read().splitlines()

N = int(arr[0])

arr = [map(int, a.split()) for a in arr[1:]]
arr = [[(v, i) for i, v in enumerate(a)] for a in zip(*arr)]

print(sol(arr))
