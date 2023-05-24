import math
from itertools import chain
from collections import deque

def solution(board):
    _max = 0
    N = len(board)
    M = len(board[0])
    
    
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] != 0:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
                
                    
    return max(list(chain(*board))) ** 2



# def solution(board):
#     _max = 0
#     N = len(board)
#     M = len(board[0])
    
    
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 1:
#                 _max = max(_max, bfs(board, i, j, N, M))   
#     return math.pow(_max, 2)

dx = [0, 1, 1]
dy = [1, 1, 0]

def bfs(board, i, j, N, M):
    q = deque()
    q.append((i, j, 1))
    visited = [[False] * M for __ in range(N)]
    
    visited[i][j] = True
    
    while q:
        px, py, width = q.popleft()
        
        for k in range(3):
            nx, ny = px + dx[k], py + dy[k]
            
            if not (0 <= nx < N and 0 <= ny < M):
                return width
            
            if board[nx][ny] == 0:
                return width
            
            if visited[nx][ny] == False and board[nx][ny] == 1:
                q.append((nx, ny, width + 1))
                visited[nx][ny] = True
                
    return 1
            
        
        