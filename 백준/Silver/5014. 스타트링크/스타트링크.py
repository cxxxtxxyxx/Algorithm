import sys
from collections import deque
input = sys.stdin.readline

"""
F = 최대 층
S = 현재 있는 층
G = 목표 층
U = 올라가는 수
D = 내려가는 수

F S G U D
10 1 10 2 1
6

100 2 1 1 0
use the stairs
"""
F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)

def bfs(S):
    if not 1 <= S <= F:
        return 0
    
    q = deque([S])
    visited[S] = 1
    while q:
        v = q.popleft()

        for k in [v + U, v - D]:
            if 1 <= k <= F and visited[k] == 0:
                q.append(k)
                visited[k] = visited[v] + 1

bfs(S)
if visited[G] == 0:
    print("use the stairs")
else:
    print(visited[G] - 1)

