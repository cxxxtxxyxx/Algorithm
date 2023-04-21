def solution(n):
    answer = 0
    one_count = bin(n)[2:].count("1")
    
    # 1개수 똑같은거 나오면 return
    while True:
        n += 1
        
        if one_count == bin(n)[2:].count("1"):
            return n