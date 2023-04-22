def solution(s):
    
    stack = []
    
    for ch in s:
        
        if not stack:
            stack.append(ch)
            continue
            
        if stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
            
    if stack:
        return 0
    
    return 1
        