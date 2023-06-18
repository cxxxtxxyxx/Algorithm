def solution(s, skip, index):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    
    for ch in skip:
        alpha.remove(ch)
        
    answer = ""
    
    for i in range(len(s)):
        answer += alpha[(alpha.index(s[i]) + index) % len(alpha)]
    return answer