import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for __ in range(n + 1)]

for __ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

def bfs(v):
    q = deque([v])
    visited[v] = 1
    
    if len(graph[v]) == 0:
        return 0
    # print("--------------------")
    
    while q:
        node = q.popleft()
        # print(graph)
        # print(visited)

        for next_node in graph[node]:
            if visited[next_node] == 0:
                q.append(next_node)
                visited[next_node] = visited[node] + 1

bfs(1)

print(len(list(filter(lambda x: 2 <= x <= 3, visited))))