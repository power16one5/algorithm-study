def gen(n):
    s, e = 1, n

    while s < e:
        yield s; yield e
        s += 1; e -= 1
    
    if s == e: yield s


def main():
    N = int(input())

    print(*gen(N))


main()
