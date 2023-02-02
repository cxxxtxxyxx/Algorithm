import sys

input = sys.stdin.readline

n = int(input())

graph = [list(input().strip()) for __ in range(n)]
visited = [[False] * n for __ in range(n)]
visited_blind = [[False] * n for __ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(i, j, color, is_blind):
    if not (0 <= i < n and 0 <= j < n):
        return 0
    
    stack = [(i, j, color)]


    if is_blind:
        if visited_blind[i][j] == True:
            return 0
        
        while stack:
            visited_blind[i][j] = True
            x, y, prev_color = stack.pop()
            for k in range(4):
                nx = dx[k] + x
                ny = dy[k] + y

                if 0 <= nx < n and 0 <= ny < n and visited_blind[nx][ny] == False:
                    if prev_color == 'R' or prev_color == 'G':
                        if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                            stack.append((nx, ny, graph[nx][ny]))
                            visited_blind[nx][ny] = True
                    else:
                        if graph[nx][ny] == 'B':
                            stack.append((nx, ny, graph[nx][ny]))
                            visited_blind[nx][ny] = True
        return 1
        

            


    else:
        if visited[i][j] == True:
            return 0
        
        while stack:
            visited[i][j] = True
            x, y, prev_color = stack.pop()
            for k in range(4):
                nx = dx[k] + x
                ny = dy[k] + y

                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] == color:
                    dfs(nx, ny, color, False)
        return 1
        
     


total_normal = 0
total_blind = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            total_normal += dfs(i, j, graph[i][j], False)
        if visited_blind[i][j] == False:
            total_blind += dfs(i, j, graph[i][j], True)

print(total_normal, total_blind)