def z(string):
    leng = len(string)
    common_pre = [0] * leng
    S = E = 0

    def update_E():
        nonlocal S, E

        S = i
        while E < leng and string[E - S] == string[E]: E += 1

        common_pre[i] = E - S
        E -= 1
    
    for i in range(1, leng):
        if i > E:
            E = i
            update_E()
        
        elif common_pre[j := i - S] <= E - i:
            common_pre[i] = common_pre[j]
        
        else:
            update_E()

    common_pre[0] = leng

    return common_pre


def sol(common, n, k):
    if n <= k: return n

    # 여유 분 추가
    if k:
        common += [k]
        for i in range(n):
            if common[i] == n - i: common[i] += k

    for step in range(n - 1, 0, -1):
        for i in range(step, n, step):
            if common[i] < step: break
        
        else: return step

    return 0


def main():
    N, K = map(int, input().split())
    string = input()
    common = z(string)

    print(sol(common, N, K))


main()
