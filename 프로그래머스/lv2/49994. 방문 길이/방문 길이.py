from itertools import chain


def solution(dirs):

    direct = dict()
    direct["U"] = (-1, 0)
    direct["D"] = (1, 0)
    direct["L"] = (0, -1)
    direct["R"] = (0, 1)
    
    cx, cy = 5, 5
    visited = set()
    for dir in dirs:
        
        dx, dy = direct[dir]
        nx, ny = cx + dx, cy + dy
        if not (0 <= nx < 11 and 0 <= ny < 11):
            continue
        
        visited.add((cx, cy, nx, ny))
        visited.add((nx, ny, cx, cy))
        cx, cy = nx, ny
        

    return len(visited) // 2