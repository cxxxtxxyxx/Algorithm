import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
x, y = map(int, input().strip().split())
m = int(input())

graph = [[] * (n + 1) for __ in range(n + 1)]


for __ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [-1] * (n + 1)

def bfs(start):
    q = deque([(start, 1)])

    visited[start] = 1

    while q:
        n, w = q.popleft()

        for node in graph[n]:
            if visited[node] == -1:
                visited[node] = w + 1
                q.append((node, visited[node]))


bfs(x)
if visited[y] == -1:
    print(visited[y])
else:
    print(visited[y] - 1)
    