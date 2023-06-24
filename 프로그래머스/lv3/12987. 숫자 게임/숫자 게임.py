import heapq

def solution(A, B):
    answer = 0
    
    heapq.heapify(A)
    heapq.heapify(B)
    
    
    while B:
        if A[0] < B[0]:
            answer += 1
            heapq.heappop(B)
            heapq.heappop(A)
            continue
        
        heapq.heappop(B)
            
        
        
    return answer