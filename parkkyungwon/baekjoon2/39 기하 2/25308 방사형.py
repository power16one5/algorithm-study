def make_dp(nums):
    dp = bytearray(512)
    ccw = (dig[b] - nums[a]) * (nums[c] - dig[b]) + dig[b] ** 2


def main():
    nums = list(map(int, input().split()))
    dig = [n * 2 ** (0.5) / 2 for n in nums]

    