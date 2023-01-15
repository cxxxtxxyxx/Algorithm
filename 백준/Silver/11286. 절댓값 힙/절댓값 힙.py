import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())

abs_heap = []

for __ in range(n):
    num_input = int(input().strip())

    if num_input == 0:
        if len(abs_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(abs_heap)[1])

    else:
        heapq.heappush(abs_heap, (abs(num_input), num_input))
