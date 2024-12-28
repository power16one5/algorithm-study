from collections import defaultdict



def main():
    dp = defaultdict(int)

    input()
    for i, a in enumerate(input().split(), 1):
        dp[a] += 1
        
        if dp[a] == 5:
            print(i)
            break
    
    else: print(0)

main()
