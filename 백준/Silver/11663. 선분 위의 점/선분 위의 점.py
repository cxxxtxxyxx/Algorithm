import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, M = map(int, input().split())
coords = list(map(int, input().split()))
coords.sort()
lines = [list(map(int, input().split())) for __ in range(M)]

res = []

for line in lines:
    left = bisect_left(coords, line[0])
    right = bisect_right(coords, line[1])

    res.append(right - left)

for el in res:
    print(el)