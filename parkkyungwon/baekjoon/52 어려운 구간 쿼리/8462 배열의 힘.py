import sys



def mo(arr, queries):
    def z_order(x, y):
        # 1) x를 짝수 비트 위치로 분산시키기
        x &= 0xFFFFFFFF  # 혹시 모를 상위 비트 정리
        x = (x | (x << 16)) & 0x0000FFFF0000FFFF
        x = (x | (x << 8))  & 0x00FF00FF00FF00FF
        x = (x | (x << 4))  & 0x0F0F0F0F0F0F0F0F
        x = (x | (x << 2))  & 0x3333333333333333
        x = (x | (x << 1))  & 0x5555555555555555

        # 2) y를 홀수 비트 위치로 분산시키기
        y &= 0xFFFFFFFF
        y = (y | (y << 16)) & 0x0000FFFF0000FFFF
        y = (y | (y << 8))  & 0x00FF00FF00FF00FF
        y = (y | (y << 4))  & 0x0F0F0F0F0F0F0F0F
        y = (y | (y << 2))  & 0x3333333333333333
        y = (y | (y << 1))  & 0x5555555555555555

        # 3) x의 비는 짝수, y의 비는 홀수 위치에 interleave
        z = x | (y << 1)
        return z

    queries.sort(key=lambda x: z_order(x[0], x[1]))
    answer = [0] * len(queries)
    leng = int(1e6) + 1
    freq = [0] * leng
    total = 0
    R, L = 0, 0

    for l, r, i in queries:
        while R < r:
            a = arr[R]
            total += (2*freq[a] + 1) * a
            freq[a] += 1
            R += 1

        while R > r:
            R -= 1
            a = arr[R]
            total += (-2*freq[a] + 1) * a
            freq[a] -= 1

        while L < l:
            a = arr[L]
            total += (-2*freq[a] + 1) * a
            freq[a] -= 1
            L += 1

        while L > l:
            L -= 1
            a = arr[L]
            total += (2*freq[a] + 1) * a
            freq[a] += 1

        answer[i] = total 
    
    return answer


def main():
    readline = sys.stdin.readline

    _, T = map(int, readline().split())
    arr = tuple(map(int, readline().split()))
    queries = [(l - 1, r, i) for i, (l, r) in enumerate(map(int, readline().split()) for _ in range(T))]

    print(*mo(arr, queries), sep='\n')


main()
