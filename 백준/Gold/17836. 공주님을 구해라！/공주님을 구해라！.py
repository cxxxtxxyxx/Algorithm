import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())

graph = [list(map(int, input().split())) for __ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    visited = [[[0, 0] for __ in range(M)] for __ in range(N)]
    
    q.append((0, 0, 0))


    while q:
        px, py, weapon = q.popleft()

        for k in range(4):
            nx, ny = dx[k] + px, dy[k] + py

            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if visited[nx][ny][weapon] != 0:
                continue
            
            if graph[nx][ny] == 0:
                visited[nx][ny][weapon] = visited[px][py][weapon] + 1
                q.append((nx, ny, weapon))

            elif graph[nx][ny] == 1:
                if weapon == 1:
                    visited[nx][ny][1] = visited[px][py][1] + 1
                    q.append((nx, ny, weapon))
                else:
                    continue
            elif graph[nx][ny] == 2:
                visited[nx][ny][1] = visited[px][py][0] + 1
                q.append((nx, ny, 1))
    if visited[N - 1][M - 1][0] == 0 and visited[N - 1][M - 1][1] == 0:
        return "Fail"
    
    if visited[N - 1][M - 1][0] > T and visited[N - 1][M - 1][1] > T:
        return "Fail"
    
    if visited[N - 1][M - 1][0] == 0 and visited[N - 1][M - 1][1] <= T:
        return visited[N - 1][M - 1][1]
    
    if visited[N - 1][M - 1][1] == 0 and visited[N - 1][M - 1][0] <= T:
        return visited[N - 1][M - 1][0]
    
    return min(visited[N - 1][M - 1][0], visited[N - 1][M - 1][1])


time = bfs()

if time == 0:
    print("Fail")
else:
    print(time)