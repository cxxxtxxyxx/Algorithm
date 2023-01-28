import sys

input = sys.stdin.readline

n = int(input())

res = [[0 for i in range(10)] for j in range(n + 1)]

for i in range(10):
    res[1][i] = 1


for i in range(2, n + 1):
    for j in range(10):
        res[i][j] = sum(res[i - 1][:j+1]) % 10007

print(sum(res[n]) % 10007)
