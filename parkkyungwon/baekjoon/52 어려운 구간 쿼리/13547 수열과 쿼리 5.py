import sys



def sol(arr, queries, m):
    visited = [0] * 1000001
    count = 0
    L, R = 0, 0
    answer = [0] * m

    def add(a):
        nonlocal count
        if not visited[a]: count += 1
        visited[a] += 1

    def sub(a):
        nonlocal count
        visited[a] -= 1
        if not visited[a]: count -= 1

    for l, r, i in queries:
        while R > r: R -= 1; sub(arr[R])
        while R < r: add(arr[R]); R += 1
        while L < l: sub(arr[L]); L += 1
        while L > l: L -= 1; add(arr[L])

        answer[i] = count

    return answer


def main():
    readline = sys.stdin.readline

    N = int(readline())
    arr = list(map(int, readline().split()))
    M = int(readline())

    block_size = N ** (0.5)
    queries = [(a-1, b, i) for i, (a, b) in enumerate(map(int, readline().split()) for _ in range(M))]
    queries.sort(key=lambda x: (x[0] // block_size, x[1]))

    print(*sol(arr, queries, M), sep='\n')


main()
