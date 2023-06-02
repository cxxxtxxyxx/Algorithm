def solution(k, ranges):
    answer = []
    
    # step 1: 우박 수열 구함
    coords = get_sequence_coords(k)
    areas = get_areas(coords)
    _sum = areas[0]
    cumulative_sum = [_sum]
    for i in range(1, len(areas)):
        _sum += areas[i]
        cumulative_sum.append(_sum)
    print(cumulative_sum)
    print(areas)
    # step 2: 각 구간넓이 구하기 
    # = 두 좌표 중 x 좌표 큰 거, y좌표 작은거 직사각형 + x 좌표 큰거 + y 좌표 큰거 넓이 절반
    # 시작 구간이 끝 구간보다 크면 -1
    # 구간별 더하기
    
    for r in ranges:
        start, end = r
        if start == 0 and end == 0:
            answer.append(cumulative_sum[-1])
            continue
        end = len(coords) + end - 1
        
        
        if start == end:
            answer.append(0)
        elif start > end:
            answer.append(-1)
        elif start == 0:
            answer.append(cumulative_sum[end - 1])
        elif start - end == 1:
            answer.append(cumulative_sum[end - 1])
        else:
            answer.append(cumulative_sum[end - 1] - cumulative_sum[start - 1])
            
            
            
    
    return answer

def get_areas(coords):
    result = []
    sx, sy = coords[0]
    
    for i in range(1, len(coords)):
        ex, ey = coords[i]
        min_y = min(sy, ey)
        max_y = max(sy, ey)
        size =  max_y - (max_y - min_y) / 2
        result.append(size)
        sx, sy = ex, ey
        
    return result

def get_sequence_coords(k):
    i = 1
    
    result = [(0, k)]
    
    while k != 1:
        if k % 2 == 0:
            k //= 2
            result.append((i, k))
        else:
            k *= 3
            k += 1
            result.append((i, k))
        
        i += 1
    return result
    
    