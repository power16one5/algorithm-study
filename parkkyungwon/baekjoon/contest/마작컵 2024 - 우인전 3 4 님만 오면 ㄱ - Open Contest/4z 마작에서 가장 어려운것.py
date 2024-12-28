def sol(a, b, c):
    an, bn = a // 3, b // 4

    if r := a % 3: 
        an += 1
        c -= 3 - r

    if r := b % 4:
        bn += 1
        c -= 4 - r
    
    if r < 0: return -1

    start = (c // 4) * 4
    for i in range(start, -1, -4):
        if not ((c - i) % 3):
            break
    
    else: return -1

    an += (c - i) // 3
    bn += i // 4

    return an, bn


def main():
    a, b, c = map(int, input().split())

    answer = sol(a, b, c)

    if answer == -1: print(-1)
    else: print(*answer)


main()
