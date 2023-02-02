# 아이디어
"""
가로 세로 대각선까지 dfs를 돌려서 갯수를 더한다
이중포문 dfs 재귀 돌리기
"""

# 시간복잡도
"""

"""

# 자료구조 & 알고리즘
"""
그래프 => 이차원배열
visited => 이차원배열
"""

import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1, -1, 1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

def dfs(i, j):
    if not (0 <= i < h and 0 <= j < w):
        return 0
    if graph[i][j] == 0:
        return 0
    
    if visited[i][j] == True:
        return 0
    
    visited[i][j] = True
    
    for k in range(8):
        x = dx[k] + i
        y = dy[k] + j
        if 0 <= x < h and 0 <= y < w and visited[x][y] == False:
            dfs(x, y)

    return 1

while True:
    w, h = map(int, input().strip().split())

    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for __ in range(h)]

    visited = [[False] * w for __ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            cnt += dfs(i, j)

    print(cnt)