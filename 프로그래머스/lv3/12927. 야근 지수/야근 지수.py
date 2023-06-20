import heapq
def solution(n, works):
    answer = 0
    
    if sum(works) < n:
        return 0
    works = list(map(lambda x: -x, works))
    heapq.heapify(works)
        

    for i in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1)
        
    return sum(map(lambda x: x ** 2, works))
