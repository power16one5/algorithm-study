import sys



def main():
    readline = sys.stdin.readline
    T = int(readline())

    for _ in range(T):
        N = int(readline())
        cards = tuple(map(int, readline().split()))

        # l과 r사이의 카드
        dp = [[0] * N for _ in range(N)]
        if N & 1:
            for i in range(N):
                dp[i][i] = cards[i]

        for turn in range(N - 1, 0, -1):
            l, r = 0, N - turn

            if turn & 1:
                while r < N:
                    lv = dp[l + 1][r] + cards[l]
                    rv = dp[l][r - 1] + cards[r]
                    dp[l][r] = lv if lv > rv else rv
                    l += 1; r += 1
            
            else:
                while r < N:
                    lv = dp[l + 1][r]
                    rv = dp[l][r - 1]
                    dp[l][r] = lv if lv < rv else rv
                    l += 1; r += 1
        
        sys.stdout.write(str(dp[0][-1]) + '\n')


main()
