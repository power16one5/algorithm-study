dice = sum(sum(map(int, input().split())) for _ in range(2))
player = (dice - 2) % 4 + 1

print(player)
