import string

def solution(n, t, m, p):
    
    # step 1: n진법, 미리 구할 숫자의 갯수 t, 게임을 참가하는 인원 m, 튜브의 순서 p
    
    
    answer = ''
    
    convertstr = ''
    num = 0
    
    for __ in range(t * m):
        convertstr += convert(num, n)
        num += 1
        
    for i in range(p - 1, len(convertstr), m):
        if len(answer) != t:
            answer += convertstr[i]
            continue
        break
    return answer


def convert(num, base) :
    tmp = string.digits+string.ascii_uppercase
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]