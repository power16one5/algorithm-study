import sys



def main():
    readline = sys.stdin.readline
    write = sys.stdout.write
    flush = sys.stdout.flush
    s, e = 1, int(readline())

    for _ in range(50):
        m = (s + e) >> 1

        write(f"? {m}\n"); flush()
        match int(readline()):
            case 1:
                e = m - 1
            case -1:
                s = m + 1
            case _:
                answer = m
                break
    
    else:
        answer = s
    
    write(f"= {answer}\n"); flush()


main()
