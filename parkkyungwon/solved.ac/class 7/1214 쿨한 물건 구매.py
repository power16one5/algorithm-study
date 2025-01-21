import math



def main():
    D, P, Q = map(int, input().split())
    most = float('inf')
    lcm = math.lcm(P, Q)
    target = D 
    if target > (lcm << 1):
        target %= lcm
        target += lcm

    if P < Q: P, Q = Q, P

    while target > 0:
        if not target % Q: 
            most = 0
            break

        a = (target // Q + 1) * Q
        diff = a - target

        if most > diff: most = diff

        target -= P

    if target <= 0 and most > -target: most = -target

    print(D + most)


main()
