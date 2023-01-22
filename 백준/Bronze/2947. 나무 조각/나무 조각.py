import sys


input = sys.stdin.readline

res = list(map(int, input().strip().split()))

for i in range(len(res) - 1):
    for j in range(len(res) - 1):
        if res[j] > res[j + 1]:
            res[j], res[j + 1] = res[j + 1], res[j]
            print(*res)