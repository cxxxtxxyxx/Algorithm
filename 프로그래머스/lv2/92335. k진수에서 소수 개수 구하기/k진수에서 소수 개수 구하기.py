def solution(n, k):
    
    _count = 0
    digit_num = []

    temp = n
    while temp > 0:
        digit_num.append(temp % k)
        temp //= k
    digit_num.reverse()

    _digit = "".join(list(map(str, digit_num)))
    

    _count = len(list(filter(lambda x: x != '' and isPrime(int(x)), _digit.split("0"))))

    return _count

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True