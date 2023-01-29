import sys
import itertools

input = sys.stdin.readline

n = int(input())

tri = [list(map(int, input().split())) for __ in range(n)]

res = [[0] * (i + 1) for i in range(n)]

res[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            res[i][j] = res[i - 1][j] + tri[i][j]
        elif i == j:
            res[i][j] = res[j - 1][j - 1] + tri[i][j]
        else:
            res[i][j] = max(res[i - 1][j - 1], res[i - 1][j]) + tri[i][j]


print(max(list(itertools.chain(*res))))