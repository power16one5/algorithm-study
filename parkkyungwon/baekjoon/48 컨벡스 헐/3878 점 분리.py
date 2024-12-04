import sys
from itertools import chain



def ccw(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2 - x1)*(y3 - y2) - (x3 - x2)*(y2 - y1)


def is_touch(a, b, c, d):
    a, b, c, d = [a[1], b[1], c[1], d[1]] if a[0] == b[0] else [a[0], b[0], c[0], d[0]]
    if a > b: a, b = b, a
    if c > d: c, d = d, c
    return a <= d and c <= b


# 선 위의 3점 a, b, c
# a와 b 사이에 c가 존재하는지 판별
def pir(a, b, c):
    if a[0] == b[0]: return (a[1] - c[1])*(b[1] - c[1])
    else: return (a[0] - c[0])*(b[0] - c[0])


def line_point(line, point):
    if ccw(line[0], line[1], point[0]): return False
    elif pir(line[0], line[1], point[0]) <= 0: return True
    else: return False


def cc(a_con, b_con):
    # 선이 겹치는지 판별
    for i in range(-1, len(a_con)-1):
        a, b = a_con[i], a_con[i+1]

        for j in range(-1, len(b_con)-1):
            c, d = b_con[j], b_con[j+1]
            det1 = ccw(a, b, c) * ccw(a, b, d)
            det2 = ccw(c, d, a) * ccw(c, d, b)

            # 모든점이 일직선 위에 존재하면
            if not (det1 or det2): return is_touch(a, b, c, d)
            elif det1 <= 0 and det2 <= 0: return True
    
    # 다각형 내부에 존재하는지 판별
    a, b = a_con[0], b_con[0]

    for i in range(-1, len(a_con)-1):
        if ccw(a_con[i], a_con[i+1], b) >= 0: break
    else: return True

    for i in range(-1, len(b_con)-1):
        if ccw(b_con[i], b_con[i+1], a) >= 0: break
    else: return True

    return False
    

def graham_scan(arr):
    root_x, root_y = min(arr, key=lambda x: (x[0], x[1]))
    arr.sort(key=lambda a: (INF if a[0] == root_x else (root_y - a[1]) / (root_x - a[0]), -a[1]), reverse=True)
    stack = []

    for a in chain(arr, [(root_x, root_y)]):
        while len(stack) > 1 and ccw(stack[-2], stack[-1], a) >= 0:
            stack.pop()
        
        stack.append(a)
    
    stack.pop()

    return stack


def is_overlap(a_dots, b_dots):
    a_ch = graham_scan(a_dots) 
    if len(a_ch) == 1 and len(a_dots) > 1:
        a_ch = [a_dots[0], a_dots[1]]
    
    b_ch = graham_scan(b_dots) 
    if len(b_ch) == 1 and len(b_dots) > 1:
        b_ch = [b_dots[0], b_dots[1]]

    if len(a_ch) == 1 and len(b_ch) == 2:
        return line_point(b_ch, a_ch)

    elif len(a_ch) == 2 and len(b_ch) == 1:
        return line_point(a_ch, b_ch)

    elif len(a_ch) == 1 and len(b_ch) == 1: 
        return False
    
    elif cc(a_ch, b_ch): 
        return True

    return False


readline = sys.stdin.readline
INF = float('inf')

T = int(readline())

for _ in range(T):
    n, m = map(int, readline().split())

    black_dots = [tuple(map(int, readline().split())) for _ in range(n)]
    white_dots = [tuple(map(int, readline().split())) for _ in range(m)]

    sys.stdout.write('NO\n' if is_overlap(black_dots, white_dots) else 'YES\n')
