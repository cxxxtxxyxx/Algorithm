import sys

input = sys.stdin.readline

n = int(input())

res = int(n ** 0.5)
if res ** 2 >= n:
    print(res)
else:
    print(res + 1)