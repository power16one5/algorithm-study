import sys



def mo(arr, queries):
    leng = int(1e5) + 1
    freq = [0] * leng
    freq_freq = [0] * leng
    freq_freq[0] = float('inf')
    max_head = 0

    def z_order(a, b):
        z = 0
        for i in range(18, -1, -1):
            z = (z << 1) | ((a >> i) & 1)
            z = (z << 1) | ((b >> i) & 1)
        return z

    queries.sort(key=lambda x: z_order(x[0], x[1]))
    answer = [0] * len(queries)
    R, L = 0, 0

    def add(a):
        nonlocal max_head

        freq_freq[freq[a]] -= 1
        freq[a] += 1
        freq_freq[freq[a]] += 1

        if freq_freq[max_head + 1]: max_head += 1

    def sub(a):
        nonlocal max_head

        freq_freq[freq[a]] -= 1
        freq[a] -= 1
        freq_freq[freq[a]] += 1

        if not freq_freq[max_head]: max_head -= 1

    for l, r, i in queries:
        while R < r: add(arr[R]); R += 1
        while R > r: R -= 1; sub(arr[R]); 
        while L < l: sub(arr[L]); L += 1
        while L > l: L -= 1; add(arr[L]); 

        answer[i] = max_head
    
    return answer


def main():
    readline = sys.stdin.readline

    N = int(readline())
    arr = tuple(map(int, readline().split()))
    M = int(readline())
    queries = [(l - 1, r, i) for i, (l, r) in enumerate(map(int, readline().split()) for _ in range(M))]

    print(*mo(arr, queries), sep='\n')


main()
