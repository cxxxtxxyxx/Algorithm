import sys

input = sys.stdin.readline

n = int(input().strip())
nums = [int(input().strip()) for __ in range(n)]
nums.sort()

for num in nums:
    print(num)