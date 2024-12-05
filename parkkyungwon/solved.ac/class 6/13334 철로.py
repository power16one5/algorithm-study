def sol(arr, d):
    sweep = []

    for s, e in arr:
        if s > e: s, e = e, s
        if e - s > d: continue

        sweep.append((e, True))
        sweep.append((s + d + 1, False))
    
    sweep.sort()
    count = 0
    maxi = 0

    for _, b in sweep:
        count += 1 if b else -1

        if maxi < count: maxi = count

    return maxi


arr = list(map(int, open(0).read().split()))

n, d = arr[0], arr[-1]
arr = [(arr[i], arr[i+1]) for i in range(1, 2*n + 1, 2)]

print(sol(arr, d))
