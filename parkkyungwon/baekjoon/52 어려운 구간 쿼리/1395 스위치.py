import sys



class SegmentTree():
    __slots__ = ['tree', 'lazy', 'adj', 's', 'e']

    def __init__(self, n):
        self.adj = 1 << n.bit_length()
        size = self.adj << 1
        self.tree = [0] * size
        self.lazy = bytearray(size)

    def update_range(self, s, e):
        self.s, self.e = s, e
        self._update_range(self.adj, 1, 0, self.adj - 1)

    def _update_range(self, level, node, node_s, node_e):
        next_node1 = node << 1
        next_node2 = next_node1 + 1
        next_level = level >> 1

        if self.lazy[node]:
            self.tree[node] = level - self.tree[node]

            if node < self.adj:
                self.lazy[next_node1] ^= 1
                self.lazy[next_node2] ^= 1

            self.lazy[node] = 0
        
        if node_e < self.s or node_s > self.e: return
        
        if node_s >= self.s and node_e <= self.e:
            self.tree[node] = level - self.tree[node]
        
            if node < self.adj:
                self.lazy[next_node1] ^= 1
                self.lazy[next_node2] ^= 1

        else:
            mid = (node_s + node_e) >> 1
            self._update_range(next_level, next_node1, node_s, mid)
            self._update_range(next_level, next_node2, mid + 1, node_e)
            self.tree[node] = self.tree[next_node1] + self.tree[next_node2]

    def query_range(self, s, e):
        self.s, self.e = s, e
        return self._query_range(self.adj, 1, 0, self.adj - 1)

    def _query_range(self, level, node, node_s, node_e):
        next_node1 = node << 1
        next_node2 = next_node1 + 1
        next_level = level >> 1

        if self.lazy[node]:
            self.tree[node] = level - self.tree[node]

            if node < self.adj:
                self.lazy[next_node1] ^= 1
                self.lazy[next_node2] ^= 1

            self.lazy[node] = 0
        
        if node_e < self.s or node_s > self.e: return 0 
        
        if node_s >= self.s and node_e <= self.e: return self.tree[node]
        
        mid = (node_s + node_e) >> 1
        left = self._query_range(next_level, next_node1, node_s, mid)
        right = self._query_range(next_level, next_node2, mid + 1, node_e)

        return left + right


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M = map(int, readline().split())
    st = SegmentTree(N + 1)
    
    for _ in range(M):
        query = list(map(int, readline().split()))

        match query[0]:
            case 0: st.update_range(query[1], query[2])
            case _: write(str(st.query_range(query[1], query[2])) + '\n')


main()
