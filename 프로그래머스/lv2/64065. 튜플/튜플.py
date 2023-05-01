"""
튜플
1. 중복 원소 ok
2. 순서가 있음
3. 원소 개수 유한

s = 원소 개수 n, 중복 원소 없는 튜플


s를 이차원 배열로 만들면 됨

길이 짧은 순으로 sort, push
"},{"로 split, 
"""
# def solution(s):
#     answer = []
#     res = list(map(lambda x: x.split(","), s[2:-2].split("},{")))
#     res.sort(key=len)    
#     for case in res:
#         for ch in case:
#             if ch not in answer:
#                 answer.append(ch)
    
#     return list(map(int, answer))

def solution(s): 

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter