from sys import stdin



def sol(arr):
    mini = 11

    def move(ri, bi, delta):
        dri, dbi = ri + delta, bi + delta
        while arr[dri] == 46: dri += delta
        while arr[dbi] == 46: dbi += delta

        if arr[dri] == 79 or arr[dbi] == 79: return dri, dbi

        dri -= delta ; dbi -= delta

        if dri == dbi:
            if delta > 0: 
                if ri > bi: dbi -= delta
                else: dri -= delta

            else: 
                if ri > bi: dri -= delta
                else: dbi -= delta
        
        return dri, dbi

    def backtrack(depth, ri, bi, is_prev_x_axis):
        nonlocal mini

        if depth >= mini: return

        for delta in ((M, -M) if is_prev_x_axis else (1, -1)):
            dri, dbi = move(ri, bi, delta)
            
            if dri == ri and dbi == bi: continue

            if arr[dbi] == 79: continue

            if arr[dri] == 79: 
                if mini > depth: mini = depth
                continue
            
            backtrack(depth + 1, dri, dbi, not is_prev_x_axis)
    
    ri = arr.index(82); bi = arr.index(66)
    arr[ri] = 46; arr[bi] = 46

    backtrack(1, ri, bi, True)
    backtrack(1, ri, bi, False)

    return -1 if mini == 11 else mini


N, M = map(int, stdin.readline().split())
arr = list(map(ord, stdin.read().replace('\n', '')))

print(sol(arr))
