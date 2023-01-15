import sys
import heapq

input = sys.stdin.readline

min_heap = []

n = int(input().strip())

for __ in range(n):
    input_num = int(input().strip())

    if input_num == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, input_num)
