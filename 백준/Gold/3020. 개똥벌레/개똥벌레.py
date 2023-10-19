import sys
from bisect import bisect_left

input = sys.stdin.readline

N, H = map(int, input().split())


"""
뒤집어서 생각
4로 지난거는
뒤집은거는 5 - 4 + 1 => (H - 구간 + 1)을 지난 것
"""

bottom = []
top = []
for i in range(1, N + 1):
    if i % 2 == 0:
        top.append(int(input()))
        continue
    bottom.append(int(input()))
top.sort()
bottom.sort()
_min_result = int(1e9)
cnt = 1

for i in range(1, H + 1):

    tc = len(top) - bisect_left(top, H - i + 1)
    bc = len(bottom) - bisect_left(bottom, i)

    _min_total = tc + bc

    if _min_total < _min_result:
        _min_result = _min_total
        cnt = 1
        continue
    
    if _min_total == _min_result:
        cnt += 1

print(_min_result, cnt)