def main():
    data = map(int, open(0).read().split())
    n = next(data)
    n1 = n + 1
    mat = [[next(data) for _ in range(n + 1)] for _ in range(n)]

    for i in range(n):
        mul = 1 / mat[i][i]
        for j in range(i, n1):
            mat[i][j] *= mul

        for j in range(n):
            if i == j: continue

            mul = mat[j][i] / mat[i][i]
            for k in range(i, n1):
                mat[j][k] -= mul * mat[i][k]
    
    answer = [None] * n
    for i in range(n - 1, -1, -1):
        answer[i] = mat[i][n]

        for j in range(i - 1, -1, -1):
            mat[j][n] -= mat[j][i] * answer[i]
    
    print(*map(round, answer))


main()
