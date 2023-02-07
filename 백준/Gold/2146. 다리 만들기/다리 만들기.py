# 아이디어
"""


dfs 돌려서 처음 육지 개수 구함
bfs 돌려서 하나씩 채워가면서 dfs 돌렸을 때 기존 - 1 성공
그 육지를 dfs를 돌려서 대륙 개수 == 기존 - 1 => 성공
"""

import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

graph = [list(map(int, input().strip().split())) for __ in range(n)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * n for __ in range(n)]

def dfs(i, j):
    global cnt
    stack = [(i, j)]
    if visited[i][j] == True:
        return False
    
    if graph[i][j] == 0:
        return False
    
    visited[i][j] = True

    while stack:
        x, y = stack.pop()
        visited[x][y] = True
        graph[x][y] = cnt
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] == 1:
                stack.append((nx, ny))
                visited[nx][ny] = True
                
    return True

def bfs(v):
    global res
    q = deque()
    dist = [[-1] * n for __ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == v:
                q.append((i, j))
                dist[i][j] = 0
    
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            
            if graph[nx][ny] > 0 and graph[nx][ny] != v:
                res = min(res, dist[x][y])
                return
            
            if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

            

res = sys.maxsize
cnt = 2
for i in range(n):
    for j in range(n):
        if visited[i][j] == False and dfs(i, j) == True:
            cnt += 1
for i in range(2, cnt):
    bfs(i)

print(res)
