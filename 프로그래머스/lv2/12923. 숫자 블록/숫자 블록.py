def solution(begin, end):
    answer = []


    # 소수 구해서 소수로 나눠지는 처음거 추가
    for i in range(begin, end + 1):
        num = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                num = j
                if i // j <= 10_000_000:
                    answer.append(i // j)
                    break
        else:
            if num != 0:
                answer.append(num)
            else:
                answer.append(1)
            
        
    if begin == 1:
        answer[0] = 0
    return answer