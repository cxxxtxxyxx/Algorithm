import heapq
import sys

INF = sys.maxsize
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for __ in range(N + 1)]

for __ in range(N - 1):
    c, n, d = map(int, input().strip().split())
    graph[c].append((n, d))
    graph[n].append((c, d))



def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    heap = []

    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if dist > distance[now]:
            continue

        for node in graph[now]:
            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(heap, (cost, node[0]))

    return distance

for i in range(M):
    s, e = map(int, input().strip().split())
    dist = dijkstra(s)
    print(dist[e])
