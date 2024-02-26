import sys

input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for __ in range(9)]

blank_coords = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank_coords.append((i, j))


def backtracking(blank_coords_idx):

    if blank_coords_idx == len(blank_coords):
        for line in sudoku:
            print(*line)
        exit(0)

    x = blank_coords[blank_coords_idx][0]
    y = blank_coords[blank_coords_idx][1]
    for i in range(10):
        if check_row(x, i) and check_col(y, i) and check_3x3(x, y, i):
            sudoku[x][y] = i
            backtracking(blank_coords_idx + 1)
            sudoku[x][y] = 0


def check_row(x, value):
    for i in range(9):
        if sudoku[x][i] == value:
            return False
    return True

def check_col(y, value):
    for i in range(9):
        if sudoku[i][y] == value:
            return False
    return True

def check_3x3(x, y, value):

    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if sudoku[nx + i][ny + j] == value:
                return False
            
    return True

backtracking(0)