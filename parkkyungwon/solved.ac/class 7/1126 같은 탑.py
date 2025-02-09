def main():
    N = int(input())
    arr = map(int, input().split())
    leng = int(5e5) + 1
    dp1 = [-1] * leng
    dp2 = [-1] * leng
    dp1[0] = dp2[0] = 0
    end = 1

    for a in arr:
        for i in range(end):
            if dp1[i] < 0: continue

            j = i + a
            v = dp1[i]
            if dp2[j] < v: dp2[j] = v
            
            if i > a:
                j = i - a 
                v = dp1[i] + a
            else:
                j = a - i
                v = dp1[i] + i

            if dp2[j] < v: dp2[j] = v
        
        dp1[:] = dp2
        end += a

    print(dp1[0] if dp1[0] else -1)


main()
