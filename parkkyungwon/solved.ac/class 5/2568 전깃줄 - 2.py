import sys
from bisect import bisect_right



def sol(a_side):
    b_side = {a_side[a]: a for a in a_side}
    arr = tuple(map(lambda x: a_side[x], sorted(a_side)))
    pos_dp = [None] * N
    lis_dp = [0]

    for i, a in enumerate(arr):
        if lis_dp[-1] < a: 
            j = len(lis_dp)
            lis_dp.append(a)

        else:
            j = bisect_right(lis_dp, a)
            lis_dp[j] = a
        
        pos_dp[i] = j

    lis_leng = len(lis_dp) - 1
    count = lis_leng

    for i in range(N - 1, -1, -1):
        if pos_dp[i] == count:
            del b_side[arr[i]]
            count -= 1

            if not count: break


    return len(arr) - lis_leng, *sorted(b_side.values())


readline = sys.stdin.readline
N = int(readline())

a_side = {a: b for a, b in (map(int, readline().split()) for _ in range(N))}

print(*sol(a_side), sep='\n')
