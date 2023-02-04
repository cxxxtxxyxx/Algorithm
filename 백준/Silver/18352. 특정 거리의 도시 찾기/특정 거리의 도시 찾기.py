import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())

graph = [[] for __ in range(N + 1)]

for __ in range(M):
    i, j = map(int, input().strip().split())

    graph[i].append(j)

result = []
visited = [False] * (N + 1)
def bfs(X):
    q = deque([(X, 0)])

    while q:
        node, w = q.popleft()
        visited[node] = True

        if w == K:
             result.append(node)

        for next_node in graph[node]:
                if visited[next_node] == False:
                    q.append((next_node, w + 1))
                    visited[next_node] = True

bfs(X)
if len(result) == 0:
     print(-1)
else:
    result.sort()
    for res in result:
         print(res)