import sys

input = sys.stdin.readline


map_size = int(input())

graph = []

for __ in range(map_size):
    graph.append(list(map(int, list(input().strip()))))


"""
방문 수 체크 후 리턴
이중포문으로 모두 돌기
"""

def dfs(x, y, visited):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    stack = [(x, y)]
    visited.add((x, y))
    
    answer = 1

    while stack:
        px, py = stack.pop()

        for k in range(4):
            nx = dx[k] + px
            ny = dy[k] + py

            if not (0 <= nx < map_size and 0 <= ny < map_size):
                continue

            if graph[nx][ny] == 0:
                continue

            if (nx, ny) not in visited:
                stack.append((nx, ny))
                visited.add((nx, ny))
                answer += 1

    return answer

answer = []
visited = set()
for i in range(map_size):
    for j in range(map_size):
        if graph[i][j] == 1 and (i, j) not in visited:
            answer.append(dfs(i, j, visited))

answer.sort()

print(len(answer))
for a in answer:
    print(a)