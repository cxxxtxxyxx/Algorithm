def solution(food):
    a1 = ''
    a2 = ''
    
    for idx, f in enumerate(food):
        if idx == 0:
            continue
        
        a1 += str(idx) * (f // 2)
        a2 = str(idx) * (f // 2) + a2
            
    return a1 + '0' + a2