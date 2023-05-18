import sys
def solution(sequence, k):
    answer = []
    _min = sys.maxsize
    
    start = 0
    end = 0
    _sum = sum(sequence[start:end+1])
    
    while end < len(sequence):
        if _sum == k and _min > end - start + 1:
            _min = end - start + 1
            answer = [start, end]
            end += 1
            if end >= len(sequence):
                break
            _sum += sequence[end]
        elif _sum > k:
            start += 1
            _sum -= sequence[start - 1]
        else:
            end += 1
            if end >= len(sequence):
                break
            _sum += sequence[end]
            
            
    return answer