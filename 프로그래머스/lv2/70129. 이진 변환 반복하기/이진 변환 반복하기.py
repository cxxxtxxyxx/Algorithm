def solution(s):
    answer = []
    prev_length = len(s)
    iter_count = 0
    remove_count = 0
    while s != "1":
        iter_count += 1
        s = s.replace("0", "")
        remove_count += prev_length - len(s)
        s = bin(len(s))[2:]
        prev_length = len(s)
    
    answer.append(iter_count)
    answer.append(remove_count)
    return answer