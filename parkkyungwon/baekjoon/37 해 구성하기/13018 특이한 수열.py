def main():
    n, k = map(int, input().split())

    if n - 1 < k:
        print('Impossible')
        return
    
    print(*range(2, n - k + 1), 1, *range(n - k + 1, n + 1))


main()
