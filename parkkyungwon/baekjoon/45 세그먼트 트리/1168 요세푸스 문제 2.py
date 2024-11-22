import sys



class SegmentTree():
    def __init__(self, n):
        self.adj = 1 << n.bit_length()
        self.dp = [0] * (self.adj << 1)

        for i in range(self.adj + 1, self.adj + n + 1):
            self.dp[i] = 1

        for i in range(self.adj - 1, 0, -1):
            j = i << 1
            self.dp[i] = self.dp[j] + self.dp[j+1]

    def _update(self, i):
        while i:
            self.dp[i] -= 1
            i >>= 1
    
    def delete(self, i):
        j = 1

        while j < self.adj:
            j <<= 1

            if self.dp[j] < i: 
                i -= self.dp[j]
                j += 1
        
        self._update(j)

        return j - self.adj


def sol():
    st = SegmentTree(N)
    answer = []
    i = 0
    op = K - 1
    
    for j in range(N, 0, -1):
        i = (i + op) % j

        answer.append(st.delete(i + 1))
    
    return answer


readline = sys.stdin.readline

N, K = map(int, readline().split())

sys.stdout.write('<' + ', '.join(map(str, sol())) + '>\n')
