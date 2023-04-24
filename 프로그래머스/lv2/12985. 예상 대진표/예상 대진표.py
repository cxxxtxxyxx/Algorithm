def next_number(num):
    if num % 2 == 0:
        return num // 2
    
    return num // 2 + 1


def solution(n,a,b):
    
    answer = 0

    # step 1 홀수 // 2 + 1, 짝수 // 2 => 다음 라운드 번호
    
    while True:
        answer += 1
        
        if max(a, b) - min(a, b) == 1 and max(a, b) // 2 == min(a, b) // 2 + 1:
            return answer
        
        a = next_number(a)
        b = next_number(b)

    return answer