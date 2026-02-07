from itertools import chain



def main():
    total = 0
    num = 2322

    for char in "A", "B":
        for i in chain(range(1, num), range(num + 2, 10001)):
            print("?", char, i, flush=True)
            if int(input()):
                total += i
                break
        else:
            total += num
    
    print("!", total, flush=True)

main()
