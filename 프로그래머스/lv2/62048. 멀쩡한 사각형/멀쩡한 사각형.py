# import math
# def solution(w,h):
#     return w * h - get_available(w, h) * math.gcd(w, h)


# def get_available(w, h):
#     gcd = math.gcd(w, h)
#     short_w = w // gcd
#     short_h = h // gcd
#     dx = [0, 0, 1, 1]
#     dy = [0, 1, 0, 1]
#     result = 0
#     for i in range(short_w - 1):
#         for j in range(short_h - 1):
#             min_cnt = 0
#             max_cnt = 0
#             for k in range(4):
#                 px, py = dx[k] + i, dy[k] + j
#                 if fx(px, py, short_w, short_h) <= 0:
#                     max_cnt += 1
                    
#             if max_cnt == 4 or min_cnt == 4:
#                 result += 1
            
#     return short_w * short_h - result * 2

# def fx(x, y, short_w, short_h):
#     return y + short_w / short_h * x- short_w

import math
def solution(w, h):
#     answer = 0
    gcd = math.gcd(w, h)
    mini_w, mini_h = w // gcd, h // gcd
#     dp = [[0] * (mini_w + 1) for __ in range(mini_h + 1)]
    
#     for i in range(min(mini_h + 1, mini_w + 1)):
#         dp[i][i] = i
        
#     for i in range(mini_h + 1):
#         for j in range(mini_w + 1):
#             if dp[i][j] == 0:
#                 dp[i][j] = i + j - 1
    if w == h:
        return w * h - w
    return w * h - gcd * (mini_h + mini_w - 1)
                
    
    """
    꼭지점 안만나는 녀석들은 못쓰는 개수가 가로 + 세로 - 1임 (최소거리)
    만나는 녀석들은 채우면 됨 1, 1, 2, 2로
    최대공약수로 나눈 걸로 찾으면 됨
    mini w, h까지 dp로 구해서 w * h - dp * gcd 하면 끝
    """
#     dp[1][1] = 0
#     dp[1][2] = 0
#     for i in range(1, h + 1):
#         for j in range(1, w + 1):
    
    