import sys

input = sys.stdin.readline

N = int(input())

graph = [[False] * 101 for __ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for __ in range(N):
    y, x, d, g = map(int, input().split())

    graph[x][y] = True

    clist = [d]
    for j in range(g):
        tmp = []
        for k in range(len(clist)):
            res = (clist[-k - 1] + 1) % 4
            tmp.append(res)
        clist.extend(tmp)
    for direct in clist:
        x += dx[direct]
        y += dy[direct]

        if not (0 <= x < 101 and 0 <= y < 101):
            continue

        graph[x][y] = True

ans = 0

for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            ans += 1

print(ans)

