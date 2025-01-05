import sys



class DSLR():
    __slots__ = ['fw_path', 'bw_path', 'fw_char', 'bw_char', 'size', 'visit', 'parent', 'command']

    def __init__(self):
        self.size = 10000
        self.fw_path = [(i-1 if i else 9999, 10*i%self.size + i//1000, i//10 + 1000*i%self.size, 2*i%self.size) for i in range(self.size)]
        self.bw_path = [(0 if i == 9999 else i+1, i//10 + 1000*i%self.size, 10*i%self.size + i//1000, j := i//2, j+5000)
                        if i % 2 == 0 else 
                        (0 if i == 9999 else i+1, i//10 + 1000*i%self.size, 10*i%self.size + i//1000) for i in range(self.size)]
        self.fw_char = ('S', 'L', 'R', 'D')
        self.bw_char = ('S', 'L', 'R', 'D', 'D')

    def bfs(self, start, end):
        self.visit[start] = 1
        self.visit[end] = 10000
        fw_queue = [start]
        bw_queue = [end]

        for i, j in zip(range(2, 5000), range(9999, 5000, -1)):
            tmp_queue = []
            for u in fw_queue:
                for v, c in zip(self.fw_path[u], self.fw_char):
                    if self.visit[v] is None:
                        self.visit[v] = i
                        self.parent[v] = u
                        self.command[v] = c
                        tmp_queue.append(v)
                    
                    elif self.visit[v] > 5000: return u, v, c
            
            fw_queue = tmp_queue

            tmp_queue = []
            for v in bw_queue:
                for u, c in zip(self.bw_path[v], self.bw_char):
                    if self.visit[u] is None:
                        self.visit[u] = j
                        self.parent[u] = v
                        self.command[u] = c
                        tmp_queue.append(u)

                    elif self.visit[u] < 5000: return u, v, c
            
            bw_queue = tmp_queue

    def backtrack(self, u, v, c):
        answer = []

        while self.parent[u] is not None:
            answer.append(self.command[u])
            u = self.parent[u]
        
        answer = answer[::-1]
        answer.append(c)

        while self.parent[v] is not None:
            answer.append(self.command[v])
            v = self.parent[v]

        return ''.join(answer)

    def sol(self, start, end):
        self.visit = [None] * self.size
        self.parent = [None] * self.size
        self.command = [None] * self.size

        u, v, c = self.bfs(start, end)
        return self.backtrack(u, v, c)


def main():
    readline = sys.stdin.readline
    T = int(readline())
    dslr = DSLR()

    for _ in range(T):
        A, B = map(int, readline().split())

        sys.stdout.write(dslr.sol(A, B) + '\n')


main()
