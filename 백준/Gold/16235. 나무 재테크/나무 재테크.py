import heapq
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for __ in range(N)]
graph = [[5] * N for __ in range(N)]
tree = [[deque() for __ in range(N)] for __ in range(N)]
deadtree = [[list() for __ in range(N)] for __ in range(N)]



for __ in range(M):
    x, y, age = map(int, input().split())
    
    tree[x - 1][y - 1].append(age)

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

for __ in range(K):

    for i in range(N):
        for j in range(N):
            _len = len(tree[i][j])
            for k in range(_len):
                if graph[i][j] < tree[i][j][k]:
                    for _ in range(k, _len):
                        deadtree[i][j].append(tree[i][j].pop())
                    break
                else:
                    graph[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1

    for i in range(N):
        for j in range(N):
            while deadtree[i][j]:
                graph[i][j] += deadtree[i][j].pop() // 2

    
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0:
                    for l in range(8):
                        nx, ny = dx[l] + i, dy[l] + j

                        if not (0 <= nx < N and 0 <= ny < N):
                            continue

                        tree[nx][ny].appendleft(1)
            
            graph[i][j] += A[i][j]
        

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])

print(ans)