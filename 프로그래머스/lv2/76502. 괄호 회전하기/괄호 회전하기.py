# from collections import deque


# def solution(s):
#     q = deque(list(s))
#     answer = is_correct(q)
    
#     for __ in range(1, len(q)):
#         q.rotate(-1)
#         answer += is_correct(list(q))
    
#     return answer

# def is_correct(str):
#     stack = []
#     open = ["[", "(", "{"]
#     _dict = dict()
#     _dict["]"] = "["
#     _dict[")"] = "("
#     _dict["}"] = "{"
    
    
#     for ch in str:
        
#         if not stack:
#             stack.append(ch)
#             continue
            
#         if ch in open:
#             stack.append(ch)
#             continue
            
#         else:
#             if stack[-1] == _dict[ch]:
#                 stack.pop()
#                 continue
#             return 0

#     if stack:
#         return 0
#     return 1
        

from collections import deque


def solution(s):
    q = deque(list(s))
    answer = is_correct(s)
    
    for __ in range(1, len(q)):
        q.rotate(-1)
        answer += is_correct(''.join(q))
    
    return answer

def is_correct(s):
    while True:
        if "[]" in s:
            s = s.replace("[]", "")
        elif "()" in s:
            s = s.replace("()", "")
        elif "{}" in s:
            s = s.replace("{}", "")
        else:
            return 0 if s else 1