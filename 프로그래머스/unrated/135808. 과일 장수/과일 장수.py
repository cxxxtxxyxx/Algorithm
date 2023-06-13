def solution(k, m, score):
    answer = 0
    
    if m > len(score):
        return 0
    
    score.sort()
    
    score = score[len(score) % m:]
    for i in range(0, len(score), m):
        answer += score[i] * m
    return answer