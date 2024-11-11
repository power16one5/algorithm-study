from sys import stdin



def sol(sharks):
    count = 0
    map_dp1 = [[False] * C for _ in range(R)]
    map_dp2 = [[False] * C for _ in range(R)]
    row_limit, col_limit = R - 1, C - 1
    row_limit_x2, col_limit_x2 = 2*row_limit, 2*col_limit
    queue = []

    for shark_y, shark_x, s, d, z in sharks: 
        map_dp1[shark_y][shark_x] = (s, d, z)
        queue.append((shark_y, shark_x))

    for human_y in range(C):
        queue_tmp = []

        for human_x in range(R):
            if map_dp1[human_x][human_y]:
                count += map_dp1[human_x][human_y][2]
                map_dp1[human_x][human_y] = False
                break
        
        for shark_y, shark_x in queue:
            if not map_dp1[shark_y][shark_x]: continue

            s, d, z = map_dp1[shark_y][shark_x]
            map_dp1[shark_y][shark_x] = False

            match d:
                case 1:
                    shark_y = shark_y - s

                    if 0 > shark_y >= -row_limit:
                        shark_y = -shark_y
                        d = 2

                    elif shark_y < -row_limit:
                        shark_y += row_limit_x2

                case 2:
                    shark_y = shark_y + s

                    if row_limit < shark_y <= row_limit_x2:
                        shark_y = row_limit_x2 - shark_y
                        d = 1
                        
                    elif shark_y > row_limit_x2:
                        shark_y -= row_limit_x2
            
                case 3:
                    shark_x = shark_x + s

                    if col_limit < shark_x <= col_limit_x2:
                        shark_x = col_limit_x2 - shark_x
                        d = 4
                        
                    elif shark_x > col_limit_x2:
                        shark_x -= col_limit_x2

                case 4:
                    shark_x = shark_x - s

                    if 0 > shark_x >= -col_limit:
                        shark_x = -shark_x
                        d = 3

                    elif shark_x < -col_limit:
                        shark_x += col_limit_x2

            if not map_dp2[shark_y][shark_x]:
                map_dp2[shark_y][shark_x] = (s, d, z)
                queue_tmp.append((shark_y, shark_x))

            elif z > map_dp2[shark_y][shark_x][2]:
                map_dp2[shark_y][shark_x] = (s, d, z)
            
        map_dp1, map_dp2 = map_dp2, map_dp1
        queue = queue_tmp

    return count


R, C, M = map(int, stdin.readline().split())

sharks = [0] * M

for i in range(M):
    r, c, s, d, z = map(int, stdin.readline().split())

    # (axis - 2)의 배수만큼 이동하면 제자리
    s %= (2 * (C if d // 3 else R) - 2)

    sharks[i] = (r-1, c-1, s, d, z)

print(sol(sharks))
