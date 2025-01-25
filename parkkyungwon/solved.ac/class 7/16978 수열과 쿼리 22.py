import sys



class BIT():
    __slots__ = ('size', 'tree', 'origin')

    def __init__(self, arr):
        self.size = len(arr)
        self.tree = arr
        self.origin = arr.copy()

        start = 2
        step, half = 2, 1
        while start < self.size:
            for i in range(start, self.size, step):
                self.tree[i] += self.tree[i - half]
            
            start += step
            half = step; step <<= 1


    def update(self, i, v):
        v -= self.origin[i]
        self.origin[i] += v
        
        while i < self.size:
            self.tree[i] += v
            i += -i & i

    def query(self, i):
        total = 0

        while i:
            total += self.tree[i]
            i -= -i & i
        
        return total

    def interval_query(self, s, e):
        return self.query(e) - self.query(s)


def main():
    readline = sys.stdin.readline

    readline()
    arr = [0] + list(map(int, readline().split()))
    sg = BIT(arr)

    one_querys = []
    two_querys = []
    M = int(readline())
    for _ in range(M):
        query = list(map(int, readline().split()))
        match query[0]:
            case 1: one_querys.append(query[1:])
            case _: two_querys.append((len(two_querys), query[1], query[2] - 1, query[3]))
    
    two_querys.sort(key=lambda x: x[1])
    answer = [None] * len(two_querys)
    
    state = 0
    for query in two_querys:
        while state < query[1]:
            sg.update(*one_querys[state])
            state += 1
        
        answer[query[0]] = sg.interval_query(*query[2:])
    
    print(*answer, sep='\n')


main()
