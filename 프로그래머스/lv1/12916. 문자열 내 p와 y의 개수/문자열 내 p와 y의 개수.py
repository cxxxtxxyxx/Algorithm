def solution(s):
    answer = True
    
    s = s.lower()
    scnt = len(list(filter(lambda x: x == 'p', list(s))))
    ycnt = len(list(filter(lambda x: x == 'y', list(s))))
    
    if scnt == 0 and ycnt == 0:
        return True
    
    if scnt != ycnt:
        return False
    return True