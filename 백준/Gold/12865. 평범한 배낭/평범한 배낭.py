import sys

input = sys.stdin.readline

n, k = map(int, input().split())

w = [0]
v = [0]
for __ in range(n):
    weight, value = map(int, input().split())

    w.append(weight)
    v.append(value)

dp = [[0 for __ in range(k + 1)] for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, k + 1):
            weight = w[i]
            value = v[i]

            if j < weight:
                 dp[i][j] = dp[i - 1][j]
                
            else:
                 dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

print(dp[n][k])