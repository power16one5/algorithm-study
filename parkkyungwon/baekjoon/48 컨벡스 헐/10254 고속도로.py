import sys
from itertools import chain



def ccw_3p(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2 - x1)*(y3 - y2) - (y2 - y1)*(x3 - x2)


def ccw_4p(a, b, c, d):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = a, b, c, d
    return (x2 - x1)*(y4 - y3) - (y2 - y1)*(x4 - x3)


def graham_scan(arr):
    root_x, root_y = min(arr, key=lambda x: (x[0], x[1]))
    arr.sort(key=lambda a: (INF if a[0] == root_x else (a[1] - root_y) / (a[0] - root_x), -a[1]), reverse=True)
    stack = []

    for a in chain(arr, [[root_x, root_y]]):
        while len(stack) > 1 and ccw_3p(stack[-2], stack[-1], a) >= 0:
            stack.pop()
        
        stack.append(a)
    
    stack.pop()
    
    return stack


def sol(arr):
    # 도시가 2개면
    if len(arr) == 2: return arr

    candidates = graham_scan(arr)

    # 컨벡스 헐을 구할 수 없으면
    if len(candidates) < 2: 
        return arr[0], arr[-1]

    max_v = 0
    i = -len(candidates)
    j = i + 1

    while i:
        a, b, c, d = candidates[i], candidates[i+1], candidates[j], candidates[j+1]
        det = ccw_4p(a, b, c, d) 
            
        if det >= 0:
            v = (a[0] - c[0])**2 + (a[1] - c[1])**2

            if v > max_v: 
                max_i = a, c
                max_v = v

        if det <= 0: j += 1
        else: i += 1

    return max_i

    
readline = sys.stdin.readline
INF = float('inf')

T = int(readline())

for _ in range(T):
    n = int(readline())
    arr = [list(map(int, readline().split())) for _ in range(n)]

    answer = ' '.join(map(str, (b for a in sol(arr) for b in a))) + '\n'
    sys.stdout.write(answer)
