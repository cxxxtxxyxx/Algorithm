import math

def get_gcd(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = math.gcd(answer, arr[i])
        
    return answer

def solution(arrayA, arrayB):
    answer = 0
    
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)
    
    resA = gcdA
    resB = gcdB
    
    for num in arrayB:
        if num % gcdA == 0:
            resA = 0
            break
            
    for num in arrayA:
        if num % gcdB == 0:
            resB = 0
            break
    
    if max(resA, resB) != 1:
        return max(resA, resB)
    return 0