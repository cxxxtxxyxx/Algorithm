import sys

input = sys.stdin.readline

res = [0] * 1000001
res[1] = 1
res[2] = 2

n = int(input())

for idx in range(3, n + 1):
    res[idx] = (res[idx - 1] + res[idx - 2]) % 15746


print(res[n])
