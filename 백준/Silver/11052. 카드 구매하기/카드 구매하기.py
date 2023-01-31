import sys

input = sys.stdin.readline

n = int(input())

card = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

dp[1] = card[1]

for i in range(2, n + 1):
    for j in range(i + 1):
        dp[i] = max(dp[i - j] + card[j], card[i], dp[i])

print(dp[n])
