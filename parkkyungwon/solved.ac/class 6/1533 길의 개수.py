def sol(n):
    if n == 1: return MAT

    A = sol(n >> 1)
    A = [[sum(c * d for c, d in zip(a, b)) % MOD for b in zip(*A)] for a in A]

    if n & 1:
        A = [[sum(c * d for c, d in zip(a, b)) % MOD for b in MAT_T] for a in A]
    
    return A


def main():
    global MAT, MAT_T
    N, S, E, T = map(int, input().split())

    leng = 5 * N
    MAT = [[0] * leng for _ in range(leng)]
    for i in range(0, leng, 5):
        for j in range(i, i + 4):
            MAT[j][j + 1] = 1

    for i in range(N):
        adj = i * 5

        for j, k in enumerate(map(int, input())):
            if not k: continue

            MAT[5*j + (k - 1)][adj] = 1

    MAT_T = tuple(a for a in zip(*MAT))

    print(sol(T)[5 * (E - 1)][5 * (S - 1)])


MOD = int(1e6) + 3

main()
