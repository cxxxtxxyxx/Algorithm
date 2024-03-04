import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())

wood = [list(map(int, input().strip().split())) for __ in range(N)]

result = 0

visited = [[False] * M for __ in range(N)]

def backtracking(x, y, _sum):

    global result

    if y == M:
        x += 1
        y = 0
    
    if x == N and y == 0:
        result = max(result, _sum)
        return
    
    if visited[x][y] == False:
        if x + 1 < N and y - 1 >= 0 and visited[x + 1][y] == False and visited[x][y - 1] == False:
            visited[x][y] = True
            visited[x + 1][y] = True
            visited[x][y - 1] = True
            backtracking(
                x, 
                y + 1, 
                _sum + wood[x][y] * 2 + wood[x + 1][y] + wood[x][y - 1]
            )
            visited[x][y] = False
            visited[x + 1][y] = False
            visited[x][y - 1] = False

        if x - 1 >= 0 and y - 1 >= 0 and visited[x - 1][y] == False and visited[x][y - 1] == False:
            visited[x][y] = True
            visited[x - 1][y] = True
            visited[x][y - 1] = True
            backtracking(
                x, 
                y + 1, 
                _sum + wood[x][y] * 2 + wood[x - 1][y] + wood[x][y - 1]
            )
            visited[x][y] = False
            visited[x - 1][y] = False
            visited[x][y - 1] = False
        
        if x - 1 >= 0 and y + 1 < M and visited[x - 1][y] == False and visited[x][y + 1] == False:
            visited[x][y] = True
            visited[x - 1][y] = True
            visited[x][y + 1] = True
            backtracking(
                x, 
                y + 1, 
                _sum + wood[x][y] * 2 + wood[x - 1][y] + wood[x][y + 1]
            )
            visited[x][y] = False
            visited[x - 1][y] = False
            visited[x][y + 1] = False
        
        if x + 1 < N and y + 1 < M and visited[x + 1][y] == False and visited[x][y + 1] == False:
            visited[x][y] = True
            visited[x + 1][y] = True
            visited[x][y + 1] = True
            backtracking(
                x, 
                y + 1, 
                _sum + wood[x][y] * 2 + wood[x + 1][y] + wood[x][y + 1]
            )
            visited[x][y] = False
            visited[x + 1][y] = False
            visited[x][y + 1] = False
        
        backtracking(x, y + 1, _sum)
    else:
        backtracking(x, y + 1, _sum)

        
backtracking(0, 0, 0)
print(result)