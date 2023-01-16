def solution(prices):
    answer = [0] * len(prices)
    current_num = prices[-1]

    stack = []

    count = 0
    
    for time, item in enumerate(prices):
        
        while stack and stack[-1][1] > item:
            pop = stack.pop()
            answer[pop[0]] = time - pop[0]
        
        stack.append((time, item))

    while stack:
        v = stack.pop()
        answer[v[0]] = len(prices) - 1 - v[0]

    return answer

print(solution([1, 2, 3, 2, 3]))