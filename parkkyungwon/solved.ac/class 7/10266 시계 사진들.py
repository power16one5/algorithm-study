from itertools import pairwise



def kmp(string):
    leng = len(string) - 1
    dp = [0] * (leng + 1)
    i, j = 1, 0

    while i < leng:
        if string[i] == string[j]:
            i += 1; j += 1
            dp[i] = j
        
        elif not j:
            i += 1

        else:
            j = dp[j]
    
    return dp


def main():
    N = int(input())

    clock1 = sorted(map(int, input().split()))
    clock1 = [b - a for a, b in pairwise(clock1)]

    clock2 = sorted(map(int, input().split()))
    clock2.append(360000 + clock2[0])
    clock2 = [b - a for a, b in pairwise(clock2)]
    clock2 += clock2

    kmp_dp = kmp(clock1)
    answer_leng = N - 1
    leng = len(clock2)
    i = j = 0
    answer = 'impossible'

    while i < leng:
        if clock2[i] == clock1[j]:
            i += 1; j += 1
            if j == answer_leng: 
                answer = 'possible'
                break
        
        elif not j:
            i += 1
        
        else:
            j = kmp_dp[j]

    print(answer)


main()
