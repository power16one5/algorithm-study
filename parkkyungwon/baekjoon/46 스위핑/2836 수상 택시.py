import sys



def sol(data):
    total = 0
    s, e = 0, 0

    for a in data:
        s2, e2 = a

        if s2 > e:
            total += e - s
            s = s2
            
        if e2 > e: e = e2

    total += e - s

    return total


readline = sys.stdin.readline
N, M = map(int, readline().split())
arr = []

for a, b in (map(int, readline().split()) for _ in range(N)):
    if a > b:
        arr.append((b, a))

arr.sort(key=lambda x: x[0])

print(2 * sol(arr) + M)
