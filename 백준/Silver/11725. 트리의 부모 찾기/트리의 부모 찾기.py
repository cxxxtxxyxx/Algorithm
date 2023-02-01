import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for __ in range(n + 1)]

for __ in range(n - 1):
    i, j = map(int, input().strip().split())

    graph[i].append(j)
    graph[j].append(i)

parents = [0] * (n + 1)

def bfs(v):
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True

    while q:
        node = q.popleft()

        for i in graph[node]:
            if not visited[i]:
                parents[i] = node
                q.append(i)
                visited[i] = True
    return parents

parents = bfs(1)
target = 2
for i in range(2, n + 1):
    print(parents[i])