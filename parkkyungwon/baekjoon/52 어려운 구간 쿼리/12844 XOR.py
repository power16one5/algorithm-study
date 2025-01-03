import sys



class SegmentTree():
    __slots__ = ['tree', 'lazy', 'adj']

    def __init__(self, n, data):
        self.adj = 1 << n.bit_length()
        size = self.adj << 1
        self.tree = [0] * size
        self.lazy = [0] * size 

        self.tree[self.adj : self.adj + len(data)] = data
        for i in range(size - 1, 1, -1):
            self.tree[i >> 1] ^= self.tree[i]
    
    def _prop(self, i, v):
        i >>= 1
        while i:
            self.tree[i] ^= v
            i >>= 1

    def _get(self, i):
        ret = 0
        while i:
            ret ^= self.lazy[i]
            i >>= 1
        
        return ret

    def update_range(self, s, e, v):
        s += self.adj; e += self.adj

        if s & 1: self._prop(s, v)
        if not (e & 1): self._prop(e, v)

        while s <= e:
            if s & 1: 
                self.lazy[s] ^= v
                s += 1

            if not (e & 1): 
                self.lazy[e] ^= v
                e -= 1
            
            s >>= 1; e >>= 1

    def query_range(self, s, e):
        s += self.adj; e += self.adj
        ret = 0

        if s & 1: ret ^= self._get(s)
        if not (e & 1): ret ^= self._get(e)

        while s <= e:
            if s & 1:
                ret ^= self.tree[s]
                s += 1

            if not(e & 1):
                ret ^= self.tree[e]
                e -= 1

            s >>= 1; e >>= 1

        return ret


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N = int(readline())
    data = list(map(int, readline().split()))
    st = SegmentTree(N, data)
    
    M = int(readline())
    for _ in range(M):
        query = list(map(int, readline().split()))

        match query[0]:
            case 1: st.update_range(query[1], query[2], query[3])
            case 2: write(str(st.query_range(query[1], query[2])) + '\n')


main()
