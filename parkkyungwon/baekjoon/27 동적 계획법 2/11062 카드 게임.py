import sys
import itertools



def main():
    readline = sys.stdin.readline
    T = int(readline())

    for _ in range(T):
        N = int(readline())
        cards = tuple(map(int, readline().split()))
        dp = list(cards) if N & 1 else [0] * N

        for turn in range(N - 1, 0, -1):
            if turn & 1:
                diff = N - turn
                dp = [lv2 if (lv2 := lv + cards[i + diff]) > (rv2 := rv + cards[i]) else rv2 for i, (lv, rv) in enumerate(itertools.pairwise(dp))]

            else:
                dp = [lv if lv < rv else rv for lv, rv in itertools.pairwise(dp)]
        
        sys.stdout.write(str(dp[0]) + '\n')


main()
