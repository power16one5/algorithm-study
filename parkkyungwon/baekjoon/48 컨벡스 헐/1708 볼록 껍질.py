def ccw(a, b, c):
    (x1, y1), (x2, y2), (x3, y3) = a, b, c
    return (x2 - x1)*(y3 - y2) - (y2 - y1)*(x3 - x2)


def sol(arr):
    root_x, root_y = min(arr, key=lambda x: (x[0], x[1]))
    arr.sort(key=lambda a: (INF if a[0] == root_x else (a[1] - root_y) / (a[0] - root_x), -a[1]), reverse=True)
    arr.append((root_x, root_y))
    stack = []

    for a in arr:
        while len(stack) > 1 and ccw(stack[-2], stack[-1], a) >= 0:
            stack.pop()
        
        stack.append(a)

    return len(stack) - 1


INF = float('inf')

arr = list(map(int, open(0).read().split()))

N = arr[0]
arr = [(arr[i], arr[i+1]) for i in range(1, 2*N, 2)]

print(sol(arr))
