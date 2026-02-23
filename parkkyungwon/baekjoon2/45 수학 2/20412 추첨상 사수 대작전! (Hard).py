def main():
    m, Seed, X1, X2 = map(int, input().split())
    
    if Seed == X1:
        a, c = 1, 0
    
    else:
        inv_sx1 = pow(Seed - X1, -1, m)
        a = ((X1 - X2) * inv_sx1) % m
        c = (X2 - a * X1) % m

    print(a, c, flush=True)


main()
