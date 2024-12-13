import sys



def sol(data):
    fac = [1] * LENG

    for i in range(1, LENG):
        fac[i] = (fac[i-1] * i) % MOD

    for n, k in data:
        answer = fac[n]
        answer = (answer * pow(fac[k], -1, MOD)) % MOD
        answer = (answer * pow(fac[n-k], -1, MOD)) % MOD

        yield answer
    

readline = sys.stdin.readline
write = sys.stdout.write
LENG = int(4e6) + 1
MOD = int(1e9) + 7

M = int(readline())
data = (map(int, readline().split()) for _ in range(M))

for a in sol(data):
    write(str(a) + '\n')
