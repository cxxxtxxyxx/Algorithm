from collections import deque
def solution(board):
    answer = 0
    
    sx, sy = 0, 0
    ex, ey = 0, 0
    size_x = len(board)
    size_y = len(list(board[0]))
    for i in range(size_x):
        if 'R' in board[i]:
            sy = board[i].find('R')
            sx = i
        
        if 'G' in board[i]:
            ey = board[i].find('G')
            ex = i
            
        board[i] = list(board[i])
    return bfs(sx, sy, ex, ey, board, size_x, size_y)
    

def bfs(sx, sy, ex, ey, board, size_x, size_y):
    q = deque()
    visited = [[0] * size_y for __ in range(size_x)]
    visited[sx][sy] = 1
    q.append((sx, sy))
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while q:
        cx, cy = q.popleft()
        
        if board[cx][cy] == 'G':
            return visited[cx][cy] - 1
        
        # 네방향 끝까지
        for k in range(4):
            nx, ny = cx, cy
            while 0 <= dx[k] + nx < size_x and 0 <= dy[k] + ny < size_y and board[dx[k] + nx][dy[k] + ny] != 'D':
                nx += dx[k]
                ny += dy[k]
                
            if visited[nx][ny] == 0 and board[nx][ny] != 'D':
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
                
    return -1
    
