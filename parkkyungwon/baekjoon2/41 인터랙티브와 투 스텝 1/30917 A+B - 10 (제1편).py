def main():
    total = 0

    for char in "A", "B":
        for i in range(1, 10):
            print("?", char, i, flush=True)
            if input() == '1':
                total += i
                break
    
    print("!", total)

main()
