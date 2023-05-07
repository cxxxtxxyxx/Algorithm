import string

def solution(n, t, m, p):
    
    # step 1: n진법, 미리 구할 숫자의 갯수 t, 게임을 참가하는 인원 m, 튜브의 순서 p
    
    
    answer = ''
    
    convertstr = ''
    num = 0
    
    for __ in range(t * m):
        convertstr += convert(num, n)
        num += 1
        
    return convertstr[p-1:t*m:m]


def convert(num, base) :
    tmp = string.digits+string.ascii_uppercase
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]