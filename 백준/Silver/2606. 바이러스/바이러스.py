import sys

input = sys.stdin.readline

vertex = int(input())

edge = int(input())

graph = [[0] * (vertex + 1) for __ in range(vertex + 1)]

for __ in range(edge):
    i, j = map(int, input().split())

    graph[i].append(j)
    graph[j].append(i)


visited = [False] * (vertex + 1)
visited[0] = True

def dfs(v):
    visited[v] = True
    for node in graph[v]:
        if visited[node] == False:
            dfs(node)

dfs(1)

print(len(list(filter(lambda x: x == True, visited))) - 2)