import math



def sol(n):
    digit_count = [0] * 10
    leng = int(math.log10(n))
    digit = 10 ** leng

    while digit:
        end = n // digit
        count = end * int(10 ** (leng - 1)) * leng

        for i in range(10):
            digit_count[i] += count

        for i in range(end):
            digit_count[i] += digit

        n -= end * digit
        digit_count[end] += n + 1

        leng -= 1
        digit_count[0] -= digit
        digit //= 10

    return digit_count


N = int(input())

print(' '.join(map(str, sol(N))))
