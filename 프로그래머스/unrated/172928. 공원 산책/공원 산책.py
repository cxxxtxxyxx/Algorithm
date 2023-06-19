def solution(park, routes):
    answer = []
    
    size_x, size_y, sx, sy = get_start_point_and_size(park)
    direct_dict = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
    for route in routes:
        change_route = route.split()
        direct = change_route[0]
        size = int(change_route[1])
        
        nx, ny = sx, sy
        for i in range(1, size + 1):
            nx, ny = sx + direct_dict[direct][0] * i, sy + direct_dict[direct][1] * i
            
            if not (0 <= nx < size_x and 0 <= ny < size_y):
                break
            if park[nx][ny] == "X":
                break
        
        else:
            sx, sy = nx, ny
            
        
        
    return [sx, sy]

def get_start_point_and_size(park):
    result = [len(park), len(park[0])]
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                result.append(i)
                result.append(j)
                return result