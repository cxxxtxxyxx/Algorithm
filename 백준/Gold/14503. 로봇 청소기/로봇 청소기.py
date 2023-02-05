"""
1. 현재 위치 청소
2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 탐색
    a. 왼쪽 방향에 청소하지 않은 공간 존재할 시 그 방향으로 회전한 다음 한칸 전진 후 1번부터 다시
    b. 청소 공간 없다면 그 방향으로 회전하고 2번으로 돌아감
    c. 네 방향 모두 청소 ok or 벽인 경우 바라보는 방향 유지한 채 한칸 후진 후 2번으로
    d. 네방향 청소 ok or (벽 and 뒤쪽 방향 벽) => 작동 멈춤

"""

import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

visited = [[True] * M for __ in range(N)]
graph = [list(map(int, input().split())) for __ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            visited[i][j] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


cnt = 0

def find_dfs(x, y):
    if not 0 <= x < N and 0 <= y < M:
        return False
    if graph[x][y] == 2:
        return False
    
    if visited[x][y] == True:
        return False
    
    visited[nx][ny] = True
    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny] == False:
            find_dfs(nx, ny)
            visited[nx][ny] = True

    return True


def dfs(r, c, d):
    
    global cnt
    if graph[r][c] == 0:
        cnt += 1
        graph[r][c] = 2
    flag = False
    for i in range(4):
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        
        if graph[nx][ny] == 0:
            dfs(nx, ny, (d + 3) % 4)
            return
        
        d = (d + 3) % 4
        

    nx = r + dx[(d + 2) % 4]
    ny = c + dy[(d + 2) % 4]

    if graph[nx][ny] == 1:
        print(cnt)
        exit()
    dfs(nx, ny, d)

dfs(r, c, d)