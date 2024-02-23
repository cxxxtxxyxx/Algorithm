import sys

input = sys.stdin.readline

N, M = map(int, input().split())


graph = [list(map(int, input().split())) for __ in range(N)]
visited = [[False] * M for __ in range(N)]

result = 0

def backtracking(x, y, _sum):

    global result

    if y == M:
        x += 1
        y = 0

    if x == N:
        result = max(result, _sum)
        return
    
    if not visited[x][y]:
        """
        ㅁㅁ
        ㅁ
        """
        if x + 1 < N and y + 1 < M and not visited[x + 1][y] and not visited[x][y + 1]:
            visited[x][y] = True
            visited[x + 1][y] = True
            visited[x][y + 1] = True
            backtracking(
                x, y + 1, _sum + 2 * graph[x][y] + graph[x + 1][y] + graph[x][y + 1]
            )
            visited[x][y] = False
            visited[x + 1][y] = False
            visited[x][y + 1] = False

        """
        ㅁㅁ
          ㅁ
        """
        if x + 1 < N and y - 1 >= 0 and not visited[x + 1][y] and not visited[x][y - 1]:
            visited[x][y] = True
            visited[x + 1][y] = True
            visited[x][y - 1] = True
            backtracking(
                x, y + 1, _sum + 2 * graph[x][y] + graph[x + 1][y] + graph[x][y - 1]
            )
            visited[x][y] = False
            visited[x + 1][y] = False
            visited[x][y - 1] = False

        """
        ㅁ
        ㅁㅁ
        """
        if x - 1 >= 0 and y + 1 < M and not visited[x - 1][y] and not visited[x][y + 1]:
            visited[x][y] = True
            visited[x - 1][y] = True
            visited[x][y + 1] = True
            backtracking(
                x, y + 1, _sum + 2 * graph[x][y] + graph[x - 1][y] + graph[x][y + 1]
            )
            visited[x][y] = False
            visited[x - 1][y] = False
            visited[x][y + 1] = False

        """
          ㅁ
        ㅁㅁ
        """
        if x - 1 >= 0 and y - 1 >= 0 and not visited[x - 1][y] and not visited[x][y - 1]:
            visited[x][y] = True
            visited[x - 1][y] = True
            visited[x][y - 1] = True
            backtracking(
                x, y + 1, _sum + 2 * graph[x][y] + graph[x - 1][y] + graph[x][y - 1]
            )
            visited[x][y] = False
            visited[x - 1][y] = False
            visited[x][y - 1] = False

    backtracking(x, y + 1, _sum)


backtracking(0, 0, 0)
print(result)
