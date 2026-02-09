import sys



def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    flush = sys.stdout.flush

    M, N, Q = map(int, readline().split())
    num_att = list(map(int, readline().split()))
    answer = [1] * N

    for a in range(min(M, N)):
        avail = {i for i in range(1, num_att[a] + 1)}
        a1 = a + 1

        for b in range(a1, M + 1, N):
            write(f"? {b} {a1}\n")
            flush()

            avail.discard(int(readline()))
        
        answer[a] = avail.pop()
    
    write("! " + " ".join(map(str, answer)) + "\n")
    flush()


main()
