def encode(n):
    string = ['a'] * 13
    i = 12

    while n:
        n, r = divmod(n, 26)
        string[i] = chr(r + 97)
        i -= 1
    
    return str(''.join(string))


def decode(string):
    n = 0
    
    for i in range(12):
        n += ord(string[i]) - 97
        n *= 26
    
    n += ord(string[-1]) - 97

    return n


def main():
    if input() == '1':
        n = sum(map(int, input().split()))
        print(encode(n))
    
    else:
        string = input()
        print(decode(string))


main()
