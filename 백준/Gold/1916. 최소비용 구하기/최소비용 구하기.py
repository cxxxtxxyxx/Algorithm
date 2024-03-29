import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
graph = [[] for __ in range(n + 1)]
distance = [INF] * (n + 1)
for __ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))

start, end = map(int, input().split())


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])
