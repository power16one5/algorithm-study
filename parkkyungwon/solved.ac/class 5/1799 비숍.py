from sys import stdin



def sol(arr):
    leng = 2*N - 1
    diagnal = [[] for _ in range(leng)]
    diagnal_col_visited = [False] * leng

    for i in range(N):
        for j in range(N):
            if arr[i][j]: diagnal[i + j].append(i - j)
        
    def backtrack(i):
        maxi = 0

        def f(i, count):
            nonlocal maxi

            if i >= leng:
                if maxi < count: maxi = count
                return

            for j in diagnal[i]:
                if diagnal_col_visited[j]: continue

                diagnal_col_visited[j] = True
                f(i + 2, count + 1)
                diagnal_col_visited[j] = False
            
            f(i + 2, count)
        
        f(i, 0)

        return maxi
            
    return backtrack(0) + backtrack(1)


N = int(stdin.readline())

arr = [tuple(map(lambda x: x == '1', a.split())) for a in stdin.read().splitlines()]

print(sol(arr))
