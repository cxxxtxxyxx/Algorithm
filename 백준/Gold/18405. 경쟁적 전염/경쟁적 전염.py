# 아이디어
"""
n * n 그래프
1 ~ k 바이러스 종류
S초 지난 후 X, Y 존재 바이러스 종류 출력
"""
# 자료구조, 알고리즘
"""
BFS사용하기
"""

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [[0] * (n + 1)] + [[0] + list(map(int, input().strip().split())) for __ in range(n)]

s, x, y = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

virus = []

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))

virus.sort()

def bfs(s, x, y):
    q = deque(virus)
    cnt = 0

    while q:
        if cnt == s:
            break
        length = len(q)
        for __ in range(length):
            prev, i, j = q.popleft()

            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                if 1 <= nx < n + 1 and 1 <= ny < n + 1:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = prev
                        q.append((graph[nx][ny], nx, ny))

        cnt += 1
    return graph[x][y]

print(bfs(s, x, y))