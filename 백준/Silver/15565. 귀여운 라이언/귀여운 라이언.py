import sys
from collections import Counter

input = sys.stdin.readline

N, K = map(int, input().split())

# 라이언 1, 어피치 2


doll = list(map(int, input().split()))

d_dict = dict(Counter(doll))
if 1 in d_dict and d_dict.get(1) < K:
    print(-1)
    exit()


left, right = 0, 0
lion_cnt = 0
_min = sys.maxsize

while left < N and right < N and doll[left] == 2:
    left += 1
    right += 1


while right < N:
    if left >= N:
        break

    if doll[right] == 1:
        lion_cnt += 1
    
    right += 1


    if lion_cnt == K:
        _min = min(_min, right - left)

        while left + 1 < N and doll[left + 1] == 2:
            left += 1

        lion_cnt -= 1
        left += 1
    
if _min == sys.maxsize:
    print(-1)
    exit()
print(_min)
