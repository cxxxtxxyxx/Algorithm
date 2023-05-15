# def solution(x, y, n):
#     dp = [-1] * (y + 1)
#     dp[x] = 0
    
#     for i in range(x + 1, y + 1):
#         if i - n >= x and dp[i - n] != -1:
#             dp[i] = dp[i - n] + 1
        
#         if i % 2 == 0 and i // 2 >= x and dp[i // 2] != -1:
#             if dp[i] == -1:
#                 dp[i] = dp[i // 2] + 1
#             else:
#                 dp[i] = min(dp[i], dp[i // 2] + 1)
            
#         if i % 3 == 0 and i // 3 >= x and dp[i // 3] != -1:
#             if dp[i] == -1:
#                 dp[i] = dp[i // 3] + 1
#             else:
#                 dp[i] = min(dp[i], dp[i // 3] + 1)
#     return dp[y]

def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer

        nxt = set()
        for i in s:
            if i+n <= y:
                nxt.add(i+n)
            if i*2 <= y:
                nxt.add(i*2)
            if i*3 <= y:
                nxt.add(i*3)
        s = nxt
        answer+=1

    return -1