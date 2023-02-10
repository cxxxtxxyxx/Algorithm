import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n, k = map(int, input().split())

distance = [INF] * (100001)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for next in ((now + 1, 1), (now - 1, 1), (now * 2, 0)):
            if not (0 <= next[0] < 100001):
                continue

            cost = dist + next[1]
            if cost < distance[next[0]]:
                    distance[next[0]] = cost
                    heapq.heappush(q, (cost, next[0]))
            # if next == now + 1 or next == now - 1:
            #     cost = dist + next[1]

            #     if cost < distance[next]:
            #         distance[next] = cost
            #         heapq.heappush(q, (cost, next))

            # else:
            #     cost = dist

            #     if cost < distance[next]:
            #         distance[next] = cost
            #         heapq.heappush(q, (cost, next))
dijkstra(n)
print(distance[k])