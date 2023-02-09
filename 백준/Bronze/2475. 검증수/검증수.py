import sys

input = sys.stdin.readline

_arr = list(map(int, input().split()))

res = 0
for el in _arr:
    res += el ** 2

print(res % 10)