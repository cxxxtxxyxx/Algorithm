import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    
    while True:
        if heap[0] >= K:
            return answer
        
        if len(heap) == 1 and heap[0] < K:
            return -1
        
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer += 1
        
    return -1