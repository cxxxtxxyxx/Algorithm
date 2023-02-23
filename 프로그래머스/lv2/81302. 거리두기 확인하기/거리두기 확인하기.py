from collections import deque

# dx = [0, 0, 1, -1, -1, 1, 1, -1]
# dy = [1, -1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(places):
    answer = []
    for place in places:
        tmp = []
        for line in place:
            tmp.append(list(line))
        coords = []
        for i in range(5):
            for j in range(5):
                if tmp[i][j] == 'P':
                    coords.append((i, j))
                    
        flag = False
        for coord in coords:
            visited = [[-1] * 5 for __ in range(5)]
            if bfs(coord[0], coord[1], visited, tmp) == 0:
                answer.append(0)
                flag = True
                break
                
        if flag == False:
            answer.append(1)
            
    return answer

def bfs(i, j, visited, place):
    
    q = deque()
    q.append((i, j))
    visited[i][j] = 0
    while q:
        
        x, y = q.popleft()
        
        if place[x][y] == 'P' and visited[x][y] != 0 and visited[x][y] != -1 and visited[x][y] <= 2:
            return 0
        
        for k in range(4):
            nx, ny = dx[k] + x, dy[k] + y
            
            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            
            if visited[nx][ny] == -1 and place[nx][ny] != 'X':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
    return 1
                
        


