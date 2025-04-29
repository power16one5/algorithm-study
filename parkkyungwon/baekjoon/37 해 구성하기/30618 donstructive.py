N = int(input())

print(*reversed(range(N, 0, -2)), *range(N-1, 0, -2))
