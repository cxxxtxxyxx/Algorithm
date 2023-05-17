def solution(numbers):
    answer = sorted(list(map(str, numbers)))
    answer.sort(key=lambda x: x*3, reverse=True)
    return str(int("".join(list(map(str, answer)))))