import sys
import heapq

input = sys.stdin.readline

N = int(input())
lecture_list = [list(map(int, input().split())) for _ in range(N)]

lecture_list.sort(key=lambda x:x[0])
heap = []
heapq.heappush(heap, lecture_list[0][1])

for i in range(1, N):
    if lecture_list[i][0] < heap[0]:
        heapq.heappush(heap, lecture_list[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lecture_list[i][1])


print(len(heap))