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
    arr.sort(key=lambda a: (INF if a[0] == root_x else (a[1] - root_y) / (a[0] - root_x)))
    stack = []

    for a in chain(arr, [(root_x, root_y)]):
        while len(stack) > 1 and ccw_3p(stack[-2], stack[-1], a) <= 0:
            del stack[-1]
        
        stack.append(a)
    
    return stack


def sol(arr):
    arr = graham_scan(arr)

    mini = INF
    i = -len(arr)
    j = i + 1

    while i:
        a, b, c, d = arr[i], arr[i + 1], arr[j], arr[j + 1]
        det = ccw_4p(a, b, c, d)

        if det < 0:
            base = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (0.5)
            height = ccw_4p(a, b, b, c) / base

            if mini > height: mini = height

            i += 1
        
        else: 
            j += 1

    answer = round(mini, 2)
    if mini > answer:
        answer += 0.01

    return answer


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    case_num = 1

    while True:
        N = int(readline())

        if not N: break
        
        arr = [tuple(map(int, readline().split())) for _ in range(N)]

        write(f'Case {case_num}: {sol(arr):.2f}' + '\n')
        case_num += 1


INF = float('inf')

main()
