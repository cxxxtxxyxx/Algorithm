import sys

input = sys.stdin.readline

N = int(input().strip())

chess_borad = [list(map(int, input().strip().split())) for __ in range(N)]

white_board = [[0] * N for __ in range(N)]
black_board = [[0] * N for __ in range(N)]

for i in range(N):
    for j in range(N):
        if chess_borad[i][j] == 1:
            if i % 2 == 0 and j % 2 == 0:
                black_board[i][j] = 1
            
            if i % 2 == 1 and j % 2 == 1:
                black_board[i][j] = 1

            if i % 2 == 0 and j % 2 == 1:
                white_board[i][j] = 1
            
            if i % 2 == 1 and j % 2 == 0:
                white_board[i][j] = 1
        

def backtracking(x, y, result, coords, board):

    if y == N:
        x += 1
        y = 0

    if x == N and y == 0:
        return max(result, len(coords))
    
    if board[x][y] == 1:
        if (x, y) not in coords:
            if check_coord(x, y, coords):
                coords.append((x, y))
                result = max(result, backtracking(x, y + 1, result, coords, board))
                coords.pop()

        result = max(result, backtracking(x, y + 1, result, coords, board))

    else:
        result = max(result, backtracking(x, y + 1, result, coords, board))
    return result

def check_coord(x, y, coords):

    for px, py in coords:
        if abs(px - x) == abs(py - y):
            return False
        
    return True


print(backtracking(0, 0, 0, [], black_board) + backtracking(0, 0, 0, [], white_board))