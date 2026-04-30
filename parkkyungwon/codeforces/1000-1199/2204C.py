from itertools import combinations
from math import lcm



def main():
    t = int(input())

    for _ in range(t):
        data = list(map(int, input().split()))
        days = data[:3]
        m = data[-1]
        water = [0] * 3

        for i in range(3):
            water[i] += 6 * (m // days[i])
            
        for a, b in combinations(range(3), 2):
            v = 3 * (m // lcm(days[a], days[b]))
            water[a] -= v; water[b] -= v
        
        v = 2 * (m // lcm(*days))
        for i in range(3):
            water[i] += v
    
        print(*water)


main()
