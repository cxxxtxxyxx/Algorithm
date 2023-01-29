import sys
import itertools
input = sys.stdin.readline

t = int(input())

for __ in range(t):
    n = int(input())
    nums = [list(map(int, input().split())) for __ in range(2)]

    dp = [[0] * n for __ in range(2)]

    if n == 1:
        print(max(nums[0][0], nums[1][0]))
        continue
    
    if n == 2:
        print(max(nums[0][1] + nums[1][0], nums[1][1] + nums[0][0]))
        continue

    dp[0][0] = nums[0][0]
    dp[1][0] = nums[1][0]
    dp[0][1] = nums[0][1] + nums[1][0]
    dp[1][1] = nums[1][1] + nums[0][0]

    for i in range(2, n):
        for j in range(2):
            
            if j == 0:
                dp[j][i] = max(dp[j + 1][i - 1] + nums[j][i], max(dp[j][i - 2], dp[j + 1][i - 2]) + nums[j][i])
            else:
                dp[j][i] = max(dp[j - 1][i - 1] + nums[j][i], max(dp[j][i - 2], dp[j - 1][i - 2]) + nums[j][i])
    print(max(list(itertools.chain(*dp))))
