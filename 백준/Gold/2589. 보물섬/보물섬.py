# import sys
# from collections import deque
# import itertools

# input = sys.stdin.readline

# n, m = map(int, input().strip().split())

# treasures = [list(input().strip()) for __ in range(n)]

# # visited = [[0] * m for __ in range(n)]

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def bfs(i, j):
#     visited = [[-1] * m for __ in range(n)]
#     if visited[i][j] != -1 or treasures[i][j] == 'W':
#         return 0
    
#     visited[i][j] = 0

#     q = deque([(i, j, 0)])

#     while q:
#         px, py, size = q.popleft()

#         for k in range(4):
#             nx = dx[k] + px
#             ny = dy[k] + py

#             if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and treasures[nx][ny] == 'L':
#                 q.append((nx, ny, size + 1))
#                 visited[nx][ny] = min(visited[px][py] + 1, size + 1)

#     return max(itertools.chain(*visited))
# _max = -1
# for i in range(n):
#     for j in range(m):
#         _max = max(bfs(i, j), _max)
# print(_max)


import sys
from collections import deque
import itertools

input = sys.stdin.readline

n, m = map(int, input().strip().split())

treasures = [list(input().strip()) for __ in range(n)]

# visited = [[0] * m for __ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    visited = [[-1] * m for __ in range(n)]
    if visited[i][j] != -1 or treasures[i][j] == 'W':
        return 0
    
    visited[i][j] = 0

    q = deque([(i, j)])

    while q:
        px, py = q.popleft()

        for k in range(4):
            nx = dx[k] + px
            ny = dy[k] + py

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and treasures[nx][ny] == 'L':
                q.append((nx, ny))
                visited[nx][ny] = visited[px][py] + 1

    return max(itertools.chain(*visited))
_max = -1
for i in range(n):
    for j in range(m):
        _max = max(bfs(i, j), _max)
print(_max)