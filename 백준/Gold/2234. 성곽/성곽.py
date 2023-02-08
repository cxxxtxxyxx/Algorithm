import sys
from collections import deque
input = sys.stdin.readline


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 이진수 변환 함수 (인자 10진수)
# 남 동 북 서 순서
def get_wall(num):
    res = deque()
    while num > 0:
        res.append(num % 2)
        num //= 2

    res.reverse()

    while len(res) < 4:
        res.appendleft(0)
    return list(res)


m, n = map(int, input().strip().split())


graph = [list(map(int, input().strip().split())) for __ in range(n)]

visited = [[False] * m for __ in range(n)]
room_num = 1
for i in range(n):
    for j in range(m):
        graph[i][j] = bin(graph[i][j])[2:]
        graph[i][j] = ['0' * (4 - len(graph[i][j])) + graph[i][j], room_num]

def bfs(i, j, room_num):
    q = deque([(i, j)])
    if visited[i][j] == True:
        return [0, 0]
    visited[i][j] = True
    room_size = 1
    graph[i][j][1] = room_num
    while q:
        x, y = q.popleft()
        for idx, k in enumerate(graph[x][y][0]):
            if k == '0':
                nx = dx[idx] + x
                ny = dy[idx] + y

                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny][1] = room_num
                    room_size += 1

    return [1, room_size]

def boundary_bfs(i, j):
    boundary_set = set()
    num = graph[i][j][1]
    area_size = 0
    visited[i][j] = True
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] == True:
                continue
            if graph[nx][ny][1] == num:
                visited[nx][ny] = True
                q.append((nx,ny))

            else:
                boundary_num = graph[nx][ny][1]
                if boundary_num not in boundary_set:
                    boundary_set.add(boundary_num)
                    area_size = max(area_size, room_info[boundary_num])
    return room_info[num] + area_size


room_cnt = 0
room_max_size = 0
room_info = {}
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            cnt, size = bfs(i, j, room_num)
            room_cnt += cnt
            room_max_size = max(room_max_size, size)
            room_info[room_num] = size
            room_num += 1


# coords = []

# for i in range(n):
#     for j in range(m):
#         for idx, k in enumerate(graph[i][j]):
#             if k == '1':
#                 coords.append((i, j, idx))


# 각 coord를 돌면서 해당 부분을 부수고 dfs돌림
# 그래프 복사 x

# broken_visited = [[[0] for _ in range(m)] for __ in range(n)]
# broken_max_size = 0
# for coord in coords:
#     visited = [[False] * m for __ in range(n)]
#     x, y, d = coord
#     graph[x][y] = graph[x][y][:d] + '0' + graph[x][y][d + 1:]
#     for i in range(n):
#         for j in range(m):
#             max_size = bfs(i, j, room_num)[1]
#             broken_max_size = max(broken_max_size, max_size)
#     graph[x][y] = graph[x][y][:d] + '1' + graph[x][y][d + 1:]

area = 0
visited = [[False] * m for __ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            area = max(area, boundary_bfs(i, j))

# print(graph)
# print(room_info)
print(room_cnt)
print(room_max_size)
print(area)