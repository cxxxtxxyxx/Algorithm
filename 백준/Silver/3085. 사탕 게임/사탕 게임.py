import sys

input = sys.stdin.readline

# 빨 C, 파 P, 초 Z, 노 Y

N = int(input())

bomboni = [list(input().strip()) for __ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


_max = 0


def getAllCount():
    global _max

    for i in range(N):
        count = 1
        for j in range(N - 1):
            if bomboni[i][j] == bomboni[i][j + 1]:
                count += 1
                _max = max(_max,count)
            else: 
                count = 1

    for i in range(N):
        count = 1
        for j in range(N - 1):
            if bomboni[j][i] == bomboni[j + 1][i]:
                count += 1
                _max = max(_max,count)
            else: 
                count = 1

for i in range(N):
    for j in range(N):
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j

            if not (0 <= nx < N and 0 <= ny < N):
                continue

            bomboni[i][j], bomboni[nx][ny] = bomboni[nx][ny], bomboni[i][j]

            getAllCount()
            
            bomboni[nx][ny], bomboni[i][j] = bomboni[i][j], bomboni[nx][ny]

print(_max)