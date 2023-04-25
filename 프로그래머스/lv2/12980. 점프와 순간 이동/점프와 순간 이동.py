"""
기능 1. 한번에 K칸 !!점프!!
기능 2. (현재까지 온 거리) * 2 !!순간이동!!

순간이동시 건전지 사용량 x
점프시 k칸 만큼 건전지 사용

점프 이동 최소화
"""

def solution(n):
    
    if n == 1:
        return 1
    
    if n == 2:
        return 1
    # step 1 : 디피 배열 N만큼 만들기
    
    plus_flag = False
    tmp = n
    
    if tmp % 2 != 0:
        plus_flag = True
        tmp -= 1
        
    count = 0
    while tmp != 1:
        if tmp % 2 == 0:
            tmp //= 2
            continue
        tmp -= 1
        count += 1
        
    if plus_flag == True:
        return count + 2
    return count + 1
        
    
#     dp = [0] * (tmp + 1)
    
#     dp[1] = 1
    
#     if n == 1:
#         return 1
    
#     # step 2 : 2부터 dp 배열 최솟값 구하기
#     for i in range(2, tmp + 1):
#         if i % 2 == 0:
#             dp[i] = min(dp[i - 1] + 1, dp[i // 2])
#             continue
#         dp[i] = dp[i - 1] + 1
    

#     if plus_flag:
#         return dp[tmp] + 1
    
#     return dp[tmp]