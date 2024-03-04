import sys

input = sys.stdin.readline

N = int(input().strip())

chess = [list(map(int, input().strip().split())) for __ in range(N)]

white_chess = [[0] * N for __ in range(N)]
black_chess = [[0] * N for __ in range(N)]

for i in range(N):
    for j in range(N):
        if chess[i][j] == 1:
            if i % 2 == 0 and j % 2 == 0:
                white_chess[i][j] = 1
            
            if i % 2 == 1 and j % 2 == 1:
                white_chess[i][j] = 1

            if i % 2 == 0 and j % 2 == 1:
                black_chess[i][j] = 1

            if i % 2 == 1 and j % 2 == 0:
                black_chess[i][j] = 1

result = 0

def backtracking(x, y, coords, board):

    global result

    if y == N:
        x += 1
        y = 0

    if x == N and y == 0:
        result = max(result, len(coords))
        return
    
    if board[x][y] == 0:
        backtracking(x, y + 1, coords, board)
        return
    

    for px, py in coords:
        if abs(x - px) == abs(y - py):
            break

    else:
        coords.append((x, y))
        backtracking(x, y + 1, coords, board)
        coords.pop()

    backtracking(x, y + 1, coords, board)

backtracking(0, 0, [], white_chess)
_sum = result
result = 0

backtracking(0, 0, [], black_chess)
print(_sum + result)