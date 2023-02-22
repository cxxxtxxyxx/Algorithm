"""
1234 2234 3334 4444
7 % 4 == 1, 3 몫 + 나머지 => 목행 나머지열
14 % 4 = 3, 2
"""

# def solution(n, left, right):
#     answer = []
#     ls, le = left // n, left % n
#     rs, re = right // n, right % n
#     l_arr = [ls + 1 for __ in range(ls + 1)] + [ls + 1 + i for i in range(1, n - (ls + 1) + 1)]
#     r_arr = [rs + 1 for __ in range(rs + 1)] + [rs + 1 + i for i in range(1, n - (rs + 1) + 1)]
#     for i in range(ls, rs + 1):
#         if i == ls:
#             answer.extend(l_arr[le:])
#         elif i == rs:
#             answer.extend(r_arr[:re + 1])
#         else:
#             _add_arr = [i + 1 for __ in range(0, i + 1)] + [i + 1 + j for j in range(1, (n - (i + 1) + 1))]
#             answer.extend(_add_arr)
            
#     return answer

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        l = i // n
        r = i % n
        
        _max = max(l, r)
        answer.append(_max + 1)
        
    return answer