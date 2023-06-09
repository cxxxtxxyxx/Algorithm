def solution(d, budget):
    d.sort()
    
    _sum = 0
    i = 0
    while i < len(d):
        _sum += d[i]
        if _sum > budget:
            return i
            
        i += 1
    return i