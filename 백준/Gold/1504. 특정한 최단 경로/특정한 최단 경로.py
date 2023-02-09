import sys
import copy
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n, e = map(int, input().split())

graph = [[] for __ in range(n)]

for __ in range(e):
    a, b, c = map(int, input().split())

    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))


v1, v2 = list(map(int, input().split()))


def dijkstra(start):
    q = []
    distance = [INF for __ in range(n)]
    distance[start] = 0

    heapq.heappush(q, (0, start))
    while q:

        dist, now = heapq.heappop(q)
        # if now == end:
        #     return distance[now]
        #     break

        if dist > distance[now]:
            continue

        for node in graph[now]:
            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

    return distance

one = dijkstra(0)
two = dijkstra(v1 - 1)
three = dijkstra(v2 - 1)

cnt = min(one[v1 - 1] + two[v2 - 1] + three[n - 1], one[v2 - 1] + three[v1 - 1] + two[n - 1])

print(cnt if cnt < INF else -1)
    


