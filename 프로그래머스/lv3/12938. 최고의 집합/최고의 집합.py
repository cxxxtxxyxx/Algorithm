def solution(n, s):
    answer = []
    if s < n:
        return [-1]

    
    answer = [s // n for __ in range(n)]
        
    for i in range(s % n):
        answer[i] += 1
    return sorted(answer)
    