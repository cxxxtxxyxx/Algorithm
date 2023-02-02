# # 아이디어
# """
# 국경선 공유 두 나라 L이상 R이하라면, 국경선을 오늘 하루 연다
# 국경선 공유 -> 하루 연합
# 국경선 공유 각 칸 인구수 -> 연합 인구 수 / 연합 칸 개수 소수점 버림
# 연합 해체 국경선 닫음
# 인구이동이 며칠 발생했는지 구하시오
# """
# # 시간복잡도
# """

# """
# # 자료구조, 알고리즘
# """

# """

# import sys
# import itertools

# input = sys.stdin.readline

# N, L, R = map(int, input().strip().split())

# populations = [list(map(int, input().strip().split())) for __ in range(N)]


# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# count = 0

# def dfs(i, j, graph, visited):
#     if not 0 <= i < N and 0 <= j < N:
#         return 0
    
#     if visited[i][j] == True:
#         return 0
#     result = populations[i][j]
#     visited[i][j] = True
#     # populations[i][j] = int((population + populations[i][j]) / 2)

#     # for coord in graph[i][j]:
#     #     x, y = coord
#     #     for k in range(4):
#     #         nx, ny = dx[k] + x, dy[k] + y
#     #         if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
#     #             popul = int((population + populations[nx][ny]) / 2)
#     #             print(i, j, nx, ny)
#     #             print(population, populations[nx][ny], popul)
#     #             populations[x][y] = populations[nx][ny] = popul
#     #             dfs(nx, ny, popul, graph, visited)
#     #             visited[nx][ny] = True
#     for coord in graph[i][j]:
#         print(graph[i][j])
#         x, y = coord
#         if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
#             print(x, y)
#             result += dfs(x, y, graph, visited)
#             visited[x][y] = True
            

#     return result
    


# stack = []
# while True:
#     print(f'POPOPOPOP>>>> {populations}')
#     # graph에 국경선 열린 곳들을 저장
#     graph = [[[] for __ in range(N)] for __ in range(N)]
#     # graph = {}
#     visited = [[False] * N for __ in range(N)]
#     print(f'start populations> {populations}')
#     # 국경선 저장
#     for i in range(N):
#         for j in range(N):
#             for k in range(4):
#                 nx = dx[k] + i
#                 ny = dy[k] + j
#                 # if 0 <= nx < N and 0 <= ny < N:
#                 #     if L <= max(populations[nx][ny], populations[i][j]) - min(populations[nx][ny], populations[i][j]) <= R:
#                 #         if not (nx, ny) in graph[(i, j)]:
#                 #             graph[(i, j)].append((nx, ny))
#                 #         if not (i, j) in graph[(nx, ny)]:
#                 #             graph[(nx, ny)].append((i, j))
                
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if L <= max(populations[nx][ny], populations[i][j]) - min(populations[nx][ny], populations[i][j]) <= R:
#                         print(f'(nx, ny), (i, j) => ({nx}, {ny}), ({i}, {j})')

#                         if not (nx, ny) in stack:
#                             stack.append((nx, ny))
#                         if not (i, j) in stack:
#                             stack.append((i, j))
#                         if not (nx, ny) in graph[i][j]:
#                             print("****************")
#                             print(f'(nx, ny), (i, j) => ({nx}, {ny}), ({i}, {j})')
#                             graph[i][j].append((nx, ny))

#                         if not (i, j) in graph[nx][ny]:
#                             print("################")
#                             print(f'(nx, ny), (i, j) => ({nx}, {ny}), ({i}, {j})')
#                             graph[nx][ny].append((i, j))


#     for i in range(N):
#         for j in range(N):
#             print(f'*** graph[{i}][{j}] {graph[i][j]}')

#     # if graph 길이 0 => 열린 곳 없음 => return
#     if len(list(itertools.chain(*list(itertools.chain(*graph))))) == 0:
#         print(f'populations> {populations}')
#         print(f'graph> {graph}')
#         break

#     # 하루 늘려줌
#     count += 1
#     total = 0
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j] == False:
#                 dfs(i, j, graph, visited)
#             for coord in stack:
#                 x, y = coord
#                 total += populations[x][y]
#             print(f'TTTTTTTTTTTTT => {total} {stack}')
#             while stack:
#                 x, y = stack.pop()
#                 populations[x][y] = int(total / len(graph))

# print(count)


import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().strip().split())

populations = [list(map(int, input().strip().split())) for __ in range(N)]

count = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    q = deque([(i, j)])

    coord = [(i, j)]

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and L <= abs(populations[nx][ny] - populations[x][y]) <= R:
                visited[nx][ny] = True
                q.append((nx, ny))
                coord.append((nx, ny))

    return coord

while True:
    visited = [[False] * N for __ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                coord = bfs(i, j)
                if len(coord) > 1:
                    flag = True
                    _sum = sum([populations[x][y] for x, y in coord]) // len(coord)

                    for x, y in coord:
                        populations[x][y] = _sum
    
    if not flag:
        break
    count += 1

print(count)