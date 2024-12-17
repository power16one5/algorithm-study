import sys
from collections import defaultdict



def sol(n, m, start):
    lp = m - 1
    end = n * m + 1

    # 왼쪽 끝, 가운데, 오른쪽 끝에 있을 경우 적용할 비트
    lmark = int('0b1' + '0' * (m - 2)  + '11', base=0)
    mmark = int('0b101' + '0' * (m - 3)  + '111', base=0)
    rmark = int('0b1' + '0' * (m - 1)  + '11', base=0)

    # 가장 오른쪽 1비트의 위치를 기준으로 저장하는 dp
    dps = [defaultdict(int) for _ in range(end + 1)]

    i = (start & -start).bit_length()
    if not i: return 0

    dps[i][start] = 0

    for i, dp in zip(range(end), dps):
        j = i - 1

        for bit in dp:
            # 이 위치를 사용하지 않을 때
            next_bit = bit - (1 << j)
            next_i = (next_bit & -next_bit).bit_length()
            if not next_i: next_i = end

            if dps[next_i][next_bit] < dp[bit]: dps[next_i][next_bit] = dp[bit]
        
            # 이 위치를 사용할 때
            r = j % m
            if not r: next_bit = bit & ~(rmark << j)
            elif r == lp: next_bit = bit & ~(lmark << (j - 1))
            else: next_bit = bit & ~(mmark << (j - 1))

            next_i = (next_bit & -next_bit).bit_length()
            if not next_i: next_i = end

            v = dp[bit] + 1
            if dps[next_i][next_bit] < v: dps[next_i][next_bit] = v
        
        # 메모리를 위해 삭제
        dps[i] = None
    
    return max(dps[-1].values(), default=0)


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    C = int(readline())

    for _ in range(C):
        N, M = map(int, readline().split())

        s = ''
        for _ in range(N):
            s += readline().rstrip()

        mt = str.maketrans('.x', '10')
        bit = int('0b' + s.translate(mt), base=0)

        write(str(sol(N, M, bit)) + '\n')


main()
