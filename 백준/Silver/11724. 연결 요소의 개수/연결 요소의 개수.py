import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

graph = [[] for __ in range(n + 1)]

for __ in range(m):
    i, j = map(int, input().split())

    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (n + 1)
visited[0] = True

def dfs(v):

    visited[v] = True

    for node in graph[v]:
        if visited[node] == False:
            dfs(node)

    return 1

result = 0
while not all(visited):
   v = visited.index(False)
   result += dfs(v)

print(result)