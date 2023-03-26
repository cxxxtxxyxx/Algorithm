import copy
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

town = [list(map(int, input().split())) for __ in range(N)]

"""
1. 살아남은 치킨집의 조합을 구한다
2. 집마다 치킨거리를 구함
"""

chicken_location = []
home_location = []
for i in range(N):
    for j in range(N):
        if town[i][j] == 2:
            chicken_location.append((i, j))
        elif town[i][j] == 1:
            home_location.append((i, j))

survive = list(combinations(chicken_location, M))

   

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def getDist(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

_min = sys.maxsize
for chicken_list in survive:

    total_dist = 0

    for home in home_location:
        c_dist = sys.maxsize
        for chicken in chicken_list:
            cx, cy = chicken
            hx, hy = home
            c_dist = min(c_dist, getDist(cx, hx, cy, hy))
        total_dist += c_dist

    _min = min(_min, total_dist)

print(_min)


