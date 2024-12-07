def sol():
    fac = [1] * 53
    inv = [1] * 53
    for i in range(1, 53):
        fac[i] = (fac[i-1] * i) % MOD
        inv[i] = pow(fac[i], -1, MOD)

    sign = 1
    total = 0
    for i in range(1, (N >> 2) + 1):
        cases = 1
        rest_card = 52 - 4*i
        rest_draw = N - 4*i

        for a in fac[13], inv[i], inv[13 - i], fac[rest_card], inv[rest_draw], inv[rest_card - rest_draw]:
            cases = (cases * a) % MOD
        
        total = (total + sign * cases) % MOD
        sign = -sign

    return total


MOD = 10007
N = int(input())

print(sol())
