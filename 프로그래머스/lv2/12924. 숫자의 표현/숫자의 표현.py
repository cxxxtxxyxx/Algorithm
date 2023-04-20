def solution(n):
    answer = 0
    
    # step1: start, end 설정
    if n == 1:
        return 1
    start, end = 1, 2
    
    # step2: end를 늘려가며 합을 구함 n을 넘으면 start를 늘림 
    
    _sum = start
    count = 0
    while end <= n:
        _sum += end
            
        if _sum < n:
            end += 1
            
        else:
            if _sum == n:
                count += 1
                end += 1
            else:
                _sum -= start
                start += 1
                _sum -= end
            
        
    return count