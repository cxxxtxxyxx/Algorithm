from collections import deque
def solution(numbers):
    # answer = [-1] * len(numbers)
    
    answer = []
    stack = []
    numbers.reverse()
    for number in numbers:
        if not answer:
            answer.append(-1)
            stack.append(number)
            continue
            
        if stack[-1] > number:
            answer.append(stack[-1])
            stack.append(number)
            
        else:
            while stack and stack[-1] <= number:
                stack.pop()
                
            if stack:
                answer.append(stack[-1])
                stack.append(number)
                
            else:
                answer.append(-1)
                stack.append(number)
                
            
        
        
    answer.reverse()
    return answer