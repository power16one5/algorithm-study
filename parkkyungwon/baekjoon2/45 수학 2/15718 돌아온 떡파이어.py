import sys



def get_fac_inv(mod):
    length = mod + 1

    fac = [1] * length
    inv_seq = [1] * length
    inv_fac = [1] * length

    for i in range(2, length):
        fac[i] = fac[i - 1] * i % mod
        q, r = divmod(mod, i)
        inv_seq[i] = (-q * inv_seq[r]) % mod

    for i in range(2, length):
        inv_fac[i] = inv_seq[fac[i]]

    return fac, inv_fac


def lucas_theorem(n, k, fac, inv, mod):
    answer = 1

    while n or k:
        nom_q, nom_r = divmod(n, mod)
        denom_q, denom_r = divmod(k, mod)

        if nom_r < denom_r:
            answer = 0
            break

        answer = answer * fac[nom_r] % mod * inv[denom_r] % mod * inv[nom_r - denom_r] % mod

        n, k = nom_q, denom_q
    
    return answer


def chinese_remain(r1, mod1, r2, mod2):
    q = (r2 - r1) * pow(mod1, -1, mod2)
    return (q * mod1 + r1) % (mod1 * mod2)


def main():
    write = sys.stdout.write

    MOD1, MOD2 = 97, 1031
    data = list(map(int, sys.stdin.read().split()))

    fac1, inv1 = get_fac_inv(MOD1)
    fac2, inv2 = get_fac_inv(MOD2)

    for i in range(1, len(data), 2):
        N, K = data[i] - 1, data[i + 1] - 2

        if N == -1 and K == -1:
            answer = 1

        elif N < 0 or N < K or K < 0:
            answer = 0
        
        else:
            r1 = lucas_theorem(N, K, fac1, inv1, MOD1)
            r2 = lucas_theorem(N, K, fac2, inv2, MOD2)

            answer = chinese_remain(r1, MOD1, r2, MOD2)
        
        write(f"{answer}\n")


main()
