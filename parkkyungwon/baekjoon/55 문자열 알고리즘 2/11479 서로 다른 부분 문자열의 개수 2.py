import itertools



def build_sa(string):
    leng = len(string)
    sa = list(range(leng))
    rank = [ord(s) for s in string]
    k = count = 1

    while k < leng and count != leng:
        keys = [(rank[i] << 20) + (rank[j] if (j := i + k) < leng else 0) for i in range(leng)]
        sa.sort(key=lambda x: keys[x])

        new_rank = [1] * leng
        count = 1

        for prev, curr in itertools.pairwise(sa):
            if keys[curr] != keys[prev]: count += 1
            new_rank[curr] = count
        
        rank = new_rank
        k <<= 1
    
    return sa


def get_lcp_count(sa, string):
    leng = len(sa)
    inv = [None] * leng
    for i, v in enumerate(sa): inv[v] = i
    h = 0
    count = 0

    for i in range(leng):
        curr = inv[i]
        if not curr: continue

        j = sa[curr - 1]
        while (a := i + h) < leng and (b := j + h) < leng and string[a] == string[b]: h += 1

        if h: count += h; h -= 1 
    
    return count


def main():
    string = input()
    sa = build_sa(string)
    count = get_lcp_count(sa, string)

    n = len(string)
    print(((n * (n + 1)) >> 1) - count)


main()
