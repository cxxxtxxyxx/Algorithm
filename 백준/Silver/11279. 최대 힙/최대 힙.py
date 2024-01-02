import sys
import heapq

input = sys.stdin.readline


heap = []

N = int(input().strip())

for __ in range(N):

    num = int(input().strip()) * -1

    if num == 0:
        if not heap:
            print(0)

        else:
            _max = heapq.heappop(heap)
            print(_max * -1)
    else:
        heapq.heappush(heap, num)