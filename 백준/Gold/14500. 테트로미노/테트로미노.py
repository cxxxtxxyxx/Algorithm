import sys

input = sys.stdin.readline


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for __ in range(N)]

_max = 0
_max_val = max(map(max, matrix))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def getTotal(i, j, step, total):
    global _max

    if total + _max_val * (4 - step) <= _max:
        return
    
    if step == 4:
        _max = max(_max, total)
        return
    

    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if visited[nx][ny] == False:

            if step == 2:
                visited[nx][ny] = True
                getTotal(i, j, step + 1, total + matrix[nx][ny])
                visited[nx][ny] = False

            visited[nx][ny] = True
            getTotal(nx, ny, step + 1, total + matrix[nx][ny])
            visited[nx][ny] = False
            



visited = [[False] * M for __ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        getTotal(i, j, 1, matrix[i][j])
        visited[i][j] = False


print(_max)