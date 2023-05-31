# def solution(n, k, enemy):
import heapq
def solution(n, k, enemy):
    answer = 0
    
    """
    가능한 선에서 가장 큰 enemy들에 대해 무적권 사용해야함
    그럼 이번 enemy가 큰건지 안큰건지 어떻게 앎?
    힙을 써볼까
    힙 크기가 k보다 커지면 가장 큰거 n에서 빼줌
    """
    
    heap = []
    for i in range(len(enemy)):
        heapq.heappush(heap, enemy[i])
        if len(heap) > k:
            n -= heapq.heappop(heap)
        
        if n < 0:
            return i
    
    return len(enemy)