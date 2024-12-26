import sys
from collections import namedtuple



Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['point1', 'point2'])


class Edge():
    __slots__ = ['to', 'rev', 'cap']

    def __init__(self, to, cap):
        self.to = to
        self.cap = cap


class Dinic():
    __slots__ = ['graph', 'graph_iter', 'size', 'level', 'start', 'end', 'INF']

    def __init__(self, n):
        self.INF = float('inf')
        self.size = n
        self.graph = tuple([] for _ in range(n))
    
    def add_edge(self, u, v, cap):
        fw, bw = Edge(v, cap), Edge(u, 0)
        fw.rev, bw.rev = bw, fw
        self.graph[u].append(fw); self.graph[v].append(bw)
    
    def bfs(self):
        self.level = [-1] * self.size
        self.level[self.start] = 0
        queue = [self.start]

        for u in queue:
            next_level = self.level[u] + 1

            for edge in self.graph[u]:
                v = edge.to

                if edge.cap > 0 and self.level[v] < 0:
                    self.level[v] = next_level
                    queue.append(v)

                    if v == self.end: return True
        
        return False
    
    def dfs(self, u, cap):
        if u == self.end: return cap

        for edge in self.graph_iter[u]:
            v = edge.to

            if edge.cap > 0 and self.level[u] < self.level[v]:
                cost = self.dfs(v, cap if cap < edge.cap else edge.cap)

                if cost > 0:
                    edge.cap -= cost
                    edge.rev.cap += cost
                    return cost
        
        return 0
    
    def max_flow(self, start, end):
        flow = 0 
        self.start, self.end = start, end

        while self.bfs():
            self.graph_iter = [iter(self.graph[i]) for i in range(self.size)]

            while True:
                ret = self.dfs(self.start, self.INF)
                if not ret: break

                flow += ret
        
        return flow


def ccw(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2 - x1)*(y3 - y2) - (x3 - x2)*(y2 - y1)


def is_touch(a, b, c, d):
    if a.x == b.x: d1, d2, d3, d4 = a.y, b.y, c.y, d.y
    else: d1, d2, d3, d4 = a.x, b.x, c.x, d.x

    if d1 > d2: d1, d2 = d2, d1
    if d3 > d4: d3, d4 = d4, d3
    if d1 > d3: d1, d2, d3, d4 = d3, d4, d1, d2

    return d2 > d3


def is_overlap(a, b):
    (p1, p2), (p3, p4) = a, b

    det1, det2 = ccw(p1, p2, p3), ccw(p1, p2, p4)
    det3, det4 = ccw(p3, p4, p1), ccw(p3, p4, p2)
    det5, det6 = det1 * det2, det3 * det4

    if ((det5 > 0 or det6 > 0) or # 완전히 교차 하지 않을 때
        (((det1 != 0) ^ (det2 != 0)) and det6 <= 0) # 일직선에 없고 홀이 벽에 있을 때
        ): return False
    
    if not any([det1, det2, det3, det4]): # 일직선
        return is_touch(p1, p2, p3, p4)

    return True


def main():
    readline = sys.stdin.readline

    N, K, H, M = map(int, readline().split())

    lines = []
    prev = Point(*map(int, readline().split()))
    for _ in range(N - 1):
        curr = Point(*map(int, readline().split()))
        lines.append(Line(prev, curr))
        prev = curr
    lines.append(Line(curr, lines[0][0]))

    hole = tuple(Point(*map(int, readline().split())) for _ in range(H))
    mouse = tuple(Point(*map(int, readline().split())) for _ in range(M))

    source = 0; mouse_start = 1
    hole_start = mouse_start + M
    sink = hole_start + H
    mf = Dinic(sink + 1)

    for i in range(mouse_start, hole_start):
        mf.add_edge(0, i, 1)

    for i in range(hole_start, sink):
        mf.add_edge(i, sink, K)
    
    for i, mp in enumerate(mouse, mouse_start):
        for j, hp in enumerate(hole, hole_start):
            for l1 in lines:
                if is_overlap(l1, (hp, mp)): break
                
            else: 
                mf.add_edge(i, j, 1)

    print('Possible' if M == mf.max_flow(source, sink) else 'Impossible')


main()
