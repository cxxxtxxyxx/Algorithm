import sys
from itertools import chain
INF = sys.maxsize
input = sys.stdin.readline

v, e = map(int, input().split())

dist = [[INF] * (v + 1) for __ in range(v + 1)]


for __ in range(e):
    a, b, d = map(int, input().split())
    dist[a][b] = d


for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

result = min(list(chain(dist[i][i] for i in range(1, v + 1))))

if result == INF:
    print(-1)
else:
    print(result)