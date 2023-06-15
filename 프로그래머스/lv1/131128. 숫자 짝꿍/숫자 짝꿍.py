import heapq
def solution(X, Y):
    answer = ""
    X = list(X)
    Y = list(Y)
    heapq.heapify(X)
    heapq.heapify(Y)

    if len(X) > len(Y):
        X, Y = Y, X
        
    while X and Y:
        if X[0] == Y[0]:
            answer += heapq.heappop(X)
            heapq.heappop(Y)
        else:
            while X and Y and X[0] < Y[0]:
                heapq.heappop(X)
                
            while X and Y and X[0] > Y[0]:
                heapq.heappop(Y)
                
    answer = answer[::-1]
    
    if answer == "":
        return "-1"
    if answer[0] == "0":
        return "0"
    
    return answer
    
    return ""



# def solution(X, Y):
#     d = dict()
#     X = list(X)
#     Y = list(Y)
#     if len(X) > len(Y):
#         X, Y = Y, X
#     for x in X:
#         if x in Y:
#             if x not in d:
#                 d[x] = 1
#             else:
#                 d[x] += 1
#             Y.remove(x)
#     answer = ""
#     for key in sorted(d.keys(), reverse=True):
#         answer += d[key] * key
    
#     if answer == "":
#         return "-1"
    
#     if answer[0] == "0":
#         return "0"
#     return answer