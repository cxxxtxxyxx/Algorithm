def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        
        if "".join(list(map(str, stack[len(stack) - 4:]))) == "1231":
            answer += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            
    return answer