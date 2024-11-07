import sys



def sol(a, b, c, d):
    total = 0
    
    ab = [ai + bi for ai in a for bi in b]
    ab.sort()
    cd = [ci + di for ci in c for di in d]
    cd.sort()

    abp, cdp, ab_leng = 0, len(cd)-1, len(ab)
    total = 0

    while abp < ab_leng and cdp > -1:
        v = ab[abp] + cd[cdp]

        if not v: 
            next_abp = abp + 1
            next_cdp = cdp - 1

            while next_abp < ab_leng and ab[abp] == ab[next_abp]: next_abp += 1
            while next_cdp > -1 and cd[cdp] == cd[next_cdp]: next_cdp -= 1

            total += (next_abp - abp) * (cdp - next_cdp)
            abp = next_abp
            cdp = next_cdp

        elif v < 0: abp += 1
        else: cdp -= 1

    return total


readline = sys.stdin.readline
N = int(readline())
a, b, c, d = (arr for arr in zip(*(map(int, readline().split()) for _ in range(N))))

print(sol(a, b, c, d))
