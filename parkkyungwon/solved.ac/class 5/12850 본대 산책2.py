def mm(a, b):
    return [[sum(aa * ba for aa, ba in zip(av, bv)) % MOD for bv in b] for av in a]


def sep(i):
    if i == 1: return mat

    arr = sep(i // 2)
    arr_T = tuple(a for a in zip(*arr))
    ret = mm(arr, arr_T)

    if i % 2: ret = mm(ret, mat_T)

    return ret


D = int(input())
MOD = int(1e9 + 7)

mat = ((0, 1, 1, 0, 0, 0, 0, 0),
       (1, 0, 1, 1, 0, 0, 0, 0),
       (1, 1, 0, 1, 1, 0, 0, 0),
       (0, 1, 1, 0, 1, 1, 0, 0),
       (0, 0, 1, 1, 0, 1, 1, 0),
       (0, 0, 0, 1, 1, 0, 0, 1),
       (0, 0, 0, 0, 1, 0, 0, 1),
       (0, 0, 0, 0, 0, 1, 1, 0))

mat_T = tuple(a for a in zip(*mat))

print(sep(D)[0][0])
