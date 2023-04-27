import sys

input = sys.stdin.readline

n = int(input())

nums = [idx for idx in range(1, n + 1)]

print(sum(nums))