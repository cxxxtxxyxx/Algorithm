import sys

input = sys.stdin.readline

n = int(input())

res = [0, 1, 1, 1, 2, 2]

for idx in range(6, 101):
    res.append(res[idx - 1] + res[idx - 5])


for __ in range(n):
    print(res[int(input())])