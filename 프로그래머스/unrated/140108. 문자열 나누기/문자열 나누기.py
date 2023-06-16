def solution(s):
    answer = 0
    
    same = 1
    diff = 0
    same_ch = s[0]
    i = 1
    
    while i < len(s):
        if same == diff:
            answer += 1
            same = 0
            diff = 0
            if i + 1 < len(s):
                same_ch = s[i + 1]
            else:
                break
            
        if s[i] != same_ch:
            diff += 1
        else:
            same += 1
        
        
                
        i += 1
        
    return answer + 1