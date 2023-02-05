import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for __ in range(n)]



dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]



def dfs(i, j):
    stack = [(i, j)]
    if not 0 <= i < n and 0 <= j < m:
        return 0
    
    if visited[i][j] == True:
        return 0
    
    if graph[i][j] == 0:
        return 0
    
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] != 0:
                stack.append((nx, ny))
                visited[nx][ny] = True
    

    return 1


def get_ice(x, y):
    if not 0 <= x < n and 0 <= y < m:
        return 0
    
    result = 0

    for k in range(4):
        nx = dx[k] + x
        ny = dy[k] + y
        if graph[x][y] != 0 and graph[nx][ny] == 0:
            result += 1
    
    return result

cnt = -1
while len(set(list(itertools.chain(*graph)))) != 1:
    result = 0
    ice = [[-1] * m for __ in range(n)]
    visited = [[False] * m for __ in range(n)]

    for i in range(n):
        for j in range(m):
            ice[i][j] = get_ice(i, j)

    for i in range(n):
        for j in range(m):
            if visited[i][j] != True:
                result += dfs(i, j)
    # print(graph)
    for i in range(n):
        for j in range(m):
            graph[i][j] = max(0, graph[i][j] - ice[i][j])
    cnt += 1

    if result >= 2:
        print(cnt)
        exit()

    

print(0)