import math



def main():
    N, K, M = map(int, input().split())
    
    total = 1
    digit = M ** int(math.log(N, M))
    
    fac = [1] * M
    fac_inv = [1] * M
    for i in range(1, M):
        fac[i] = (fac[i - 1] * i) % M
        fac_inv[i] = pow(fac[i], -1, M)

    while digit:
        q1 = N // digit
        q2 = K // digit

        if q1 < q2: 
            total = 0
            break

        numer = fac[q1]
        denom1 = fac_inv[q2]
        denom2 = fac_inv[q1 - q2]

        total = (total * numer * denom1 * denom2) % M
        N -= q1 * digit
        K -= q2 * digit
        digit //= M
    
    print(total)


main()
