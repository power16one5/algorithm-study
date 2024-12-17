import sys



def mm(A, B):
    return [[sum(ai * bi for ai, bi in zip(a, b)) % MOD for b in B] for a in A]


def mpow(n):
    if n == 1: return MAT

    A = mpow(n >> 1)
    A = mm(A, [a for a in zip(*A)])

    if n & 1: A = mm(A, MAT_T)

    return A
    

def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    T, N, D = map(int, readline().split())
    matrices = [tuple([0] * N for _ in range(N)) for _ in range(T)]

    for matrix in matrices:
        M = int(readline())

        for _ in range(M):
            a, b, c = map(int, readline().split())
            # 행렬곱을 쉽게 하기위해 전치해서 저장
            matrix[b - 1][a - 1] = c
    
    cum_mat = tuple([0] * N for _ in range(N))
    for i in range(N):
        cum_mat[i][i] = 1

    for matrix in matrices: 
        cum_mat = mm(cum_mat, matrix)

    global MAT, MAT_T
    MAT = cum_mat
    MAT_T = tuple(a for a in zip(*cum_mat))

    q, r = divmod(D, T)

    if q: 
        A = mpow(q)

    else:
        A = tuple([0] * N for _ in range(N))
        for i in range(N): 
            A[i][i] = 1

    for matrix, _ in zip(matrices, range(r)):
        A = mm(A, matrix)
    
    for a in A:
        write(' '.join(map(str, a)) + '\n')
    

MOD = int(1e9) + 7

main()
