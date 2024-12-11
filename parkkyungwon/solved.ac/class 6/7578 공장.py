class BIT():
    def __init__(self, n):
        self.leng = n
        self.dp = [1] * self.leng
        self.dp[0] = None

        s, diff = 2, 2
        for _ in range(n.bit_length() - 1):
            for i in range(s, n, diff):
                self.dp[i] <<= 1

            s += diff
            diff <<= 1
    
    def query(self, i):
        total = 0

        while i:
            total += self.dp[i]
            i -= i & -i
        
        return total
    
    def update(self, i):
        while i < self.leng:
            self.dp[i] -= 1
            i += i & -i
        

def sol(arr):
    abit = BIT(N + 1)
    total = 0

    for a in arr:
        total += abit.query(a) - 1
        abit.update(a)

    return total


N = int(input())
A = input().split()
mapping = {v: i for i, v in enumerate(input().split(), 1)}

A = list(map(lambda x: mapping[x], A))
del mapping

print(sol(A))
