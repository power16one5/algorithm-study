def gen(n):
    half = n >> 1
    
    for i in range(half, 0, -1):
        yield i; yield i + half
    
    if n & 1: yield n
    

def main():
    N = int(input())

    print(*gen(N))


main()
