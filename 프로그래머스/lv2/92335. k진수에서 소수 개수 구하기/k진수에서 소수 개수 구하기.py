def solution(n, k):
    stack = []
    temp = n
    while temp != 0:
        stack.append(temp % k)
        temp = temp // k
    stack.reverse()
    
    res_str = "".join(list(map(str, stack))).split("0")
    
    return len(list(filter(lambda x: x != '' and isPrime(int(x)), res_str)))

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True

