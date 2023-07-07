def solution(arr, divisor):
    answer = []
    
    for el in arr:
        if el % divisor == 0:
            answer.append(el)

    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)