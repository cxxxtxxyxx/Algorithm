import sys

input = sys.stdin.readline

res = list(map(int, input().split()))
res.sort()
print(res[1])