from collections import deque
def solution(numbers):
    # answer = [-1] * len(numbers)
    
    answer = deque()
    stack = []
    numbers.reverse()
    for number in numbers:
        if not answer:
            answer.appendleft(-1)
            stack.append(number)
            continue
            
        if stack[-1] > number:
            answer.appendleft(stack[-1])
            stack.append(number)
            
        else:
            while stack and stack[-1] <= number:
                stack.pop()
                
            if stack:
                answer.appendleft(stack[-1])
                stack.append(number)
                
            else:
                answer.appendleft(-1)
                stack.append(number)
                
            
        
        
    
    return list(answer)