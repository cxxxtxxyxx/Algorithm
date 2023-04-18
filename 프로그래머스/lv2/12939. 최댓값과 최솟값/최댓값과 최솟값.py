def solution(s):
    res = list(map(int, s.split(" ")))
    answer = str(min(res)) + " " + str(max(res))
    return answer