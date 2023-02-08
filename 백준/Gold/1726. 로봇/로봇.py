import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
factory = [[0] * (m + 1)] + [[0] + list(map(int, input().strip().split())) for __ in range(n)]

# print(factory)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if factory[i][j] == 1:
            factory[i][j] = -1

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

start_x, start_y, start_direction = map(int, input().strip().split())

dest_x, dest_y, dest_direction = map(int, input().strip().split())

def bfs():
    visited = [[[False] * 5 for _ in range(m + 1)] for __ in range(n + 1)]

    q = deque()
    command_count = 0
    direction = start_direction
    q.append((start_x, start_y, command_count, direction))

    while q:
        x, y, prev_count, prev_direction = q.popleft()

        if (x, y, prev_direction) == (dest_x, dest_y, dest_direction):
            return prev_count
        
        for i in range(1, 4):
            nx = x + dx[prev_direction] * i
            ny = y + dy[prev_direction] * i
            nd = prev_direction


            if nx <= 0 or nx >= n + 1 or ny <= 0 or ny >= m + 1:
                continue

            if visited[nx][ny][nd] == True:
                continue

            if visited[nx][ny][nd] == False and factory[nx][ny] == 0:
                q.append((nx, ny, prev_count + 1, nd))
                visited[nx][ny][nd] = True
            else:
                break

        for k in range(1, 3):
            if prev_direction == 1 or prev_direction == 2:  
                if visited[x][y][k + 2] == False:
                    q.append((x, y, prev_count + 1, k + 2))
                    visited[x][y][k + 2] = True
            else:
                if visited[x][y][k] == False:
                    q.append((x, y, prev_count + 1, k))
                    visited[x][y][k] = True
                


# for fac in factory:
    # print(*fac)
print(bfs())

# for fac in factory:
# print(*fac)
