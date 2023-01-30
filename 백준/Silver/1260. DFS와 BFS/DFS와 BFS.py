import sys
from collections import deque

# def dfs(root):
#   stack = []
#   stack.append(root)
#   while stack:
#     node = stack.pop()
#     if visited[node] == False:
#       visited[node] = True
#     print(node)
#     for i in graph[node]:
#       if visited[i] == False:
#         stack.append(i)
#     if not False in visited:
#       break

# def dfsR(root):
#   if visited[root] == True:
#     return
#   visited[root] = True
#   print(root)
#   for i in graph[root]:
#     dfsR(i)


def dfs(graph, start):
  visited = []
  stack = []
  stack.append(start)
  while stack:
    now = stack.pop()
    if now not in visited:
      visited.append(now)
      stack.extend(graph[now])
  
  print(*visited)

# visited = []
# def dfsR(graph, start):
  
#   if start in visited:
#     return
#   visited.append(start)
#   print(start, end=' ')
#   for now in graph[start]:
#     dfsR(graph, now)

def bfs(graph, start):
  visited = []
  Queue = deque([start])

  while Queue:
    now = Queue.popleft()
    if now not in visited:
      visited.append(now)
      Queue.extend(graph[now])
  
  print(*visited)



N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(N + 1)]
# visited = [False for _ in range(N + 1)]
# visited[0] = True

for _ in range(M):
  v1, v2 = map(int, sys.stdin.readline().rstrip().split())
  graph[v1].append(v2)
  graph[v2].append(v1)

for vertices in graph:
  vertices.sort(reverse=True)


dfs(graph, V)
# dfsR(graph, V)
for vertices in graph:
  vertices.sort()
bfs(graph, V)
