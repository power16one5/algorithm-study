def interval_max(arr):
    cum_sum = [0] + arr
    for i in range(1, len(cum_sum)):
        cum_sum[i] += cum_sum[i - 1]
    
    amax = -INF
    s, e = INF, -INF

    for a in cum_sum:
        if s > a: s = e = a
        elif e < a: e = a
        else: continue

        if amax < (v := e - s): amax = v
    
    return amax if amax else max(arr)


def top_down(arr):
    queue1 = [arr]
    queue2 = []

    sep = len(arr)
    for _ in range(len(arr).bit_length()):
        yield [b for a in queue1 for b in a]
        sep >>= 1

        for a in queue1:
            queue2.append(a[:sep])
            queue2.append(a[sep + 1:])
        queue1, queue2 = queue2, []
        

def bottom_up(arr):
    for _ in range(len(arr).bit_length()):
        yield arr
        arr = [arr[i] for i in range(1, len(arr), 2)]


def dfs(arr):
    arr, ret = [0] + arr, []
    leng = len(arr)

    def f(i):
        j = i << 1

        if j < leng: 
            f(j)
            ret.append(arr[i])
            f(j + 1)
        
        else:
            ret.append(arr[i])
    
    f(1)

    return ret


def main():
    input()
    arr = dfs(list(map(int, input().split())))

    amax = -INF
    for a in bottom_up(arr):
        for b in top_down(a):
            v = interval_max(b)
            if amax < v: amax = v
    
    print(amax)


INF = float('inf')
main()
