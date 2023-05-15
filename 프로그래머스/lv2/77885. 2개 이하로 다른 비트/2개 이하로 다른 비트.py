def solution(numbers):
    answer = []
    
    for number in numbers:
        binary_str = "0b" + "0" * 10 + bin(number)[2:]
        if binary_str[-1] == '0':
            answer.append(int(binary_str[:-1] + '1', 2))
            continue
            
        answer.append(int(binary_str[:binary_str.rfind("01")] + "10" + binary_str[binary_str.rfind("01") + 2:], 2))
            
            
    return answer
            