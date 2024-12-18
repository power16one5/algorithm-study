from collections import defaultdict



def sol(start):
    INF = float('INF')

    dps = [defaultdict(lambda: INF) for _ in range(101)]
    dps[0][start] = 0

    for pos in range(100):
        curr_dp, next_dp = dps[pos], dps[pos + 1]

        mask = 1 << pos
        if pos % 10: mask += 1 << (pos - 1)
        if pos % 10 != 9: mask += 1 << (pos + 1)
        if pos // 10: mask += 1 << (pos - 10)
        if pos // 10 != 9: mask += 1 << (pos + 10)

        for bit in curr_dp:
            # 다 꺼지면
            if not bit:
                if dps[-1][0] > curr_dp[0]: dps[-1][0] = curr_dp[0]
                continue

            # 가장 오른쪽 1비트 위치를 확인하고, 해당 비트가 변경 불가능하면 패스
            if pos - (bit & -bit).bit_length() > 9: continue

            count = curr_dp[bit]
            if next_dp[bit] > count: next_dp[bit] = count
            if next_dp[bit ^ mask] > (count_p1 := count + 1): next_dp[bit ^ mask] = count_p1
        
        # 메모리 절약
        dps[pos] = None
    
    return -1 if dps[-1][0] is INF else dps[-1][0]


def main():
    start = open(0).read()
    tran = str.maketrans('#O', '01', '\n')
    start = int(start.translate(tran), base=2)

    print(sol(start))


main()
