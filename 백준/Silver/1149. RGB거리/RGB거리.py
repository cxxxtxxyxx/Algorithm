import sys

input = sys.stdin.readline


N = int(input())

dp = [0] * 3
tmp = [0] * 3


for i in range(N):
    R, G, B = map(int, input().split())

    for j in range(3):

        if j == 0:
            tmp[j] = min(dp[1], dp[2]) + R

        elif j == 1:
            tmp[j] = min(dp[0], dp[2]) + G

        else:
            tmp[j] = min(dp[0], dp[1]) + B

    
    dp = tmp[:]

print(min(dp))
