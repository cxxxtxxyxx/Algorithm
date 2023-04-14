import sys
from collections import deque

input = sys.stdin.readline


# N 접시 수, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
N, d, k, c = map(int, input().split())

lane = []

for __ in range(N):
    lane.append(int(input()))

# lane.rotate(-1) 


_max = 0
start = 0
end = 0


while start != len(lane):
    sushi = set()
    end = start + k
    flag = True

    for i in range(start, end):
        sushi.add(lane[i % len(lane)])
        if lane[i % len(lane)] == c:
            flag = False

    if flag:
        _max = max(_max, len(sushi) + 1)
    else:
        _max = max(_max, len(sushi))


    start += 1


print(_max)
        