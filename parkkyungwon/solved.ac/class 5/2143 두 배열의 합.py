from collections import defaultdict



def sol(arr1, arr2):
    def count_case(arr):
        cumsum = [0] + arr.copy()
        leng = len(cumsum)

        for i in range(leng-1):
            cumsum[i+1] += cumsum[i]

        dp = defaultdict(int)

        for i in range(leng):
            for j in range(i+1, leng):
                dp[cumsum[j] - cumsum[i]] += 1
        
        return dp
    
    dp1, dp2 = map(count_case, (arr1, arr2))
    count = 0

    for a in dp1:
        if (b := T - a) in dp2:
            count += dp1[a] * dp2[b]
    
    return count


T = int(input())
N = input()
arr1 = list(map(int, input().split()))
M = input()
arr2 = list(map(int, input().split()))

print(sol(arr1, arr2))
