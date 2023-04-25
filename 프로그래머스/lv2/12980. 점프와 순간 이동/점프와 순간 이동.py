"""
기능 1. 한번에 K칸 !!점프!!
기능 2. (현재까지 온 거리) * 2 !!순간이동!!

순간이동시 건전지 사용량 x
점프시 k칸 만큼 건전지 사용

점프 이동 최소화
"""

# def solution(n):
    
#     if n == 1:
#         return 1
    
#     count = 0
#     while n != 1:
#         if n % 2 == 0:
#             n //= 2
#             continue
#         n -= 1
#         count += 1
        
#     return count + 1

def solution(n):
    x = 2
    return bin(n)[2:].count('1')