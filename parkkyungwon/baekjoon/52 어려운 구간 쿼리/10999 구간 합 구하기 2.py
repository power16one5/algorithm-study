import sys



class SegmentTree:
    __slots__ = ['tree', 'lazy', 'size', 'start', 'end', 'value']

    def __init__(self, n, data):
        self.size = 1 << n.bit_length()
        self.tree = [0] * (self.size << 1)
        self.lazy = [0] * (self.size << 1)

        self.tree[self.size : self.size + len(data)] = data
        for i in range(self.size - 1, 0, -1):
            j = i << 1
            self.tree[i] += self.tree[j] + self.tree[j + 1]
    
    def update_range(self, s, e, v):
        self.start, self.end, self.value = s, e, v
        self._update_range(1, 0, self.size - 1)
    
    def query_range(self, s, e):
        self.start, self.end = s, e
        return self._query_range(1, 0, self.size - 1)
    
    def _update_range(self, node, node_s, node_e):
        next_node = node << 1

        if self.lazy[node]:
            self.tree[node] += (node_e - node_s + 1) * self.lazy[node]

            if node < self.size:
                self.lazy[next_node] += self.lazy[node]
                self.lazy[next_node + 1] += self.lazy[node]

            self.lazy[node] = 0

        if node_s > self.end or node_e < self.start: return

        if self.start <= node_s and node_e <= self.end:
            self.tree[node] += (node_e - node_s + 1) * self.value

            if node < self.size:
                self.lazy[next_node] += self.value
                self.lazy[next_node + 1] += self.value
        
        else:
            mid = (node_s + node_e) >> 1
            self._update_range(next_node, node_s, mid)
            self._update_range(next_node + 1, mid + 1, node_e)
            self.tree[node] = self.tree[next_node] + self.tree[next_node + 1]
        
    def _query_range(self, node, node_s, node_e):
        next_node = node << 1

        if self.lazy[node]:
            self.tree[node] += (node_e - node_s + 1) * self.lazy[node]

            if node < self.size:
                self.lazy[next_node] += self.lazy[node]
                self.lazy[next_node + 1] += self.lazy[node]

            self.lazy[node] = 0

        if node_s > self.end or node_e < self.start: return 0
        if self.start <= node_s and node_e <= self.end: return self.tree[node]

        mid = (node_s + node_e) >> 1
        left_sum = self._query_range(next_node, node_s, mid)
        right_sum = self._query_range(next_node + 1, mid + 1, node_e)

        return left_sum + right_sum


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    N, M, K = map(int, readline().split())
    data = [0] + [int(readline()) for _ in range(N)]
    st = SegmentTree(N + 1, data)
    
    for _ in range(M + K):
        query = list(map(int, readline().split()))

        match query[0]:
            case 1: st.update_range(query[1], query[2], query[3])
            case 2: write(str(st.query_range(query[1], query[2])) + '\n')


main()
