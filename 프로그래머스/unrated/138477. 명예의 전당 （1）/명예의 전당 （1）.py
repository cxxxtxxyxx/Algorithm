import heapq
def solution(k, score):
    answer = []
    _min = min(score[:k])
    heap = []
    for i in range(len(score)):
        if i < k:
            heapq.heappush(heap, score[i])
            answer.append(heap[0])
            continue
        
        if heap[0] < score[i]:
            heapq.heappop(heap)
            heapq.heappush(heap, score[i])
        
        answer.append(heap[0])
            
    return answer