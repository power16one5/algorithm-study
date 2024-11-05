def sol(arr):
    N = len(arr)
    min_v = float('inf')
    min_arr = None
    leng = N - 1

    for i in range(N):
        target = -arr[i]

        s, e = i+1, leng

        while s < e:
            v1 = arr[s] + arr[e]
            v2 = arr[i] + v1
            
            if v2 < 0: v2 = -v2

            if v2 < min_v:
                min_v = v2
                min_arr = (i, s, e)
            
            if v1 > target: e -= 1
            else: s += 1
    
    return (arr[i] for i in min_arr)


N = int(input())
arr = sorted(map(int, input().split()))

print(*sol(arr))
