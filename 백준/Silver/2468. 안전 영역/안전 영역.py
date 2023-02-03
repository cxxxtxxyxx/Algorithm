import sys

input = sys.stdin.readline

n = int(input().strip())

heights = [list(map(int, input().strip().split())) for __ in range(n)]

del_dupl_heights = []

for height in heights:
    del_dupl_heights.extend(height)

del_dupl_heights = list(set(del_dupl_heights))
del_dupl_heights.sort()
# _max -= 1

# i = 1, _max까지 dfs돌리면서 result 저장
result = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(i, j, sink, visited):
    if not 0 <= i < n and 0 <= j < n:
        return 0
    if sink[i][j] == 1:
        return 0
    if visited[i][j] == True:
        return 0
    
    stack = [(i, j)]

    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and sink[nx][ny] == 0:
                stack.append((nx, ny))
                visited[nx][ny] = True

    return 1

for i in range(max(del_dupl_heights) + 1):
    sink = [[0] * n for __ in range(n)]
    for j in range(n):
        for k in range(n):
            if heights[j][k] <= i:
                sink[j][k] = 1
    # print(f'{i} >>>>>> {sink}')
    
    # print(sink)
    total = 0
    visited = [[False] * n for __ in range(n)]
    for j in range(n):
        for k in range(n):
            total += dfs(j, k, sink, visited)
    # print(total)

    result.append(total)
# print(result)
print(max(result))