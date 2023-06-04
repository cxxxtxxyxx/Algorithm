"""
원 포함되는 정수 좌표
r = 1 -> 1
r = 2 -> (r = 1 ~ 2) 사이점 1개씩 * 4 = 3 * 3
r = 3 -> (r = 2 ~ 3) 사이점 3개씩 * 4 = 5 * 5 
r = 4 -> (r = 3 ~ 4) 사이점 5개씩 * 4
내부 점 = pow(2r + 1)
"""
import math
def solution(r1, r2):

    count = 0
    
    for i in range(1, r2 + 1):
        vr2 = r2 ** 2 - i ** 2 if r2 ** 2 - i ** 2 >= 0 else 0
        vr1 = r1 ** 2 - i ** 2 if r1 ** 2 - i ** 2 >= 0 else 0
        count += math.floor(math.sqrt(vr2)) - math.ceil(math.sqrt(vr1)) + 1
    count *= 4
        
    
    return count