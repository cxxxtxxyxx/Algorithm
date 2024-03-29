# def solution(n):
#     if n == 1:
#         return 1
    
#     if n == 2:
#         return 2
    
#     if n == 3:
#         return 3
    
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 2
#     dp[3] = 3
    
#     for i in range(4, n + 1):
#         dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

        
#     return dp[n]


def solution(n):
    
    if n == 1:
        return 1
    
    a, b = 1, 2

    for i in range(2, n):
        a, b = b, (a + b) % 1234567
        
    return b
