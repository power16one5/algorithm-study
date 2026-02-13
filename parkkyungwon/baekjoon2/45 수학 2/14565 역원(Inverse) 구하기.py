def ex_euclide(a, b):
    ori_b = b
    ca1, ca2 = 1, 0

    while b:
        a, b, ca1, ca2 = b, a % b, ca2, ca1 - (a // b) * ca2
    
    return a, ca1 % ori_b


def main():
    n, a = map(int, input().split())
    
    add_inv = n - a
    gcd, a_inv = ex_euclide(a, n)

    if gcd != 1: a_inv = -1

    print(add_inv, a_inv)

main()
