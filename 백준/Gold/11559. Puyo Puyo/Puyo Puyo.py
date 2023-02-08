import sys
from collections import deque


def bfs(i,j, visited):
    result = []
    q = deque()
    q.append((i, j, rotate_graph[i][j]))
    result.append((i, j))
    visited[i][j] = True
    count = 1
    while q:
        flag = False
        # print(q)
        # print(result)
        x, y, prev_color = q.popleft()

        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if not (0 <= nx < 6 and 0 <= ny < 12):
                continue
            if visited[nx][ny] == False and rotate_graph[nx][ny] == prev_color and rotate_graph[nx][ny] != '.':
                count += 1
                q.append((nx, ny, prev_color))
                visited[nx][ny] = True
                result.append((nx, ny))
                flag = True
            # elif visited[nx][ny] == False and rotate_graph[nx][ny] != '.' and rotate_graph[nx][ny] != prev_color:
        if flag == False and count >= 4:
            # print('@@@@@@@@@@@@', result)
            for t_x, t_y in result:
                rotate_graph[t_x][t_y] = '.'
            return 1
            
    return 0





dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

graph = [list(input().strip()) for __ in range(12)]




rotate_graph = [['.'] * 12 for __ in range(6)]
for i in range(12):
    for j in range(6):
        rotate_graph[j][11 - i] = graph[i][j]

cnt = 0
while True:
    coords = []
    for i in range(6):
        for j in range(12):
            if rotate_graph[i][j] != '.':
                coords.append((i, j))

    res = 0
    for i, j in coords:
        visited = [[False] * 12 for __ in range(6)]
        # print(i, j)
        res += bfs(i, j, visited)

    for row in rotate_graph:
        row_cnt = row.count('.')
        if row_cnt != 12:
            for __ in range(row_cnt):
                row.remove('.')
            for __ in range(row_cnt):
                row.append('.')

    
    if res == 0:
        break
    cnt += 1


print(cnt)