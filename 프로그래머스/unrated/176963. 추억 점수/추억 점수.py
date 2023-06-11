from collections import defaultdict

def solution(name, yearning, photo):
    d = defaultdict(int)
    answer = []
    
    for idx, year in enumerate(yearning):
        d[name[idx]] = year
        
    for case in photo:
        _sum = 0
        for c in case:
            _sum += d[c]
        answer.append(_sum)
    return answer