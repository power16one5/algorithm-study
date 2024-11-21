import sys



class SegmentTree():
    def __init__(self, data):
        self.adj = len(data)
        self.dp = [[INF, 0] for _ in range(self.adj)]
        self.dp += [[a, a] for a in data]

        for i in range((self.adj - 1), 0, -1):
            self.__update(i)
        
    def __update(self, i):
        j = i << 1; k = j + 1

        self.dp[i][0] = self.dp[j][0] if self.dp[j][0] < self.dp[k][0] else self.dp[k][0]
        self.dp[i][1] = self.dp[j][1] if self.dp[j][1] > self.dp[k][1] else self.dp[k][1]

    def change(self, i, j):
        i += self.adj; j += self.adj
        self.dp[i], self.dp[j] = self.dp[j], self.dp[i]

        while i:
            i >>= 1; j >>= 1

            # i와 j가 만나면 둘 중 하나만 갱신하면 되므로
            if i == j: break
            
            self.__update(i); self.__update(j)
        
        while i:
            i >>= 1
            self.__update(i)

    def interval_sum(self, s, e):
        mini, maxi = INF, 0
        s += self.adj; e += self.adj

        while s <= e:
            if s & 1:
                if mini > self.dp[s][0]: mini = self.dp[s][0]
                if maxi < self.dp[s][1]: maxi = self.dp[s][1]
                s += 1
            
            if not(e & 1):
                if mini > self.dp[e][0]: mini = self.dp[e][0]
                if maxi < self.dp[e][1]: maxi = self.dp[e][1]
                e -= 1
            
            s >>= 1; e >>= 1

        return mini, maxi


readline = sys.stdin.readline
INF = float('inf')
T = int(readline())

for _ in range(T):
    N, M = map(int, readline().split())

    st = SegmentTree([i for i in range(N)])

    for _ in range(M):
        op, a, b = map(int, readline().split())

        if op: 
            mini, maxi = st.interval_sum(a, b)
            sys.stdout.write('NO\n' if mini < a or maxi > b else 'YES\n')
        
        else:
            st.change(a, b)
