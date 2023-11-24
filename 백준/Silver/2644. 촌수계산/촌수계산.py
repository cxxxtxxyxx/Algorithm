import sys
from collections import deque

input = sys.stdin.readline

people_size = int(input())
x, y = map(int, input().split())
m = int(input())

graph = [[] for __ in range(people_size + 1)]

for __ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


"""
촌수 계산
bfs
x -> y로 가는 최단 거리
"""

def bfs(start, end):
    visited = [False] * (people_size + 1)
    q = deque([(start, 0)])
    visited[start] = True

    while q:
        next, dist = q.popleft()
        if next == end:
            return dist

        for node in graph[next]:
            if not visited[node]:
                q.append((node, dist + 1))
                visited[node] = True

    return -1

print(bfs(x, y))