def solution(babbling):
    answer = 0
    pronounce = {"aya":"b", "ye":"c", "woo":"d", "ma":"f"}
    change = "bcdf"
    sequence = []
    for i in range(2, 16):
        sequence.append("b" * i)
        sequence.append("c" * i)
        sequence.append("d" * i)
        sequence.append("f" * i)
        
    for i in range(len(babbling)):
        tmp = babbling[i]
        for p in pronounce.keys():
            if p in tmp:
                tmp = tmp.replace(p, pronounce[p])
        for s in sequence:
            if s in tmp:
                break
        else:
            for t in tmp:
                if t not in change:
                    break
            else:
                answer += 1


    return answer