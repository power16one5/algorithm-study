def main():
    length = int(input())
    nums = list(map(int, input().split()))
    bit = 1 << (max(nums).bit_length() - 1)

    for i in range(length):
        for j in range(i + 1, length):
            if bit & nums[j]:
                nums[j] ^= nums[i]


main()
