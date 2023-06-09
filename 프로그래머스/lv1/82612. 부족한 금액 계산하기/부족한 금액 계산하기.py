def solution(price, money, count):
    answer = price * count * (count + 1) // 2 - money
    return 0 if answer < 0 else answer