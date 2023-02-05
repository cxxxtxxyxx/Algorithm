import sys
import heapq
input = sys.stdin.readline

INF = sys.maxsize
V, E = map(int, input().strip().split())
start = int(input())

graph = [[] for __ in range(V + 1)]
for __ in range(E):
    u, v, w = map(int, input().strip().split())
    graph[u].append((w, v))

distance = [INF] * (V + 1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, next = heapq.heappop(q)

        if distance[next] < dist:
            continue

        for node in graph[next]:
            cost = dist + node[0]
            if cost < distance[node[1]]:
                distance[node[1]] = cost
                heapq.heappush(q, (cost, node[1]))


dijkstra(start)
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


