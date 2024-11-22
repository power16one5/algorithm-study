import sys



def sol(data):
    total = 0
    s, e = -int(1e9), -int(1e9)

    for a in data:
        s2, e2 = a

        if s2 > e:
            total += e - s
            s = s2
            
        if e2 > e: e = e2

    total += e - s

    return total


readline = sys.stdin.readline
N = int(readline())

arr = [tuple(map(int, readline().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])

print(sol(arr))
