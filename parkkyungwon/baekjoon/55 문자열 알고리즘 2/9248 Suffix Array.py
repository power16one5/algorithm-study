def build_sa(string):
    leng = len(string)
    rank = [ord(c) for c in string]
    sa = list(range(leng))
    k = 1

    while k < leng:
        keys = [(rank[i] << 19) + (rank[j] if (j := i + k) < leng else 0) for i in range(leng)]
        sa.sort(key=lambda i: keys[i])
        
        next_rank = [1] * leng
        it = iter(sa)
        prev = next(it)

        for curr in it:
            next_rank[curr] = next_rank[prev] + (keys[curr] != keys[prev])
            prev = curr
        
        if next_rank[sa[-1]] == leng: break

        rank = next_rank
        k <<= 1
    
    return sa


def build_lcp(string, sa):
    leng = len(sa)

    inv_sa = [0] * leng
    for i in range(leng):
        inv_sa[sa[i]] = i

    lcp = [0] * leng
    lcp[0] = 'x'
    h = 0

    for i in range(leng):
        if not inv_sa[i]: continue

        j = sa[inv_sa[i] - 1]
        while (a := i + h) < leng and (b := j + h) < leng and string[a] == string[b]:
            h += 1

        lcp[inv_sa[i]] = h

        if h: h -= 1

    return lcp


def main():
    string = input()
    sa = build_sa(string)
    lcp = build_lcp(string, sa)

    print(*map(lambda x: x + 1, sa))
    print(*lcp)


main()
