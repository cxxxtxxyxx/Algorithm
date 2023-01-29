import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 2)
days = [0]
values = [0]

for __ in range(n):
    day, value = list(map(int, input().strip().split()))
    days.append(day)
    values.append(value)

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    
    if i + days[i] <= n + 1:
        dp[i + days[i]] = max(dp[i + days[i]], dp[i] + values[i])

print(max(dp))