def sol(w, n, arr):
    dp = [None] * 400000
    half = w // 2

    for i in range(n):
        for j in range(i + 1, n):
            v = arr[i] + arr[j]

            if v < half:
                if not dp[v]: 
                    dp[v] = [i, j]
    
            else:
                v = w - v

                if v > 0 and dp[v]:
                    a, b = dp[v]

                    if i != a and i != b and j != a and j != b:
                        return 'YES'

    return 'NO'


W, N = map(int, input().split())
arr = tuple(sorted(map(int, input().split())))

print(sol(W, N, arr))
