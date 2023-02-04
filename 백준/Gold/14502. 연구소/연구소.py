import sys
import itertools
import copy

input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = [list(map(int, input().strip().split())) for __ in range(n)]

coords_no_wall = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            coords_no_wall.append((i, j))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
coords = []


def get_coords(idx, res):
    if len(res) == 3:
        # print(res)
        coords.append(list(res))
        return
    
    for i in range(idx, len(coords_no_wall)):
        if not coords_no_wall[i] in res:
            res.append(coords_no_wall[i])
            get_coords(i, res)
            res.pop()
        
    

def dfs(i, j, temp):
    if temp[i][j] == 0 or temp[i][j] == 1:
        return False
    stack = [(i, j)]
    temp[i][j] = 2
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                stack.append((nx, ny))

    return True
_max = 0

# print(coords)
# print(coords_no_wall)
get_coords(0, [])

# print(coords)
for coord in coords:
    temp = copy.deepcopy(graph)
    # print(coord)
    # print(coord)
    for k in coord:
        x, y = k
        # print(x, y)
        temp[x][y] = 1
    # print(temp)
    for i in range(n):
        for j in range(m):
                dfs(i, j, temp)
    # print(list(itertools.chain(*temp)))
    # print(len(list(filter(lambda x: x == 0, list(itertools.chain(*temp))))))
    _max = max(_max, len(list(filter(lambda x: x == 0, list(itertools.chain(*temp))))))
print(_max)