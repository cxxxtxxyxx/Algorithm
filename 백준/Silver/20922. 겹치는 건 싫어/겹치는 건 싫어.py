import sys
from collections import Counter

input = sys.stdin.readline


N, K = map(int, input().split())

s = list(map(int, input().split()))
cnt_dict = dict()


left = 0
right = 0
res = 0
while right < N:

    if s[right] in cnt_dict:
        if cnt_dict[s[right]] < K:
            cnt_dict[s[right]] += 1
            right += 1
        
        else:
            cnt_dict[s[left]] -= 1
            left += 1

    else:
        cnt_dict[s[right]] = 1
        right += 1

    res = max(res, right - left)
    


print(res)

