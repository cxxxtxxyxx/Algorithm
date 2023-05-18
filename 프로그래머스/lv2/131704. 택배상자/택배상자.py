def solution(order):
    
    stack = []
    
    count = 0
    for i in range(1, len(order) + 1):
        stack.append(i)
        while stack and stack[-1] == order[count]:
            count += 1
            stack.pop()
            
    return count