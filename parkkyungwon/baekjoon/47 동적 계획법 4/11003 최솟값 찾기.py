from collections import deque



def sol(arr):
    arr = [INF] * L + arr
    min_dq = deque([INF])

    leng = len(arr)
    answer = []

    for s, e in zip(range(0, leng-L), range(L, leng)):
        if arr[s] == min_dq[0]:
            min_dq.popleft()
        
        while min_dq and min_dq[-1] > arr[e]:
            min_dq.pop()
        
        min_dq.append(arr[e])
        answer.append(min_dq[0])
    
    return answer


INF = float('inf')

N, L = map(int, input().split())
arr = list(map(int, input().split()))

print(*sol(arr))
