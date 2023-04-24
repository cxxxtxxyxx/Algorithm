def solution(n,a,b):
    
    answer = 0

    # step 1 홀수 // 2 + 1, 짝수 // 2 => 다음 라운드 번호
    
    while a != b:
        answer += 1
        
        
        a = (a + 1) // 2
        b = (b + 1) // 2

    return answer