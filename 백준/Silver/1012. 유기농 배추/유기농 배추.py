import sys

def bfs(x, y):
  queue = [[x, y]]
  while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
      c = a + dx[i]
      d = b + dy[i]
      if 0 <= c < N and 0 <= d < M and graph[c][d] == 1:
        graph[c][d] = 0
        queue.append([c, d])


T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]



for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().rstrip().split())
  visited = [[False] * M for _ in range(N)]
  graph = [[0] * M for _ in range(N)]
  result = 0
  for _ in range(K):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[y][x] = 1
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        bfs(i, j)
        graph[i][j] = 0
        result += 1
  print(result)
    