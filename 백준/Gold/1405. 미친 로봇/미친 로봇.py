# from itertools import product

# n, E, W, S, N = map(int, input().split())

# moves = list(product(['E', 'W', 'S', 'N'], repeat=n))

# move_dic = {
#   'E':(1, 0),
#   'W':(-1, 0),
#   'S':(0, -1),
#   'N':(0, 1)
# }
# result = 0

# for move in moves:
#   direction = [(0, 0)]
#   x, y = 0, 0
#   sum_ = 1
#   flag = 0
#   for coor in move:
#     if coor == 'E':
#       sum_ *= E / 100
#     elif coor == 'W':
#       sum_ *= W / 100
#     elif coor == 'S':
#       sum_ *= S / 100
#     else:
#       sum_ *= N / 100
#     x += move_dic[coor][0]
#     y += move_dic[coor][1]
#     if (x, y) in direction:
#       flag += 1
#       break
#     direction.append((x, y))
#   if flag == 0:
#     result += sum_

# print(result)

# dfs로풀기 / 백트래킹
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, E, W, S, N = map(int, input().split())
percent_val = [E, W, S, N]

graph = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]

answer = 0
def dfs(x, y, percent, cnt):
  global answer
  if cnt == n:
    answer += percent
    return

  now_percent = percent
  graph[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < (2 * n + 1) and 0 <= ny < (2 * n + 1):
      if graph[nx][ny] == 1:
        continue
      else:
        dfs(nx, ny, now_percent*(percent_val[i] / 100), cnt + 1)
        graph[nx][ny] = 0

dfs(n, n, 1, 0)
print(answer)