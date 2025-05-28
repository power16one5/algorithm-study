def main():
    N = int(input())
    
    i = N
    A, B = [], []
    for _ in range(N // 3):
        A.append(i)
        B.append(i - 1)
        B.append(i - 2)
        i -= 3
        
    if (N % 3) == 2:
        A.append(2)
        B.append(1)

    print(len(A))
    print(*A)
    print(len(B))
    print(*B)


main()
