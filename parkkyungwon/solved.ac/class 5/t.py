import random


print(*[int(random.random() * 2e9) - 1000000000 for _ in range(5000)])
