import sys


def sol(H, W, C, D):
    if H > W + 1: return

    area = H * W
    a = (H * (H - 1)) // 2
    arr = ''

    if C < a: return
    area -= a; C -= a

    for i in range(H - 1, W):
        if C > W - i:
            arr += '1 ' * W
            C -= W - i; area -= a
        
        else:












def main():
    write = sys.stdout.write

    H, W = map(int, input().split())
    C, D = map(int, input().split())

    answer = sol(H, W, C, D)

    if answer:
        pass
    else:
        write('-1\n')
 

main()
