import sys



def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    t = int(readline())
    for _ in range(t):
        n, _ = map(int, readline().split())

        arr = list(map(int, readline().split()))

        if not arr or arr[0] != 1:
            arr = [1] + arr
        else:
            arr.pop(0)

        write(f"{n} {len(arr)}\n")
        write(" ".join(map(str, arr)) + "\n")


main()
