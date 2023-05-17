def solution(numbers, target):
    answer = 0
    stack = [(numbers[0],0), (-numbers[0],0)]
    
    while stack:
        _sum, depth = stack.pop()
        
        if depth + 1 == len(numbers):
            if _sum == target:
                answer += 1
            continue
            
        if depth + 1 < len(numbers):
            stack.append([_sum + numbers[depth + 1], depth + 1])
            stack.append([_sum - numbers[depth + 1], depth + 1])
            
                
    return answer