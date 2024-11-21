import sys



class SegmentTree():
    def __init__(self, data):
        self.adj = len(data)
        self.dp = [[INF, 0] for _ in range(self.adj)]
        self.dp += [[a, a] for a in data]

        for i in range(len(self.dp) - 1, 0, -2):
            j = i - 1
            k = i >> 1

            self.dp[k][0] = self.dp[i][0] if self.dp[i][0] < self.dp[j][0] else self.dp[j][0]
            self.dp[k][1] = self.dp[i][1] if self.dp[i][1] > self.dp[j][1] else self.dp[j][1]
        
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
N, M = map(int, readline().split())

st = SegmentTree([0] + [int(readline()) for _ in range(N)])

for _ in range(M):
    a, b = map(int, readline().split())

    sys.stdout.write(' '.join(map(str, st.interval_sum(a, b))) + '\n')
