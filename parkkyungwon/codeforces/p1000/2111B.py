import sys



def fibonacci(exp):
    if exp == 1: return 1, 1, 0

    a, b, c = fibonacci(exp >> 1)
    b_sq = b ** 2
    a, b, c = a**2 + b_sq, b * (a + c), b_sq + c**2

    if exp & 1: a, b, c = a + b, a, b

    return a, b, c
    

def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    t = int(readline())
    for _ in range(t):
        cubes, boxes = map(int, readline().split())

        fib = fibonacci(cubes)
        fib_np1 = fib[0] + fib[1]
        fib_n = fib[0]

        answer = ''

        for _ in range(boxes):
            w, l, h = map(int, readline().split())

            if h >= fib_np1:
                answer += '0' if w < fib_n or l < fib_n else '1'
            
            elif h >= fib_n:
                ge, le = (w, l) if w > l else (l, w)
                answer += '0' if ge < fib_np1 or le < fib_n else '1'
            
            else:
                answer += '0'
        
        write(answer + '\n')


main()
