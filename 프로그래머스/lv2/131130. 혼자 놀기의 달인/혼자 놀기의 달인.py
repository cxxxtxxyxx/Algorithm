"""
1 ~ 100 숫자
"""

def solution(cards):
    answer = 0
    isopen = [False] * (len(cards))
    answer = []
    
    for i in range(len(cards)):
        if isopen[i] == False:
            isopen[i] = True
            next = cards[i] - 1
            count = 1
            while isopen[next] == False:
                isopen[next] = True
                next = cards[next] - 1
                count += 1
            answer.append(count)
                
    answer.sort(reverse=True)    
    return 0 if len(answer) == 1 else answer[0] * answer[1]