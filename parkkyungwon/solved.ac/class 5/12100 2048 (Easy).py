import sys
from itertools import cycle



def vector_compress(arr, rev=False):
    filtered_arr = [a for a in (arr[::-1] if rev else arr) if a]
    end = len(filtered_arr) - 1
    compressed = []

    i = 0
    while i < end:
        if filtered_arr[i] == filtered_arr[i+1]:
            compressed.append(filtered_arr[i] << 1)
            i += 2

        else:
            compressed.append(filtered_arr[i])
            i += 1
    
    if i == end: compressed.append(filtered_arr[i])

    return compressed[::-1] if rev else compressed


def sol(arr):
    maxi = 0
    true = cycle([True])

    def backtrack(depth, arr):
        nonlocal maxi
        
        if depth == 5:
            if maxi < (v := max(map(max, arr))): maxi = v
            return

        # 왼쪽
        left = list(map(vector_compress, arr))
        left = [a + [0] * (N - len(a)) for a in left]
        backtrack(depth + 1, left)

        # 오른쪽
        right = list(map(vector_compress, arr, true))
        right = [[0] * (N - len(a)) + a for a in right]
        backtrack(depth + 1, right)

        # 수직으로 압축
        vert = [list(a) for a in zip(*arr)]

        # 위쪽
        up = list(map(vector_compress, vert))
        up = [a + [0] * (N - len(a)) for a in up]
        backtrack(depth + 1, up)

        # 아래쪽
        down = list(map(vector_compress, vert, true))
        down = [[0] * (N - len(a)) + a for a in down]
        backtrack(depth + 1, down)

    backtrack(0, arr)

    return maxi


readline = sys.stdin.readline
N = int(readline())

arr = [list(map(int, a.split())) for a in sys.stdin.read().splitlines()]

print(sol(arr))
