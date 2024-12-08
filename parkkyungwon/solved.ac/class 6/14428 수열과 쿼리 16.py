import sys



class SegmentTree():
    def __init__(self, data):
        leng = len(data)
        self.adj = 1 << leng.bit_length()
        self.indices = [None] * self.adj + [i for i in range(self.adj)]
        self.min_dp = [INF] * (self.adj << 1)
        self.min_dp[self.adj:self.adj + leng] = data

        for i in range(self.adj - 1, 0, -1):
            j = i << 1
            next_j = j + 1

            if self.min_dp[j] > self.min_dp[next_j]:
                self.indices[i] = self.indices[next_j] 
                self.min_dp[i] = self.min_dp[next_j] 
            else:
                self.indices[i] = self.indices[j] 
                self.min_dp[i] = self.min_dp[j] 
    
    def update(self, i, v):
        i += self.adj
        self.min_dp[i] = v
        i >>= 1

        while i:
            j = i << 1
            next_j = j + 1

            if self.min_dp[j] > self.min_dp[next_j]:
                self.indices[i] = self.indices[next_j] 
                self.min_dp[i] = self.min_dp[next_j] 

            else:
                self.indices[i] = self.indices[j] 
                self.min_dp[i] = self.min_dp[j] 

            i >>= 1
    
    def query(self, s, e):
        mini = INF
        index = -1
        s += self.adj; e += self.adj

        while s <= e:
            if s & 1:
                if mini > self.min_dp[s]:
                    mini = self.min_dp[s]
                    index = self.indices[s]
                
                elif mini == self.min_dp[s] and index > self.indices[s]:
                    index = self.indices[s]
                
                s += 1

            if not(e & 1):
                if mini > self.min_dp[e]:
                    mini = self.min_dp[e]
                    index = self.indices[e]

                elif mini == self.min_dp[e] and index > self.indices[e]:
                    index = self.indices[e]

                e -= 1
            
            s >>= 1; e >>= 1
        
        return index


readline = sys.stdin.readline
INF = float('inf')

readline()
data = [INF] + list(map(int, readline().split()))
M = int(readline())

sg = SegmentTree(data)

for _ in range(M):
    op, a, b = map(int, readline().split())

    match op:
        case 1: sg.update(a, b)
        case _: sys.stdout.write(str(sg.query(a, b)) + '\n')
