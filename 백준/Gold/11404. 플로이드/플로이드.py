import sys
import copy

INF = sys.maxsize
input = sys.stdin.readline


n = int(input().strip())
m = int(input().strip())
graph = [[INF] * n for __ in range(n)]

for __ in range(m):
    a, b, c = map(int, input().strip().split())
    if c < graph[a - 1][b - 1]:
        graph[a - 1][b - 1] = c

for i in range(n):
    graph[i][i] = 0

dist = copy.deepcopy(graph)


def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                

floyd()

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            dist[i][j] = 0
for distance in dist:
    print(*distance)