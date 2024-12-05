import sys



def ccw(a, b, c):
    (_, x1, y1), (_, x2, y2), (_, x3, y3) = a, b, c
    return (x2 - x1)*(y3 - y2) - (x3 - x2)*(y2 - y1)


def sol(arr):
    root = min(arr, key=lambda x: (x[1], x[2]))
    root_i, root_x, root_y = root
    arr.pop(root_i)
    arr.sort(key=lambda x: (INF if root_x == x[1] else (root_y - x[2])/(root_x - x[1])))

    # 기울기가 같은 점들은 x 좌표로 정렬
    flag = False
    for i in range(len(arr) - 1):
        next_i = i + 1
        if not ccw(root, arr[i], arr[next_i]):
            if flag: end = next_i 
            else: flag, start, end = True, i, next_i

        elif flag:
            arr[start:end+1] = sorted(arr[start:end+1], key=lambda x: x[1])
            flag = False
    
    # 마지막 까지 같은 기울기가 존재하고, 기울기가 같은 점들은 x 좌표로 역정렬
    if flag:
        func = (lambda x: x[2]) if root_x == arr[start][1] else (lambda x: x[1])
        arr[start:end+1] = sorted(arr[start:end+1], key=func, reverse= True)
    
    return [root] + arr


readline = sys.stdin.readline
INF = float('inf')

T = int(readline())

for _ in range(T):
    arr = readline().split()
    n = int(arr[0])

    arr = [(i >> 1, int(arr[i]), int(arr[i+1])) for i in range(1, 2*n + 1, 2)]

    sys.stdout.write(' '.join(map(lambda x: str(x[0]), sol(arr))) + '\n')
