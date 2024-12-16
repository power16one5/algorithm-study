def sol(w, arr):
    dp = {}
    w2 = w // 2

    for i in range(N):
        for j in range(i + 1, N):
            v = arr[i] + arr[j]

            if v < w2:
                if v not in dp: 
                    dp[v] = [i, j]
    
            else:
                v = w - v

                if v > 0 and v in dp:
                    a, b = dp[v]

                    if i != a and i != b and j != a and j != b:
                        return 'YES'

    return 'NO'


W, N = map(int, input().split())
arr = tuple(sorted(map(int, input().split())))

print(sol(W, arr))
