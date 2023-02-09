import sys
import heapq
import copy
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# def bfs(i, j):
#     q = deque()

#     visited[i][j] = True
#     q.append((i, j))

#     while q:
#         x, y = q.popleft()

#         for k in range(4):
#             nx = dx[k] + x
#             ny = dy[k] + y

#             if not (0 <= nx < n and 0 <= ny < n):
#                 continue

#             if visited[nx][ny] == False:
#                 q.append((nx, ny))
#                 visited[nx][ny] = True
#                 graph[nx][ny] += graph[x][y]

#             else:
#                 if graph[nx][ny] == graph[x][y] + 1:
#                     break
#                 q.append((nx, ny))
#                 graph[nx][ny] = min(graph[nx][ny], graph)

# def dijkstra(i, j):
#     global visited
#     global distance
#     global graph
#     q = []

#     visited[i][j] = True
#     heapq.heappush(q, (graph[i][j], i, j))

#     while q:
#         cost, x, y = heapq.heappop(q)

#         # if distance[x][y] < cost:
#         #     continue

#         for k in range(4):
#             nx = dx[k] + x
#             ny = dy[k] + y

#             if not (0 <= nx < n and 0 <= ny < n):
#                 continue

#             new_cost = cost + graph[nx][ny]
#             if visited[nx][ny] == False:
#                 distance[nx][ny] = new_cost
#                 heapq.heappush(q, (distance[nx][ny], nx, ny))
#                 visited[nx][ny] = True
def dijkstra(i, j):
    q = []

    distance[i][j] = 0

    heapq.heappush(q, (graph[i][j], i, j))

    while q:
        cost, x, y = heapq.heappop(q)

        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            new_cost = cost + graph[nx][ny]
            if new_cost < distance[nx][ny]:
                distance[nx][ny] = new_cost
                heapq.heappush(q, (distance[nx][ny], nx, ny))


case_count = 1

while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().strip().split())) for __ in range(n)]

    visited = [[False] * n for __ in range(n)]

    distance = [[INF] * n for __ in range(n)]
    dijkstra(0, 0)
    print(f'Problem {case_count}: {distance[n - 1][n - 1]}')
    case_count += 1

