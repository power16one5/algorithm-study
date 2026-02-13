import sys



def ex_euclide(a, b):
    b_copy = b
    ac1, ac2 = 1, 0

    while b:
        a, b, ac1, ac2 = b, a % b, ac2, ac1 - (a // b) * ac2
    
    return a, ac1 % b_copy


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    t = int(readline())
    for _ in range(t):
        a, b = map(int, readline().split())

        if b == 1:
            if a == 10 ** 9:
                write("IMPOSSIBLE\n")
            else:
                write(f"{a + 1}\n")

        elif a == 1:
            write(f"1\n")

        else:
            gcd, inv = ex_euclide(b, a)
            write(f"{inv}\n" if gcd == 1 else "IMPOSSIBLE\n")


main()
