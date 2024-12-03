from itertools import chain
import math



def ccw(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2 - x1)*(y3 - y2) - (x3 - x2)*(y2 - y1)


def graham_scan(arr):
    root_x, root_y = min(arr, key=lambda x: (x[0], x[1]))
    arr.sort(key=lambda a: (INF if a[0] == root_x else (root_y - a[1]) / (root_x - a[0]), -a[1]), reverse=True)
    stack = []

    for a in chain(arr, [(root_x, root_y)]):
        while len(stack) > 2 and ccw(stack[-2], stack[-1], a) >= 0:
            stack.pop()
        
        stack.append(a)
    
    stack.pop()

    return stack


def sol(arr):
    total = 2 * L * math.pi

    if len(arr) == 1: 
        return round(total)

    convex_hull = graham_scan(arr)

    if len(convex_hull) == 2:
        a, b = arr[0], arr[-1]
        total += 2 * ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** (0.5)

    else:
        a = convex_hull[-1]

        for b in convex_hull:
            total += ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** (0.5)
            a = b
    
    return round(total)


INF = float('inf')

arr = list(map(int, open(0).read().split()))
N, L = arr[0], arr[1]

arr = [(arr[i], arr[i+1]) for i in range(2, 2*N + 2, 2)]

print(sol(arr))
