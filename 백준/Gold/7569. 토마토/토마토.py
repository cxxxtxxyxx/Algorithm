# 아이디어
"""
bfs 돌리기
위 아래 왼쪽 오른쪽 앞 뒤
1 => 익은 토마토
0 => 익지 않은 토마토
-1 => 토마토 없음
"""
# 자료구조 알고리즘
"""
- 토마토 박스 => 3차원배열
- visited => 3차원 배열
- 
"""

import sys
from collections import deque
import itertools

input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = [[list(map(int, input().split())) for __ in range(N)] for _ in range(H)]

cnt = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j] == 0:
                cnt += 1
if cnt == 0:
    print(0)
    exit()


visited = [[[False] * M for __ in range(N)] for __ in range(H)]
# graph[h][i][j] => 높이 h 세로 i 가로 j

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    q = deque(coords)

    while q:
        length = len(q)
        for __ in range(length):
            z, x, y = q.popleft()
            for k in range(6):
                nz = dz[k] + z
                nx = dx[k] + x
                ny = dy[k] + y
                if 0 <= nz < H and 0 <= ny < M and 0 <= nx < N and graph[nz][nx][ny] == 0:
                    q.append((nz, nx, ny))
                    graph[nz][nx][ny] = graph[z][x][y] + 1
        

    # if not 0 <= h < H and 0 <= n < N and 0 <= m < m:
    #     return 0
    
    # if visited[h][n][m] == True:
    #     return 0
    
    # if graph[h][n][m] == -1:
    #     return 0
    
    
    # visited[h][n][m] = True
    # graph[h][n][m] = 1
    
    
    
    # return cnt

total = 0
coords = []
for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j] == 1:
                coords.append((h, i, j))
bfs()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j] == 0:
                print(-1)
                exit()




print(max(list(itertools.chain(*(list(itertools.chain(*graph)))))) - 1)