from bisect import bisect_right



class DisjointSet():
    def __init__(self, n):
        self.dp = [None] * n

    def find(self, i):
        if self.dp[i] == None: return i

        r = self.find(self.dp[i])
        if self.dp[i] != r: self.dp[i] = r

        return self.dp[i]
    
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)

        self.dp[ra] = rb


def sol(cards, op_cards):
    cards.sort()
    ds = DisjointSet(M)
    answer = [None] * K
    end = M - 1

    for i, op_card in enumerate(op_cards):
        j = bisect_right(cards, op_card)
        rj = ds.find(j)
        answer[i] = cards[rj]

        if rj < end: ds.union(rj, rj+1)
    
    return answer


N, M, K = map(int, input().split())
cards = list(map(int, input().split()))
op_cards = tuple(map(int, input().split()))

print(*sol(cards, op_cards), sep='\n')
