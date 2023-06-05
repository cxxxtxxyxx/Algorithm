def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if get(i) % 2 == 0:
            answer += i
            continue
        answer -= i
    return answer

def get(x):
    cnt = 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            cnt += 1
            
    
    if x ** 0.5 == int(x ** 0.5):
        
        return cnt * 2 + 1
    return cnt * 2 + 2