import sys



def fill_p(Kth, sink_x, sink_y):
    dp = [[-1] * Kth for _ in range(Kth)]
    block_num = 1

    def fill(x, y, sink_x, sink_y, size, shape):
        # shape
        # 0: 0 1  # 1: -1 0  # 2: 2 -1  # 3: 1  2
        #   -1 2        2 1       1  0       0 -1
        nonlocal block_num

        next_size = size >> 1
        nx, ny = x + next_size, y + next_size

        if shape is None:
            if nx <= sink_x:
                if ny <= sink_y: shape = 3
                else: shape = 2
            else:
                if ny <= sink_y: shape = 0
                else: shape = 1

        if size > 1:
            nxm1, nym1 = nx - 1, ny - 1

            match shape:
                case 0:
                    fill(x, y, nxm1, nym1, next_size, 3)
                    fill(nx, y, nx, nym1, next_size, 0)
                    fill(nx, ny, nx, ny, next_size, 1)
                    rest_x, rest_y = x, ny

                case 1:
                    fill(nx, y, nx, nym1, next_size, 0)
                    fill(nx, ny, nx, ny, next_size, 1)
                    fill(x, ny, nxm1, ny, next_size, 2)
                    rest_x, rest_y = x, y

                case 2:
                    fill(nx, ny, nx, ny, next_size, 1)
                    fill(x, ny, nxm1, ny, next_size, 2)
                    fill(x, y, nxm1, nym1, next_size, 3)
                    rest_x, rest_y = nx, y

                case 3:
                    fill(x, ny, nxm1, ny, next_size, 2)
                    fill(x, y, nxm1, nym1, next_size, 3)
                    fill(nx, y, nx, nym1, next_size, 0)
                    rest_x, rest_y = nx, ny

            if size > 2: 
                # 정사각형의 중앙에 블록을 채우기
                fill(nxm1, nym1, None, None, 2, shape)
                # 나머지 부분 채우기
                fill(rest_x, rest_y, sink_x, sink_y, next_size, None)
            
            else: block_num += 1
            
        else: dp[y][x] = block_num
    
    fill(0, 0, sink_x - 1, sink_y - 1, Kth, None)

    return dp


def main():
    Kth = 1 << int(input())
    sink_x, sink_y = tuple(map(int, input().split()))

    dp = fill_p(Kth, sink_x, sink_y)
    
    for a in reversed(dp):
        sys.stdout.write(' '.join(map(str, a)) + '\n')
    

main()
