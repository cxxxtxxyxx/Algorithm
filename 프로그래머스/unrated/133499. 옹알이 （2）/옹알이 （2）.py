def solution(babbling):
    answer = 0
    pronounce = ['aya','ye','woo','ma']
    for el in babbling:
        for p in pronounce:
            if p * 2 not in el:
                el = el.replace(p,' ')
        if len(el.strip())==0:
            answer +=1
    return answer