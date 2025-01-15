def manacher(string):
    string = '^#' + '#'.join(string) + '#$'
    leng = len(string)
    max_p = [0] * leng
    center = 0
    end = 0
    total = 0

    for i in range(1, leng - 1):
        j = (center << 1) - i

        if i < end: max_p[i] = min(end - i, max_p[j])

        while string[i + max_p[i] + 1] == string[i - max_p[i] - 1]: max_p[i] += 1

        if (new_end := i + max_p[i]) > end:
            center = i
            end = new_end
    
        if max_p[i]:
            total += max_p[i] >> 1
            if max_p[i] & 1: total += 1

    return total


def main():
    S = input()
    
    print(manacher(S))


main()
