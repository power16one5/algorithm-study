def sol(n):
    leng = int(n ** (0.5)) + 2
    total = 1
    i = 2

    while i < leng and i <= n:
        if not (n % i):
            count = 0

            while not (n % i):
                n //= i
                count += 1

            total *= (i ** count) - (i ** (count - 1))
        
        i += 1
    
    if n != 1: total *= n - 1
    
    return total


N = int(input())

print(sol(N))
