import sys



N, M = map(int, input().split())

arr = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr[i][j] = ((2*i + j) % 5) + 1

for a in arr:
    sys.stdout.write(' '.join(map(str, a)) + '\n')
