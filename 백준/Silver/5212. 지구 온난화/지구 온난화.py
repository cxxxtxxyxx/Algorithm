import sys

input = sys.stdin.readline

R, C = map(int, input().strip().split())

island = [list(input().strip()) for __ in range(R)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(R):
    for j in range(C):
        if island[i][j] == 'X':
            count = 0
            for k in range(4):
                nx, ny = dx[k] + i, dy[k] + j
                
                if not (0 <= nx < R and 0 <= ny < C):
                    count += 1
                    continue

                if island[nx][ny] == '.':
                    count += 1

            if count >= 3:
                island[i][j] = ','


for i in range(R):
    for j in range(C):
        if island[i][j] == ',':
            island[i][j] = '.'

sx, bx, sy, by = R + 1, -1, C + 1, -1
# x 가장 작고, y 가장 큰 것
# x 가장 크고, y 가장 작은 것
coord = []
result = []
for j in range(C):
    count = 0
    for i in range(R):
        if island[i][j] == 'X':
            sx = min(sx, i)
            bx = max(bx, i)
            sy = min(sy, j)
            by = max(by, j)




for i in range(sx, bx + 1):
    for j in range(sy, by + 1):
        print(island[i][j], end="")
    print()