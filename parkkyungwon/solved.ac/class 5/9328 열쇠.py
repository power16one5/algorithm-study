import sys



def sol(arr, keys, h, w):
    count = 0
    visited_dp = [[False] * w for _ in range(h)]
    direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
    door_key_dp = [[False, False] for _ in range(26)]
    
    for a in keys:
        door_key_dp[a - 97][1] = True

    def parse(i, j):
        nonlocal count

        if visited_dp[i][j] or arr[i][j] == 42: 
            return

        elif arr[i][j] == 46: 
            queue_tmp.append((i, j))

        elif arr[i][j] == 36: 
            queue_tmp.append((i, j))
            count += 1

        elif 64 < arr[i][j] < 91: 
            alpha = arr[i][j] - 65
            door_key_dp[alpha][0] = True

            if door_key_dp[alpha][1]:
                queue_tmp.append((i, j))
            else:
                door_key_dp[alpha].append((i, j))

        else: 
            alpha = arr[i][j] - 97
            door_key_dp[alpha][1] = True

            if door_key_dp[alpha][0]:
                queue_tmp.extend(door_key_dp[alpha][2:])

            queue_tmp.append((i, j))

        visited_dp[i][j] = True

    queue = [(1, 1)]
    visited_dp[1][1] = True

    while queue:
        queue_tmp = []

        for i, j in queue:
            for di, dj in direction:
                di += i
                dj += j

                parse(di, dj)

        queue = queue_tmp

    return count

readline = sys.stdin.readline
T = int(readline())

for _ in range(T):
    h, w = map(int, readline().split())
    w2, h4, w4 = w+2, h+4, w+4

    arr = [[42] * w4]
    arr += [[42, *([46] * w2), 42]]
    for _ in range(h):
        arr += [[42, 46] + list(map(ord, readline().rstrip())) + [46, 42]]
    arr += [[42, *([46] * w2), 42]]
    arr += [[42] * w4]

    keys = readline().rstrip()
    if keys == '0': keys = []
    else: keys = tuple(map(ord, keys))

    print(sol(arr, keys, h4, w4))
