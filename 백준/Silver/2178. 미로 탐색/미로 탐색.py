import sys
from collections import deque

N, M = map(int, input().split())
maze = []

for _ in range(N):
  maze.append(list(map(int, list(sys.stdin.readline().rstrip()))))

visited = [[False for col in range(M)] for row in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

Q = deque([(0, 0)])
result = 0

while Q:
  x, y = Q.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]

    if (0 <= nx and nx < N) and (0 <= ny and ny < M):
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        Q.append((nx, ny))

print(maze[N - 1][M - 1])