import sys
from collections import Counter
from collections import defaultdict
def solution(gems):
    answer = []
    gem_count = defaultdict(int)
    
#     # step 1: gem을 set으로 만듬
#     # step 2: 투포인터를 활용해서 set에 넣어줌 (gem과 길이 같아질 때 까지)
#     # step 3: 길이가 같은 순간 start, end를 answer에 넣어줌
#     # step 4: 값 바꿔주고 나서 start를 늘려주며 기존 set에서 하나씩 빼줌 (있을 때)
    
    
    duplicated_gems = set(gems)
    result = set()
    start = 0
    end = 0
    min_len = sys.maxsize
    
    if len(duplicated_gems) == 1:
        return [1, 1]
    
    
    while start <= end and end < len(gems):        
            
        if len(result) < len(duplicated_gems):
            result.add(gems[end])
            gem_count[gems[end]] += 1
            end += 1
            continue
            
        
        
        while len(result) == len(duplicated_gems):
            if min_len > end - start + 1:
                answer = [start + 1, end]
                min_len = end - start + 1
            if gem_count[gems[start]] >= 1:
                gem_count[gems[start]] -= 1
                if gem_count[gems[start]] == 0:
                    result.remove(gems[start])
                start += 1
                
    while len(result) == len(duplicated_gems):
        if min_len > end - start + 1:
            answer = [start + 1, end]
            min_len = end - start + 1
        if gem_count[gems[start]] >= 1:
            gem_count[gems[start]] -= 1
            if gem_count[gems[start]] == 0:
                result.remove(gems[start])
            start += 1


    
    return answer