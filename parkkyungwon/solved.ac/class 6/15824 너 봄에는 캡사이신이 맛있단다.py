# i 길이를 가진 조합들의 min, max 차이
def diff_min_max(arr):
    diff = [0] * N 
    s, e = 0, N - 1
    
    while s < e:
        diff[s + 1] = diff[e] = (arr[e] - arr[s] + diff[s]) % MOD
        s += 1; e -= 1

    return diff


def sol(arr):
    diff = diff_min_max(arr)
    two_power = 1
    total = 0

    for i in range(1, N):
        total = (total + (two_power * diff[i]) % MOD) % MOD
        two_power = (two_power << 1) % MOD

    return total


MOD = int(1e9) + 7

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(sol(arr))
