import sys



def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    T = int(readline())
    for _ in range(T):
        N = int(readline())
        arr = list(map(int, readline().split()))

        odd = 0
        for a in arr: 
            if a & 1: odd += 1

        even = N - odd

        larger = odd if odd > even else even
        answer = 'heeda0528\n' if odd == even or not(larger & 1) else 'amsminn\n'
        write(answer)


main()
