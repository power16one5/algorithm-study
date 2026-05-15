import sys



def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    while True:
        prev = readline().strip()
        if prev == '#': break

        length = len(prev)
        flag = True

        while True:
            curr = readline().strip()
            if curr == '#': break
            if len(curr) != length: 
                flag = False
                break

            count = 0
            for c1, c2 in zip(prev, curr):
                if c1 != c2: 
                    count += 1
                    if count > 1: break
            
            if count != 1:
                flag = False
                break
                
            prev = curr
        
        while curr != '#':
            curr = readline().strip()

        write('Correct\n' if flag else 'Incorrect\n')


main()
