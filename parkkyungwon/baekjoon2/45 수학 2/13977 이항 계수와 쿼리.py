import sys



def get_facts(sets, mod):
    sets.discard(0)
    cum = 1
    i = 1
    
    j_it = iter(sorted(sets))
    j = next(j_it)
    if not j: j = next(j_it)

    fact= {0: 1}
    inv = {0: 1}

    while True:
        cum = (cum * i) % mod

        if i == j:
            fact[i] = cum
            inv[i] = pow(cum, -1, mod)

            try:
                j = next(j_it)
            except StopIteration:
                break
        
        i += 1
    
    return fact, inv


def main():
    write = sys.stdout.write

    MOD = 1000000007
    data = list(map(int, sys.stdin.read().split()))
    M = data[0]

    sets = set()
    for i in range(1, len(data), 2):
        N, K = data[i], data[i + 1]
        sets.update((N, K, N - K))

    fact, inv = get_facts(sets, MOD)

    for i in range(1, len(data), 2):
        N, K = data[i], data[i + 1]

        if K:
            answer = (fact[N] * inv[K] % MOD) * inv[N - K] % MOD
    
        else:
            answer = 1
        
        write(f"{answer}\n")


main()
