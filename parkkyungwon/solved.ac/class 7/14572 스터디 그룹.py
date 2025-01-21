import sys



def sol(data, N, K, D):
    s, e = 0, 0
    al_dp = [0] * K
    amax = 0
    count = 0
    degrees, num_als = [], []

    data.sort(key=lambda x: x[0])
    for degree, num_al in data:
        degrees.append(degree)
        num_als.append(num_al)

    while e < N:
        s_degree = degrees[e] - D

        while degrees[s] < s_degree:
            for a in num_als[s]: 
                al_dp[a] -= 1
                if not al_dp[a]: count -= 1
            s += 1
        
        leng = e - s + 1
        adj = 0

        for a in num_als[e]: 
            if not al_dp[a]: count += 1
            al_dp[a] += 1 
            if al_dp[a] == leng: adj += 1
        
        if amax < (v := (count - adj) * leng): amax = v
        e += 1
    
    return amax


def main():
    readline = sys.stdin.readline

    N, K, D = map(int, readline().split())
    data = [[0, []] for _ in range(N)]

    for i in range(N):
        data[i][0] = int(readline().split()[1])
        data[i][1].extend(map(lambda x: int(x) - 1, readline().split()))

    sys.stdout.write(str(sol(data, N, K, D)) + '\n')


main()
