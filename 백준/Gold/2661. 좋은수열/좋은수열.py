import sys

input = sys.stdin.readline

N = int(input())


def backtracking(nums):

    for i in range(1, len(nums) // 2 + 1):
        if nums[-i:] == nums[-2*i:-i]:
            return

    if len(nums) == N:
        print(nums)
        exit(0)

    for i in ('1', '2', '3'):
        nums += i
        backtracking(nums)
        nums = nums[:-1]

backtracking("")