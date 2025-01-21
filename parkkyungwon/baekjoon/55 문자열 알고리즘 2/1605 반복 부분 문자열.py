import itertools



def build_sa(string):
    leng = len(string)
    sa = list(range(leng))
    rank = [ord(s) for s in string]
    k = count = 1

    while k < leng and count != leng:
        keys = [(rank[i] << 18) + (rank[j] if (j := i + k) < leng else 0) for i in range(leng)]
        sa.sort(key=lambda x: keys[x])

        new_rank = [1] * leng
        count = 1

        for prev, curr in itertools.pairwise(sa):
            if keys[curr] != keys[prev]: count += 1
            new_rank[curr] = count
        
        rank = new_rank
        k <<= 1
    
    return sa


def get_lcp(sa, string):
    leng = len(sa)
    inv = [None] * leng
    for i, v in enumerate(sa): inv[v] = i
    h = 0
    amax = 0

    for i in range(leng):
        curr = inv[i]
        if not curr: continue

        j = sa[curr - 1]
        while (a := i + h) < leng and (b := j + h) < leng and string[a] == string[b]: h += 1

        if amax < h: amax = h
        if h: h -= 1
    
    return amax


def main():
    input()
    string = input()
    sa = build_sa(string)
    max_lcp = get_lcp(sa, string)

    print(max_lcp)


main()
