import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for __ in range(N + 1)]


for __ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(graph, start):
    q = deque()
    q.append(start)
    _sum = [0] * (N + 1)
    visited = [False] * (N + 1)
    visited[start] = True

    while q:
        px = q.popleft()

        for x in graph[px]:
            if visited[x] == False:
                _sum[x] = _sum[px] + 1
                visited[x] = True
                q.append(x)

    return sum(_sum)

result = []
for i in range(1, N + 1):
    result.append(bfs(graph, i))

print(result.index(min(result)) + 1)

