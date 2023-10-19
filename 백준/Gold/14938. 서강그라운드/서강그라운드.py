import heapq
import sys

INF = sys.maxsize

input = sys.stdin.readline

n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))

graph = [[] for __ in range(n + 1)]

for __ in range(r):
    x, y, dist = map(int, input().split())

    graph[x].append((dist, y))
    graph[y].append((dist, x))


def dijkstra(start):
    
    heap = []
    distance = [INF] * (n + 1)
    heapq.heappush(heap, [0, start])
    distance[start] = 0

    while heap:
        now_dist, now_node = heapq.heappop(heap)

        for next_dist, next_node in graph[now_node]:
            if next_dist + now_dist < distance[next_node]:
                next_dist += now_dist
                distance[next_node] = next_dist
                heapq.heappush(heap, (next_dist, next_node))

    return distance

_max = int(-1e9)

for i in range(1, n + 1):
    distance = dijkstra(i)

    _sum = 0

    for j in range(1, n + 1):
        if distance[j] <= m:
            _sum += items[j]

    _max = max(_max, _sum)

print(_max)


