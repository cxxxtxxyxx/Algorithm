from collections import defaultdict
import sys

def solution(k, tangerine):
    # 1 2 2 3 3 4 5 5 
    # step 1: len(tangerine) - k 만큼 제외한 귤의 종류가 최소가 되도록
    count_dict = defaultdict(int)
    
    for el in tangerine:
        count_dict[el] += 1
    
    v = list(count_dict.values())
    v.sort(reverse=True)
    start = 0
    end = 0

    _sum = v[start]
    count = sys.maxsize
    
    while start <= end and end < len(v):
        if _sum >= k:
            count = min(count, end - start + 1)
            return count
            
        if end + 1 < len(v):
            end += 1
            _sum += v[end]
            continue
            
        break
