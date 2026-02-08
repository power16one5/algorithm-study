def main():
    N = int(input())
    
    print("? 1", flush=True)
    a = int(input())

    print(f"? {N}", flush=True)
    b = int(input())

    if a == b:
        print("! 0", flush=True)
    elif a:
        print("! -1", flush=True)
    else:
        print("! 1", flush=True)


main()
