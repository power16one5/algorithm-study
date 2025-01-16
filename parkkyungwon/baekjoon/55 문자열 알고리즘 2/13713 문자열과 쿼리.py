import sys



def z(string):
    leng = len(string)
    common_pre = [0] * leng
    S = E = 0

    def update_E():
        nonlocal S, E

        S = i
        while E < leng and string[E - S] == string[E]:
            E += 1
        
        common_pre[i] = E - S
        E -= 1

    for i in range(1, leng):
        if i > E:
            E = i
            update_E()

        elif common_pre[j := i - S] < E - i + 1: 
            common_pre[i] = common_pre[j]

        else:
            update_E()

    common_pre[0] = leng

    return common_pre


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    string = readline().rstrip()
    dp = z(string[::-1])[::-1]

    M = int(readline())
    for _ in range(M):
        write(str(dp[int(readline()) - 1]) + '\n')


main()
