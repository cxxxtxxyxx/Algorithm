import sys

input = sys.stdin.readline
n = int(input())


res = [[0 for i in range(10)] for __ in range(101)]

for i in range(1, 10):
    res[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            res[i][j] = res[i - 1][1]
        elif j == 9:
            res[i][j] = res[i - 1][8]
        else:
            res[i][j] = res[i - 1][j - 1] + res[i - 1][j + 1]

print(sum(res[n]) % 1000000000)