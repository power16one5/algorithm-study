import sys



def main():
    readline = sys.stdin.readline
    s, e = 1, 10 ** 9
    
    for _ in range(29):
        n = int(readline())
        gt = e - n
        lt = n - s

        if gt > lt:
            print('>', flush=True)
            if n >= s: s = n + 1
        
        else:
            print('<', flush=True)
            if n <= e: e = n - 1
    
    for _ in range(71):
        n = int(readline())

        if n < s:
            print('>', flush=True)
        
        elif n > e:
            print('<', flush=True)

        else:
            print('=', flush=True)
            break


main()
