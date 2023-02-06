import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, L, R = map(int, input().strip().split())
populations = [list(map(int, input().strip().split())) for __ in range(N)]

def bfs(i, j):
    q = deque([(i, j)])
    coord = [(i, j)]

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if 0 <= nx < N and 0 <= ny < N and L <= abs(populations[nx][ny] - populations[x][y]) <= R and visited[nx][ny] == False:
                q.append((nx, ny))
                coord.append((nx, ny))
                visited[nx][ny] = True
    return coord

cnt = 0
while True:
    visited = [[False] * N for __ in range(N)]
    flag = False

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                coord = bfs(i, j)

                if len(coord) >= 2:
                    flag = True
                    _sum = sum([populations[x][y] for x, y in coord])

                    for x, y in coord:
                        populations[x][y] = _sum // len(coord)
    if not flag:
        break
    
    cnt += 1

print(cnt)