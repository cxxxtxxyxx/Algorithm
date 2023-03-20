import heapq
import sys

input = sys.stdin.readline
N = int(input())
time = [list(map(int, input().split())) for __ in range(N)]

time.sort(key=lambda x: x[0])

heap = []
for s, e in time:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)

print(len(heap))