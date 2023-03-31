import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().strip().split())

graph = [list(deque() for _ in range(N)) for __ in range(N)]


fireball_coords = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().strip().split())
    graph[r - 1][c - 1].append((m, s, d))
    fireball_coords.append((r - 1, c - 1))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(K):
    for __ in range(len(fireball_coords)):
        r, c = fireball_coords.popleft()
        m, s, d = graph[r][c].popleft()

        nx, ny = (r + (dx[d] * s)) % N, (c + (dy[d] * s)) % N

        graph[nx][ny].append((m, s, d))
    
    for i in range(N):
        for j in range(N):
            total = len(graph[i][j])

            if total >= 2:
                tm, ts, td = 0, 0, []
                odd, even = 0, 0
                while len(graph[i][j]) != 0:
                    pm, ps, pd = graph[i][j].popleft()

                    tm += pm
                    ts += ps
                    
                    if pd % 2 == 1:
                        odd += 1
                    else:
                        even += 1

                tm //= 5

                if tm == 0:
                    continue

                ts //= total

                if odd == total or even == total:
                    td = [0, 2, 4, 6]
                else:
                    td = [1, 3, 5, 7]

                for k in range(4):
                    graph[i][j].append((tm, ts, td[k]))
                    fireball_coords.append((i, j))

            else:
                if total == 1:
                    fireball_coords.append((i, j))

ans = 0
for i in range(N):
    for j in range(N):
        ans += sum(g[0] for g in graph[i][j])

print(ans)





