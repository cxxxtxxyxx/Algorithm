import string

def solution(n):
    _num3 = convert(n, 3)
    _num3 = int(_num3[::-1].lstrip('0'))
    
    x = _num3
    _sum = 0
    cal = 1
    while x > 0:
        r = x % 10
        _sum += cal * r
        x //= 10
        cal *= 3
    
    return _sum


def convert(num, base) :
    tmp = string.digits+string.ascii_lowercase
    
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]