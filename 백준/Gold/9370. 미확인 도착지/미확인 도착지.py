import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

T = int(input()) # 테스트 케이스 갯수

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []

    distance[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for next in graph[now]:
            cost = dist + next[1]

            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance


result = [[] for __ in range(T)]
for case in range(T):
    # n = 교차로 개수, m = 도로 개수, t = 목적지 후보 개수
    n, m, t = map(int, input().split())

    # s = 예술가들 출발지, (g != h) g, h = 교차로
    s, g, h = map(int, input().split())

    graph = [[] for ___ in range(n + 1)]
    for __ in range(m):
        # a와 b사이에 길이 d의 양방향 도로가 존재
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    distance = dijkstra(s)
    # print(distance)

    destinations = [int(input()) for __ in range(t)]

    for destination in destinations:
        v1 = dijkstra(g)
        v2 = dijkstra(h)

        if distance[destination] == distance[g] + v1[h] + v2[destination] or distance[destination] == distance[h] + v2[g] + v1[destination]:
            result[case].append(destination)


    result[case].sort()

for res in result:
    print(*res)