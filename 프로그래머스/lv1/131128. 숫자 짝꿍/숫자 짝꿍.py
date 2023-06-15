from collections import Counter
from collections import defaultdict
def solution(X, Y):
    answer = ""
    gyo = sorted(list(set(X) & set(Y)))
    
    X, Y = defaultdict(int, dict(Counter(X))), defaultdict(int, dict(Counter(Y)))
    for i in gyo:
        answer = i * min(X[i], Y[i]) + answer
    
    if answer == "":
        return "-1"
    
    if answer[0] == "0":
        return "0"
    return answer

# import heapq
# def solution(X, Y):
#     answer = ""
#     X = list(X)
#     Y = list(Y)
#     heapq.heapify(X)
#     heapq.heapify(Y)

#     if len(X) > len(Y):
#         X, Y = Y, X
        
        
#     while X and Y:
#         if X[0] == Y[0]:
#             answer += heapq.heappop(X)
#             heapq.heappop(Y)
#         else:
#             while X and Y and X[0] < Y[0]:
#                 heapq.heappop(X)
                
#             while X and Y and X[0] > Y[0]:
#                 heapq.heappop(Y)
                
#     answer = answer[::-1]
    
#     if answer == "":
#         return "-1"
#     if answer[0] == "0":
#         return "0"
    
#     return answer