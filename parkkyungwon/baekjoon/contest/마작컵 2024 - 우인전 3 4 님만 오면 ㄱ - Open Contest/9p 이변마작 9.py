from collections import defaultdict, deque



def main():
    dp = defaultdict(deque)
    mini = INF

    input()
    for i, key in enumerate(input().split()):
        dp[key].append(i)
        
        if len(dp[key]) == 5:
            j = dp[key].popleft()
            diff = i - j + 1
            
            if mini > diff: mini = diff
    
    print(-1 if mini is INF else mini)


INF = float('inf')

main()
