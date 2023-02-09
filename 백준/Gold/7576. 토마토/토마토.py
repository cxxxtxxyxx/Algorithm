import sys
from collections import deque

def bfs():
  while Q:
    x, y = Q.popleft()
    for i in range(4):
      nx, ny = dx[i] + x, dy[i] + y

      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        Q.append([nx, ny])

Q = deque([])
M, N = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      Q.append([i,j])

bfs()

for vertices in graph:
  for j in vertices:
    if j == 0:
      print(-1)
      exit(0)
  
  res = max(res, max(vertices))
print(res - 1)