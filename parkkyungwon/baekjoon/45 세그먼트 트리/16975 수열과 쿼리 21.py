import sys



class SegmentTree():
    def __init__(self, data):
        self.adj = len(data)
        self.dp = [0] * self.adj + data

    def check(self, i):
        total = 0
        i += self.adj

        while i:
            total += self.dp[i]
            i >>= 1
        
        return total
    
    def interval_add(self, s, e, v):
        s += self.adj; e += self.adj

        while s <= e:
            if s & 1:
                self.dp[s] += v
                s += 1

            if not(e & 1):
                self.dp[e] += v
                e -= 1
            
            s >>= 1; e >>= 1


readline = sys.stdin.readline
N = int(readline())
st = SegmentTree([0] + list(map(int, readline().split())))

M = int(readline())
for _ in range(M):
    query = list(map(int, readline().split()))

    if query[0] == 1: st.interval_add(query[1], query[2], query[3])
    else: sys.stdout.write(str(st.check(query[1])) + '\n')
