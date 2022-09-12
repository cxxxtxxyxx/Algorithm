import sys
from collections import deque

def bfs(start, end):
  Q = deque([start])
  while Q:
    now = Q.popleft()
    if now == end:
      print(dist[now])
      break
    for nx in [now - 1, now + 1, now * 2]:
      if 0 <= nx <= MAX and not dist[nx]:
        dist[nx] = dist[now] + 1
        Q.append(nx)
    

N, K = map(int, sys.stdin.readline().rstrip().split())

MAX = 10 ** 5
dist = [0] * (MAX + 1)



bfs(N, K)