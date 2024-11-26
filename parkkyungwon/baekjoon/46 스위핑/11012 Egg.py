import sys


class SegmentTree():
    def __init__(self):
        self.adj = 100001
        self.dp = [0] * (2*self.adj)
    
    def interval_update(self, s, e, v):
        s += self.adj; e += self.adj

        while s <= e:
            if s & 1:
                self.dp[s] += v
                s += 1
            
            if not(e & 1):
                self.dp[e] += v
                e -= 1
            
            s >>= 1; e >>= 1

    def query(self, i):
        total = 0
        i += self.adj

        while i:
            total += self.dp[i]
            i >>= 1
        
        return total
    

def sol(hist):
    st = SegmentTree()
    total = 0

    for a in hist:
        match a[0]:
            case 0: st.interval_update(a[2], a[3], 1)
            case 1: total += st.query(a[2])
            case 2: st.interval_update(a[2], a[3], -1)
    
    return total


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    n, m = map(int, readline().split())
    hist = []

    # folks
    for _ in range(n):
        x, y = map(int, readline().split())
        hist.append((1, y, x))

    # parades
    parades = [list(map(int, readline().split())) for _ in range(m)]
    for x1, x2, y1, y2 in parades:
        hist.append((0, y1, x1, x2))
        hist.append((2, y2, x1, x2))

    # 1순위는 y, 2순위는 op기준으로 정렬
    hist.sort(key=lambda x: (x[1], x[0]))

    sys.stdout.write(str(sol(hist)) + '\n')
