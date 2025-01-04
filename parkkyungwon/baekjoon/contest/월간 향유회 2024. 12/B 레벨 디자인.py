def main():
    N = int(input())

    arr = [i for i in range(1, N + 1)]

    for i in range(N - 1, N >> 1, -2):
        arr[i], arr[i-1] = arr[i-1], arr[i]
    
    sum_a = sum(arr[i] for i in range(1, N, 2))
    sum_b = sum(arr[i] for i in range(0, N, 2))

    print(*arr)
    print(sum_a if sum_a > sum_b else sum_b)


main()
