import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for __ in range(N + 1)]

_max = 0
for __ in range(M):
    a, b, c = map(int, input().split())
    _max = max(c, _max)
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

fac_1, fac_2 = map(int, input().split())

def bfs(val, visited):
    q = deque()
    q.append(fac_1)
    visited[fac_1] == True

    while q:
        now = q.popleft()

        if now == fac_2:
            return True
        
        for next, weight in graph[now]:
            if visited[next] == False and val <= weight:
                q.append(next)
                visited[next] = True

    return False

def binary_search():
    start = 1
    end = _max
    res = 0
    while start <= end:
        visited = [0 for __ in range(N + 1)]

        mid = (start + end) // 2

        if bfs(mid, visited):
            start = mid + 1
            res = mid
        else:
            end = mid - 1
    return res


print(binary_search())