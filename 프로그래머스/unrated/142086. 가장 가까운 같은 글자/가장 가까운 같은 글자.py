from collections import defaultdict
def solution(s):
    d = dict()
    answer = []
    
    for i in range(len(s)):
        if s[i] not in d:
            answer.append(-1)
            d[s[i]] = i
            continue
        answer.append(i - d[s[i]])
        d[s[i]] = i
    return answer
