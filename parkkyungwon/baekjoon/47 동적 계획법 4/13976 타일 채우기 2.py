def dq(ex):
    if ex == 1: 
        return MAT
    
    mat = dq(ex >> 1)
    mat_T = [[*a] for a in zip(*mat)]
    # 행렬 제곱
    mat = [[(a[0] * b[0] + a[1] * b[1]) % MOD for b in mat_T] for a in mat]
    
    # 홀수일 때
    if ex & 1:
        mat = [[(a[0] * b[0] + a[1] * b[1]) % MOD for b in MAT_T] for a in mat]
    
    return mat


def sol(n):
    if n & 1: return 0
    if n == 2: return 3

    mat = dq((n >> 1) - 1)[0]
        
    return (3*mat[0] + mat[1]) % MOD


MOD = int(1e9) + 7
N = int(input())
MAT = [[4, -1],
       [1, 0]]

MAT_T = [[4, 1],
         [-1, 0]]

print(sol(N))
