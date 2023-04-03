import heapq
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

graph = []
heap = []

class Level:
    def __init__(self, level, exp) -> None:
        self.level = level
        self.exp = exp

    def eat(self):
        self.exp += 1
        if self.level == self.exp:
            self.level += 1
            self.exp = 0


baby_level = Level(2, 0)

for i in range(N):
    _input = list(map(int, input().split()))
    graph.append(_input)
    if 9 in _input:
        bx, by = i, _input.index(9)
        heapq.heappush(heap, (0, bx, by))
        graph[bx][by] = 0


def bfs():
    global heap
    global shark_level
    ans = 0

    visited = [[False] * N for __ in range(N)]

    while heap:
        dist, nx, ny = heapq.heappop(heap)

        if 0 < graph[nx][ny] < shark_level.level:
            shark_level.eat()
            graph[nx][ny] = 0

            ans += dist
            dist = 0

            heap = []

            visited = [[False] * N for __ in range(N)]

        for k in range(4):
            px, py = dx[k] + nx, dy[k] + ny

            if not (0 <= px < N and 0 <= py < N):
                continue

            if graph[px][py] <= shark_level.level and visited[px][py] == False:
                heapq.heappush(heap, (dist + 1, px, py))
                visited[px][py] = True

    return ans



shark_level = Level(2, 0)

print(bfs())


