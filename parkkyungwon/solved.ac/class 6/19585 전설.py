import sys



def sol(color_tri, name_set, string):
    dp = color_tri

    for i, char in enumerate(string):
        if None in dp and string[i:] in name_set:
            return True

        if char not in dp:
            break
        
        dp = dp[char]
    
    return False


def main():
    readline = sys.stdin.readline
    write = sys.stdout.write

    C, N = map(int, readline().split())

    color_tri = {}

    for _ in range(C):
        dp = color_tri

        for char in readline().rstrip():
            if char not in dp:
                dp[char] = {}
            
            dp = dp[char]
        
        dp[None] = None
    
    name_set = frozenset(readline().rstrip() for _ in range(N))

    Q = int(readline())

    data = [readline().rstrip() for _ in range(Q)]

    write('\n'.join('Yes' if sol(color_tri, name_set, string) else 'No' for string in data) + '\n')


main()
