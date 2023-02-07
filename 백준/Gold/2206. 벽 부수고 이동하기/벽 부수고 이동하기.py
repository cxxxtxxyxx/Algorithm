# bfs 사용하기
"""
0,0에서 시작, 벽 뿌쑨거 False
네방향으로 bfs 돌림
if 다음 방향이 0 이면 이전 + 1
elif 다음 방향이 -1 and 뿌수기 True이면 continue
else 다음 방향이 -1 and 뿌수기 False라면 다음 방향 0으로 만든 뒤 copy해서 q에 넣어줌
"""

import sys
import itertools
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, list(input().strip()))) for __ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

# wall = []
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 1:
#             graph[i][j] = -1
#             wall.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))

    while q:
        a, b, c = q.popleft()
        if a == n - 1 and b == m - 1:
            return visited[a][b][c]
        for k in range(4):
            nx = dx[k] + a
            ny = dy[k] + b

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                q.append((nx, ny, c))
            elif graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                q.append((nx, ny, 1))
            else:
                continue
            

    return -1


print(bfs(0, 0, 0))