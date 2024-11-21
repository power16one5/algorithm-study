class SegmentTree():
    def __init__(self, n):
        self.adj = n
        self.dp = [0] * (2 * self.adj)

    def update(self, i):
        i += self.adj

        while i:
            self.dp[i] += 1
            i >>= 1
    
    def interval_sum(self, s, e):
        total = 0
        s += self.adj; e += self.adj

        while s <= e:

            if s & 1:
                total += self.dp[s]
                s += 1

            if not(e & 1):
                total += self.dp[e]
                e -= 1
            
            s >>= 1; e >>= 1
        
        return total
    

def sol(arr):
    total = 0
    st = SegmentTree(N)
    e = len(arr) - 1

    for s, _ in arr:
        total += st.interval_sum(s, e)
        st.update(s)
    
    return total


N = int(input())
arr = sorted(enumerate(map(int, input().split())), key=lambda x: (x[1], x[0]))

print(sol(arr))
