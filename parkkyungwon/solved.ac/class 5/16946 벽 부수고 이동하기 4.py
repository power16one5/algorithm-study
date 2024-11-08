from sys import stdin, stdout



def sol(arr):
    leng = len(arr)
    arr_copy = arr.copy()
    space_count_dp = [None] * 3

    def fill_count_bfs(start, dp_i):
        queue = [start]
        arr_copy[start] = dp_i

        for q in queue:
            for j in q+1, q-1, q+L, q-L:
                if arr_copy[j]: continue

                arr_copy[j] = dp_i
                queue.append(j)

        return queue

    for i in range(leng):
        if arr_copy[i]: continue

        dp_i = len(space_count_dp)
        queue = fill_count_bfs(i, dp_i)

        space_count_dp.append(len(queue) % 10)
    
    for i in range(leng):
        if arr[i] != 1: continue

        idxs = []

        for j in i+1, i-1, i+L, i-L:
            if arr_copy[j] < 3 or arr_copy[j] in idxs: continue

            idxs.append(arr_copy[j])
        
        count = 1
        for j in idxs: count += space_count_dp[j]

        arr[i] = count % 10


N, M = map(int, stdin.readline().split())
L = M + 2

arr = [2] * L
for line in stdin.read().splitlines():
    arr += [2] + list(map(int, line)) + [2]
arr += [2] * L

sol(arr)

i = L + 1
for _ in range(N):
    stdout.write(''.join(map(str, arr[i:i+M])) + '\n')
    i += L
