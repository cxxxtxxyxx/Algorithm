import copy

def solution(m, n, board):
    answer = 0
    while True:
        coords = set()
        for i in range(m):
            for j in range(n):
                if (board[i][j] != '0' and can_remove(i, j, m, n, board)):
                    coords.add((i, j))
                    coords.add((i, j + 1))
                    coords.add((i + 1, j))
                    coords.add((i + 1, j + 1))

        if len(coords) == 0:
            return answer
        
        
        board = remove_block(coords, board, m, n)
        answer += len(coords)

def remove_block(coords, board, m, n):
    tempboard = [["0"] * (m) for __ in range(n)]
    
    for i in range(m):
        for j in range(n):
            tempboard[j][i] = board[i][j]
            
    for coord in coords:
        x, y = coord
        tempboard[y][x] = "0"
    
    for i in range(n):
        str = "".join(tempboard[i])
        start_idx = 0
        res_str = ''
        for j in range(len(str)):
            if str[j] != "0":
                res_str = res_str + str[j]
        
        tempboard[i] = ["0"] * (m - len(res_str)) + list(res_str)
                    
    
    tempboard2 = [["0"] * n for __ in range(m)]
    
    for i in range(m):
        for j in range(n):
            tempboard2[i][j] = tempboard[j][i]
    
    board = list(map("".join, tempboard2))
    return board
        

def can_remove(x, y, m, n, board):
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]
    
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        
        if not (0 <= nx < m and 0 <= ny < n):
            return False
        
        if board[x][y] != board[nx][ny]:
            return False
        
    return True
    
    