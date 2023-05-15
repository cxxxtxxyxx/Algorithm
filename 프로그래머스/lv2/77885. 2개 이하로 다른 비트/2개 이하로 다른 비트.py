def solution(numbers):
    answer = []
    
    for number in numbers:
        binary_str = "0b" + "0" * 10 + bin(number)[2:]
        if binary_str[-1] == '0':
            answer.append(number + 1)
            continue
        idx = binary_str.rfind("01")
        answer.append(int(binary_str[:idx] + "10" + binary_str[idx + 2:], 2))
            
            
    return answer
            