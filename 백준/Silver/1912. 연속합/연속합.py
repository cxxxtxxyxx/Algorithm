import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [nums[0]] + [0] * (n - 1)

for i in range(1, n):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])

print(max(dp))