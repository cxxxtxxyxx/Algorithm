def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        count = get_divisor_count(i)
        if count <= limit:
            answer += count
            continue
        answer += power
    return answer


def get_divisor_count(n):
    
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            
    if int(n ** 0.5) == n ** 0.5:
        count = count * 2 - 1
        return count
    
    count *= 2
    return count