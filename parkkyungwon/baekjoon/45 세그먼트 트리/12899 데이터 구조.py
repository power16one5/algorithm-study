import sys



class SegmentTree():
    def __init__(self):
        # 포화 이진 트리로 만들지 않으면 오류가 발생
        self.adj = 1 << 22
        self.dp = [0] * (2 * self.adj)

    def update(self, i, v):
        i += self.adj

        while i:
            self.dp[i] += v
            i >>= 1
    
    def delete(self, i):
        j = 1

        while j < self.adj:
            j <<= 1

            if self.dp[j] < i: 
                i -= self.dp[j]
                j += 1
        
        answer = j - self.adj
        self.update(answer, -1)
        
        return answer
        

readline = sys.stdin.readline
st = SegmentTree()

N = int(readline())

for _ in range(N):
    op, a = map(int, readline().split())

    match op:
        case 1: st.update(a, 1)
        case 2: sys.stdout.write(str(st.delete(a)) + '\n')
