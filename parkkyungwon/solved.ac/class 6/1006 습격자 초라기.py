import sys



def find(n, w, arr1, arr2):
    # arr1[i], arr2[i] 까지 채워진 dp
    # arr1[i + 1], arr2[i] 까지 채워진 dp
    # arr1[i], arr2[i + 1] 까지 채워진 dp
    dpa, dpb, dpc = [[INF] * (n + 1) for _ in range(3)]
    dpa[0], dpb[0], dpc[0] = 0, 1, 1

    for i in range(1, n + 1):
        i1 = i - 1
        i2 = i - 2

        dpa[i] = min(dpa[i], dpb[i1], dpc[i1], 
                     dpa[i1] if arr1[i1] + arr2[i1] <= w else INF, 
                     dpa[i2] + 1 if arr1[i1] + arr1[i2] <= w and arr2[i1] + arr2[i2] <= w else INF) + 1

        dpb[i] = min(dpa[i], dpc[i1] if arr1[i] + arr1[i1] <= w else INF) + 1
        dpc[i] = min(dpa[i], dpb[i1] if arr2[i] + arr2[i1] <= w else INF) + 1
    
    return dpa[-1]


def sol(n, w, arr1, arr2):
    arr1 += dummy; arr2 += dummy
    mini = find(n, w, arr1, arr2)
    
    if n > 1:
        if arr1[0] + arr1[-2] <= w:
            v1, v2 = arr1[0], arr1[-2]
            arr1[0], arr1[-2] = INF, INF

            tmp =  find(n, w, arr1, arr2) - 1
            if mini > tmp: mini = tmp

            arr1[0], arr1[-2] = v1, v2

        if arr2[0] + arr2[-2] <= w:
            v1, v2 = arr2[0], arr2[-2]
            arr2[0], arr2[-2] = INF, INF

            tmp =  find(n, w, arr1, arr2) - 1
            if mini > tmp: mini = tmp

            arr2[0], arr2[-2] = v1, v2

        if arr1[0] + arr1[-2] <= w and arr2[0] + arr2[-2] <= w:
            v1, v2 = arr1[0], arr1[-2]
            v3, v4 = arr2[0], arr2[-2]
            arr1[0], arr1[-2] = INF, INF
            arr2[0], arr2[-2] = INF, INF

            tmp =  find(n, w, arr1, arr2) - 2
            if mini > tmp: mini = tmp

            arr1[0], arr1[-2] = v1, v2
            arr2[0], arr2[-2] = v3, v4
        
    return mini


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    T = int(readline())

    for _ in range(T):
        N, W = map(int, readline().split())
        
        arr1 = list(map(int, readline().split()))
        arr2 = list(map(int, readline().split()))

        write(str(sol(N, W, arr1, arr2)) + '\n')


INF = float('INF')
dummy = [INF]

main()
