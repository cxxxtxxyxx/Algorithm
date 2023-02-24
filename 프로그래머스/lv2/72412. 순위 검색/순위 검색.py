from itertools import combinations
from bisect import bisect_left, bisect_right

def solution(info, query):
    answer = []
    cnt_dict = {}
    for i in range(len(info)):
        el = info[i].split(" ")
        info_key = el[:-1]
        info_value = el[-1]
        
        for j in range(5):
            for c in combinations(info_key, j):
                tmp = ''.join(c)
                if tmp in cnt_dict:
                    cnt_dict[tmp].append(int(info_value))
                    
                else:
                    cnt_dict[tmp] = [int(info_value)]
                    
    for k in cnt_dict:
        cnt_dict[k].sort()
        
    for state in query:
        res = state.split(' ')
        state_key = res[:-1]
        state_value = res[-1]
        
        while 'and' in state_key:  # and 제거
            state_key.remove('and')
        while '-' in state_key:  # - 제거
            state_key.remove('-')
        state_key = ''.join(state_key)
        
        
        if state_key in cnt_dict:
            scores = cnt_dict[state_key]
            if scores:
                enter = bisect_left(scores, int(state_value))

                answer.append(len(scores) - enter)
                
        else:
            answer.append(0)
                
    return answer