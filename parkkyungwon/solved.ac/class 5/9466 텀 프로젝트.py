import sys



def sol(n, arr):
    arr = (0, ) + arr
    
    dp = [0] * (n + 1)
    for i in arr[1:]: dp[i] += 1

    queue = [i for i, v in enumerate(dp[1:], 1) if not v]
    
    for q in queue:
        t = arr[q]
        dp[t] -= 1

        if not dp[t]: queue.append(t)
    
    return len(queue)


readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    n = int(readline())
    arr = tuple(map(int, readline().split()))

    sys.stdout.write(str(sol(n, arr)) + '\n')
