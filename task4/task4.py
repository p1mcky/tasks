import sys


def min_moves(file_name):
    with open(file_name) as f:
        nums = sorted(map(int, f))
    return sum(abs(x - nums[len(nums) // 2]) for x in nums)


print(min_moves(sys.argv[1]))